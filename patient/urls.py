from django.urls import path
from . views import PatientListView
from . import views

urlpatterns = [
        path('', PatientListView.as_view(), name='patient'),
        path('add_patient/', views.add_referral, name='add_refferal')
]
