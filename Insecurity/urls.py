from django.urls import path
from .views import results,insecure_form_handling,search
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
        path('',results,name='results'),
        path('form/',insecure_form_handling, name='insecure_form_handling'),
        path('search/',search, name='search_all')
        ] 
