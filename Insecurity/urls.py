from django.urls import path
from .views import results,insecure_form_handling,search
urlpatterns=[
        path('',results,name='results'),
        path('form/',insecure_form_handling,name='insecure_form_handling'),
        path('form/<str:string>',search,name='search_all')
        ]
