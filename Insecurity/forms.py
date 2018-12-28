from django.forms import ModelForm
from .models import InsecureModel

class InsecureForm(ModelForm):
    class Meta:
        model=InsecureModel
        fields=('title','description','file')
    
