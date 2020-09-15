from django.urls import path
from . import views

urlpatterns = [
    path('legalNotice/legal_notice/<str:name>', views.legal_notice, name="legalNotice"),
]