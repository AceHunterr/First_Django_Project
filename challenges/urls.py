from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.jan),
    # path("february", views.feb),
    path("<int:month>", views.monthly_challenge_by_no), # Order also matters here we first wanna check for int then str
    path("<str:month>", views.monthly_challenge)
]
