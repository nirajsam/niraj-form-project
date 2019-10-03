from django.shortcuts import render
from . import forms
# Create your views here.
def thankyou_view(request):
    return render(request,'testapp/thankyou.html')

def studentregisterview(request):
    if request.method=='GET':
        form=forms.studentRegistration()
        
    if request.method=='POST':
        form=forms.studentRegistration(request.POST)
        if form.is_valid():
            print('validation completed..printing feedback info')
            print('student name:',form.cleaned_data['name'])
            print('student roll:',form.cleaned_data['roll'])
            print('student email:',form.cleaned_data['email'])
            print('student feedback:',form.cleaned_data['feedback'])
            return thankyou_view(request)

    return render(request,'testapp/register.html',{'form':form})
