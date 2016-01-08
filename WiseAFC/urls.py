# encoding: UTF-8
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from login import views as login_views
from afc import views as afc_views


router = routers.DefaultRouter()
router.register(r'users', login_views.UserViewSet)
router.register(r'groups', login_views.GroupViewSet)
router.register(r'passengers', afc_views.PassengerViewSet)
router.register(r'company', afc_views.CompanyViewSet)
router.register(r'supervisors', afc_views.SupervisorViewSet)
router.register(r'vehicles', afc_views.VehicleViewSet)
router.register(r'tickets', afc_views.TicketViewSet)
router.register(r'receipt', afc_views.ReceiptViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'WiseAFC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),

    url(r'^admin/', include(admin.site.urls)),
]
