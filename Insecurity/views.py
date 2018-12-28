from django.shortcuts import render
from django.http import HttpResponse
from .forms import InsecureForm
def results(request):
    return render(request,'results.html',{})

def insecure_form_handling(request):
    if request.method=="POST":
        form=InsecureForm(request.POST,request.FILES)
        if form.is_valid():
            print(request)
            form.save()
        return render(request,'form.html',context={'form':form})
    else:
        form = InsecureForm()
        return render(request,'form.html',context={'form':form})
