from django.contrib.auth.models import AbstractUser, User
from django.db import models


class WorkStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название
    is_active = models.BooleanField(default=True)  # Название
    permission = models.BooleanField(default=False)  # Доступ

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь с моделью User
    patronymic = models.CharField(max_length=30, blank=True)  # Отчество
    phone = models.CharField(max_length=15)  # Телефон
    work_status = models.ForeignKey(WorkStatus, on_delete=models.SET_NULL,
                                    related_name='employees', null=True, blank=True)  # Связь с моделью WorkStatus
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} {self.patronymic} - {self.work_status}"


class Address(models.Model):
    street = models.CharField(max_length=255)  # улица
    house_number = models.CharField(max_length=10)  # номер дома
    is_active = models.BooleanField(default=True)  # заменяет удаления на "неактивно"
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.street}, {self.house_number}"


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь с моделью User
    name = models.CharField(max_length=255, unique=True)  # название компании
    addresses = models.ManyToManyField(Address, related_name='addresses')  # связь с Address, филиалы компании

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Название приоритета
    is_active = models.BooleanField(default=True)  # заменяет удаление

    def __str__(self):
        return self.name


class Application(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE,
                                related_name='applications')  # связь с моделью Company
    address = models.ForeignKey('Address', on_delete=models.CASCADE,
                                related_name='applications')  # связь с моделью Address
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True,
                                 related_name='applications')  # Внешний ключ на приоритет
    lastname = models.CharField(max_length=100)  # Контактное лицо
    firstname = models.CharField(max_length=100)  # Контактное лицо
    patronymic = models.CharField(max_length=100)  # Контактное лицо
    phone = models.CharField(max_length=15)  # Телефон
    email = models.EmailField()  # E-mail
    serial_number = models.CharField(max_length=50)  # Серийный номер
    equipment_name = models.CharField(max_length=100)  # Наименование оборудования
    location_in_room = models.CharField(max_length=100)  # Расположение в зале
    ip_management_interface = models.GenericIPAddressField(protocol='both', unpack_ipv4=True,
                                                           null=True)  # IP Management Interface
    equipment_non_operational = models.BooleanField(default=False)  # Оборудование полностью неработоспособно
    functionality_limited = models.CharField(
        max_length=255)  # Неисправность ограничивает полный функционал оборудования
    suspicion_of_logical_errors = models.CharField(
        max_length=255)  # Подозрение на логические ошибки
    fault_description = models.TextField()  # Описание неисправности
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания заявки

    def __str__(self):
        return f"Заявка от {self.lastname} {self.firstname} {self.patronymic} на оборудование {self.equipment_name}"


class WorkPlanStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название статуса
    is_active = models.BooleanField(default=True)  # Заменяет удаление

    def __str__(self):
        return self.name


class Zip(models.Model):
    type = models.CharField(max_length=255)  # Тип запасной части
    name = models.CharField(max_length=255)  # Название запасной части
    article_number = models.CharField(max_length=50)  # Артикул

    unit = models.CharField(max_length=50)  # Единица измерения
    is_active = models.BooleanField(default=True)


class ZipObject(models.Model):
    zip = models.ForeignKey(Zip, on_delete=models.CASCADE, related_name='zips')
    quantity = models.PositiveIntegerField()  # Количество
    created_at = models.DateField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')  # Отправитель сообщения
    content = models.TextField()  # Содержимое сообщения
    timestamp = models.DateTimeField(auto_now_add=True)  # Время отправки сообщения


class Chat(models.Model):
    message = models.ManyToManyField(Message, related_name='chats', blank=True)


class WorkPlan(models.Model):
    application = models.ForeignKey('Application', on_delete=models.CASCADE,
                                    related_name='work_plans')  # Внешний ключ на заявку
    responsible = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                    related_name='responsible_work_plans', null=True, blank=True)  # Ответственный
    engineer = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='engineer_work_plans', null=True,
                                 blank=True)  # Инженер
    status = models.ForeignKey(WorkPlanStatus, related_name='work_plans', on_delete=models.SET_NULL, null=True,
                               blank=True)  # Статус выполнения
    zip_resources = models.ManyToManyField(ZipObject, related_name='work_plans',
                                           blank=True)  # ЗИП (запасные части и материалы)
    start_date = models.DateField(null=True, blank=True)  # Дата начала работы
    end_date = models.DateField(null=True, blank=True)  # Дата окончания работы
    tasks = models.TextField(null=True, blank=True)  # Задачи в рабочем плане
    notes = models.TextField(null=True, blank=True)  # Примечания
    is_agreed = models.BooleanField(default=False)  # Согласованность заявки
    chat_with_client = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='work_plans_0')
    chat_with_employee = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='work_plans_9')

    def __str__(self):
        return f"Рабочий план для заявки {self.application.id} - Ответственный: {self.responsible.user.last_name} {self.responsible.user.first_name} {self.responsible.patronymic}"
