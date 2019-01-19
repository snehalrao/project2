from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def calc(request):
    field1=request.GET['field1']
    field2=request.GET['field2']
    operation=request.GET['op']
    result=0
    if operation=='+':
        result=int(field1)+int(field2)
    elif operation=='-':
        result=int(field1)-int(field2)
    elif operation=='/':
        result=int(field1)/int(field2)
    else:
        result=int(field1)*int(field2)

    return render(request,'calc.html',{'result':result})