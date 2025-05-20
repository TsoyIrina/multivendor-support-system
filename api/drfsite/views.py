from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from drfsite.permission import *
from drfsite.serializers import *


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminOrAuthForReadOnlyOrCurrentUser,)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Employee.objects.get(pk=pk)
            user_instance = instance.user
        except:
            return Response({"error": "Object does not exists"})

        try:
            data = request.data.dict()
            user_data = {'username': data.pop('user.username'),
                         'last_name': data.pop('user.last_name'),
                         'first_name': data.pop('user.first_name'),
                         'is_active': data.pop('user.is_active'),
                         'is_superuser': WorkStatus.objects.get(id=data['work_status']).permission, }
        except:
            data = request.data
            user_data_sup = data.pop('user')
            user_data = {'username': user_data_sup.get('username'),
                         'last_name': user_data_sup.get('last_name'),
                         'first_name': user_data_sup.get('first_name'),
                         'is_active': user_data_sup.get('is_active'),
                         'is_superuser': WorkStatus.objects.get(id=data['work_status']).permission, }

        user_serializer = UserSerializer(data=user_data, instance=user_instance)
        user_serializer.is_valid(raise_exception=True)
        serializer = EmployeeSerializer(data=data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_serializer.save()

        return Response({"post": serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user.is_active = False
        instance.user.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], name='get_current_employee')
    def get_current(self, request, *args, **kwargs):
        employee = Employee.objects.get_or_create(user=request.user)[0]
        serializer = self.get_serializer(employee)
        return Response(serializer.data)


class WorkStatusViewSet(viewsets.ModelViewSet):
    queryset = WorkStatus.objects.all()
    serializer_class = WorkStatusSerializer
    permission_classes = (IsAdminOrAuthForReadOnly,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (IsAuth,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        for company in instance.addresses.all():
            company.addresses.remove(instance)
            company.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAdminOrAuthForReadOnlyOrCurrentUser,)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Company.objects.get(pk=pk)
            user_instance = instance.user
        except:
            return Response({"error": "Object does not exists"})

        try:
            data = request.data.dict()
            user_data = {'username': data.pop('user.username'),
                         'is_active': data.pop('user.is_active'), }
        except:
            data = request.data
            user_data_sup = data.pop('user')
            user_data = {
                'username': user_data_sup.get('username'),
                'is_active': user_data_sup.get('is_active'),
            }

        data['addresses_id'] = [int(_) for _ in data.get('addresses_id', [])]
        user_serializer = UserSerializer(data=user_data, instance=user_instance)
        user_serializer.is_valid(raise_exception=True)
        serializer = CompanySerializer(data=data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_serializer.save()

        return Response({"post": serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user.is_active = False
        instance.user.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], name='get_current_company')
    def get_current(self, request, *args, **kwargs):
        company = Company.objects.get_or_create(user=request.user)[0]
        serializer = self.get_serializer(company)
        return Response(serializer.data)


class PriorityViewSet(viewsets.ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer
    permission_classes = (IsAdminOrAuthForReadOnly,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuth,)


class WorkPlanStatusViewSet(viewsets.ModelViewSet):
    queryset = WorkPlanStatus.objects.all()
    serializer_class = WorkPlanStatusSerializer
    permission_classes = (IsAdminOrAuthForReadOnly,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ZipViewSet(viewsets.ModelViewSet):
    queryset = Zip.objects.all()
    serializer_class = ZipSerializer
    permission_classes = (IsAuth,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ZipObjectViewSet(viewsets.ModelViewSet):
    queryset = ZipObject.objects.all()
    serializer_class = ZipObjectSerializer
    permission_classes = (IsAuth,)


class WorkPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkPlan.objects.all()
    serializer_class = WorkPlanSerializer
    permission_classes = (IsAuth,)


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuth,)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuth,)
