

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm
from .models import CustomUser, Police

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

def landing_page_view(request):
    return render(request, 'accounts/landing_page.html')

def register_view(request, user_level):
   
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        user = CustomUser.objects.create_user( email, first_name, last_name, phone_number, password)

        #set user level
        if(user_level == 'admin'):
            user.user_level = 'admin'
            user.save()
        else:
            user.user_level = 'user'
            user.save()
         
        # login the user
        # login(request, user)

        # Redirect to a success page or any other desired page
        return redirect(f'/accounts/login/level={user_level}')
    else:
        return render(request, 'accounts/register.html', {'user_level': user_level})

def login_view(request, user_level):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid email or password'
    else:
        error_message = ''
        messages.success(request,'Welcome, please remember to logout when done')
    context= {
             'error_message': error_message,
             'user_level':user_level,
             }
    return render(request, 'accounts/login.html', context)

def police_login_view(request):
    if request.method == 'POST':
        policeID = request.POST.get('policeID')
        password = request.POST.get('password')

        try:
            email = Police.objects.get(policeID=policeID).user.email
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error_message = 'Invalid ID OR password'
        except Police.DoesNotExist:
             error_message = 'Invalid ID or password'
    else:
        error_message = ''
        messages.success(request,'Welcome, please remember to logout when done')
    context= {
             'error_message': error_message,
             }
    return render(request,'accounts/police_login.html')

def logout_view(request):
    logout(request)
    return redirect('login') 

# account management
def edit_profile_view(request):
    user = request.user
    context = {
        'user':user
    }
    if request.method == 'POST':
        try:
            # Save the POST arguements
            data = request.POST

            attributes = {
                "first_name": data['first_name'],
                "last_name": data['last_name'],
                "phone_number": data['phone_number'],
                
            }
            
            #update user info
            CustomUser.objects.filter(id=user.id).update(**attributes)
     

            # category = Category.objects.get(id=category_id)

            messages.success(request, 'Profile updated successfully!', extra_tags="success")
            return redirect('edit-profile')
        except Exception as e:
            messages.success(
                request, 'There was an error during the update!', extra_tags="danger")
            print(e)
            return redirect('edit-profile')
    return render(request, 'accounts/edit_profile.html')

def change_password_view(request):
    user = request.user
    context = { 
        'user':user,
       
    }
    return render(request, 'accounts/change_password.html', context)


def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Validate the passwords
        user = authenticate(email=request.user.email, password=current_password)
        if user is not None:
            if new_password == confirm_password:
                # Update the user's password
                user.set_password(new_password)
                user.save()

                # Log in the user with the new password
                login(request, user)

                messages.success(request, 'Your password has been successfully changed.')
                return redirect('home')  
            else:
                messages.error(request, 'New password and confirmation password do not match.')
        else:
            messages.error(request, 'Incorrect current password.')
    
    return render(request, 'accounts/change_password.html')