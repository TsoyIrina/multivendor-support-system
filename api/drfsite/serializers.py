from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from drfsite.models import *


class WorkStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkStatus
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    password = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'last_name', 'first_name', 'is_active', 'is_superuser']

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.last_name = validated_data.get('last_name', '')
        instance.first_name = validated_data.get('first_name', '')
        instance.is_active = validated_data['is_active']
        instance.is_superuser = validated_data.get('is_superuser', False)
        instance.save()
        return instance


class EmployeeSerializer(serializers.ModelSerializer):
    work_status = serializers.PrimaryKeyRelatedField(read_only=False, queryset=WorkStatus.objects.all())
    user = UserSerializer(read_only=False, required=False)

    class Meta:
        model = Employee
        fields = ['id', 'user', 'patronymic', 'work_status', 'birthdate', 'phone']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(username=user_data['username'],
                                   last_name=user_data['last_name'],
                                   first_name=user_data['first_name'],
                                   is_active=user_data['is_active'],
                                   is_superuser=validated_data['work_status'].permission)
        user.set_password(user_data['password'])
        user.save()
        employee = None
        try:
            employee = Employee.objects.create(user=user, **validated_data)
        except:
            user.delete()
        return employee

    def to_representation(self, instance):
        rep = super(EmployeeSerializer, self).to_representation(instance)
        rep['work_status'] = {'id': instance.work_status.id, 'name': instance.work_status.name,
                              'permission': instance.work_status.permission}
        rep['date_joined'] = str(instance.user.date_joined)[:10]
        return rep


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False, required=False)
    addresses = AddressSerializer(many=True, read_only=True, )
    addresses_id = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Address.objects.all(),
                                                      required=False)

    class Meta:
        model = Company
        fields = ['id', 'user', 'name', 'addresses', 'addresses_id', ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(username=user_data['username'],
                                   is_active=user_data['is_active'], )
        user.set_password(user_data['password'])
        user.save()
        company = None
        try:
            company = Company.objects.create(user=user, **validated_data)
        except:
            user.delete()
        return company

    def update(self, instance, validated_data):
        addresses = validated_data.get('addresses_id', None)
        instance.name = validated_data['name']
        instance.addresses.set(addresses)
        instance.save()
        return instance

    def to_representation(self, instance):
        rep = super(CompanySerializer, self).to_representation(instance)
        rep['date_joined'] = str(instance.user.date_joined)[:10]
        return rep


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True, )
    address = AddressSerializer(read_only=True, )
    priority = PrioritySerializer(read_only=True, )
    company_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Company.objects.all())
    address_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Address.objects.all())
    priority_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Priority.objects.all())

    class Meta:
        model = Application
        fields = ['id', 'company', 'company_id', 'address_id', 'priority_id', 'address', 'priority', 'lastname',
                  'firstname',
                  'patronymic', 'phone', 'email', 'serial_number', 'equipment_name', 'location_in_room',
                  'ip_management_interface', 'equipment_non_operational', 'functionality_limited',
                  'suspicion_of_logical_errors', 'fault_description', 'created_at']

    def create(self, validated_data):
        validated_data['company_id'] = validated_data.get('company_id').id
        validated_data['address_id'] = validated_data.get('address_id').id
        validated_data['priority_id'] = validated_data.get('priority_id').id
        application = Application.objects.create(**validated_data)

        chat_with_client = Chat.objects.create()
        chat_with_client.save()
        chat_with_employee = Chat.objects.create()
        chat_with_employee.save()


        work_plan = WorkPlan.objects.create(application=application, chat_with_client=chat_with_client,
                                            chat_with_employee=chat_with_employee, status_id=1)
        work_plan.save()
        return application

    def update(self, instance, validated_data):
        validated_data['company_id'] = validated_data.get('company_id').id
        validated_data['address_id'] = validated_data.get('address_id').id
        validated_data['priority_id'] = validated_data.get('priority_id').id
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)
        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()
        return instance


class WorkPlanStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlanStatus
        fields = '__all__'


class ZipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zip
        fields = '__all__'


class ZipObjectSerializer(serializers.ModelSerializer):
    zip = ZipSerializer(many=False, read_only=True)
    zip_id = serializers.PrimaryKeyRelatedField(write_only=True, required=False, queryset=Zip.objects.all())

    class Meta:
        model = ZipObject
        fields = '__all__'

    def create(self, validated_data):
        validated_data['zip_id'] = validated_data['zip_id'].id
        zip_object = ZipObject.objects.create(**validated_data)
        zip_object.save()
        return zip_object


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp', 'sender_id']

    def create(self, validated_data):
        validated_data['sender_id'] = validated_data['sender_id'].id
        message = Message.objects.create(**validated_data)
        message.save()
        return message


class ChatSerializer(serializers.ModelSerializer):
    message = MessageSerializer(many=True, read_only=True)
    messages_id = serializers.PrimaryKeyRelatedField(many=True, write_only=True, required=False,
                                                     queryset=Message.objects.all())

    class Meta:
        model = Chat
        fields = ('id', 'message', 'messages_id')

    def update(self, instance, validated_data):
        instance.message.set(validated_data['messages_id'])
        instance.save()
        return instance

class WorkPlanSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(read_only=True)
    responsible = EmployeeSerializer(read_only=True)
    responsible_id = serializers.PrimaryKeyRelatedField(write_only=True, required=False,
                                                        queryset=Employee.objects.all())
    engineer = EmployeeSerializer(read_only=True)
    engineer_id = serializers.PrimaryKeyRelatedField(write_only=True, required=False, queryset=Employee.objects.all())
    status = WorkPlanStatusSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(write_only=True, required=False,
                                                   queryset=WorkPlanStatus.objects.all())
    zip_resources = ZipObjectSerializer(many=True, read_only=True)
    zip_resources_id = serializers.PrimaryKeyRelatedField(many=True, write_only=True, required=False,
                                                          queryset=ZipObject.objects.all())
    chat_with_client = ChatSerializer(read_only=True)
    chat_with_employee = ChatSerializer(read_only=True)

    class Meta:
        model = WorkPlan
        fields = ['id', 'application', 'responsible', 'responsible_id', 'engineer', 'engineer_id', 'status',
                  'status_id', 'zip_resources', 'zip_resources_id', 'start_date', 'end_date',
                  'tasks', 'notes', 'is_agreed', 'chat_with_client', 'chat_with_employee']

    def update(self, instance, validated_data):
        instance.zip_resources.set(validated_data['zip_resources_id'])
        instance.responsible = validated_data['responsible_id']
        instance.engineer = validated_data['engineer_id']
        instance.status = validated_data['status_id']
        instance.start_date = validated_data['start_date']
        instance.end_date = validated_data['end_date']
        instance.tasks = validated_data['tasks']
        instance.notes = validated_data['notes']
        instance.is_agreed = validated_data['is_agreed']
        instance.save()
        return instance
