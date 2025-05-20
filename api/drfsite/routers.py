from rest_framework import routers

from drfsite.views import *


def router():
    _router = routers.DefaultRouter()
    _router.register('employee', EmployeeViewSet, )
    _router.register('work_status', WorkStatusViewSet, )
    _router.register('address', AddressViewSet, )
    _router.register('company', CompanyViewSet, )
    _router.register('priority', PriorityViewSet, )
    _router.register('application', ApplicationViewSet, )
    _router.register('work_plan_status', WorkPlanStatusViewSet, )
    _router.register('zip', ZipViewSet, )
    _router.register('zip_object', ZipObjectViewSet, )
    _router.register('work_plan', WorkPlanViewSet, )
    _router.register('chat', ChatViewSet, )
    _router.register('message', MessageViewSet, )

    return _router
