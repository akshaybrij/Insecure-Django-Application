from django.urls import path
from .views import results,insecure_form_handling
urlpatterns=[
        path('',results),
        path('form/',insecure_form_handling)
        ]
