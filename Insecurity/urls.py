from django.urls import path
from .views import results,insecure_form_handling
urlpatterns=[
        path('',results,name='results'),
        path('form/',insecure_form_handling,name='insecure_form_handling')
        ]
