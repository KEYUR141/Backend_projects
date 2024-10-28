from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import formsubmission



def cal(request):
   ans =''
   info={}
   try:
      if request.method=="POST":
        n1 = eval(request.POST.get('num1'))
        n2 = eval(request.POST.get('num2'))
        opr = request.POST.get('option')
        if opr == "+":
            ans = n1+n2
        elif opr == "-":
            ans = n1-n2
        elif opr == "*":
            ans = n1*n2
        elif opr =="/":
           ans = n1/n2
        info={
           'n1':n1,
           'n2':n2,
           'ans':ans
        }
        
      
   except:
      ans = "Invalid Operation"
    
   return render(request,'form.html',info)
 


