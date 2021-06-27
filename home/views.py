from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model
import uuid
from django.contrib import messages





# Create your views here.
User = get_user_model()




def registeruser(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            phone_number = request.POST.get('phonenumber')
            password = request.POST.get('password')
            email_token = uuid.uuid4()

            users = User(
                email = email,
                phone = phone_number,
                emailtoken = email_token
            )   
            users.set_password(password)
            users.save()
           
            print('account created')
            return redirect('/login/')


    except Exception as e:
           print(e)
    return render(request, 'register.html')
           
def verify_user(request , token):
    try:
        user_obj = User.objects.get(emailtoken = token)
        user_obj.is_verified = True
        user_obj.save()
        return HttpResponse('Your account is verified')
    except Exception as e:
        print(e)
    return HttpResponse('Invalid Token')



def loginuser(request):
    return HttpResponse('login')    