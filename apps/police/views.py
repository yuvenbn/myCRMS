from django.shortcuts import render
from apps.police_stations.models import PoliceStation
from apps.authentication.models import CustomUser, Police
from django.shortcuts import render, redirect



from django.contrib import messages
# Create your views here.

def add_police(request):
    context = {
        'police_stations': PoliceStation.objects.all()
    }
    if( request.method == 'POST' ):
        #collect user data
        user_attributes = {
            'email':request.POST['email'],
            'first_name':request.POST['first_name'],
            'last_name':request.POST['last_name'],
            'phone_number':request.POST['phone_number'], 
            'password':request.POST['password'],
        }
        #create user object and level
        user = CustomUser.objects.create_user(**user_attributes) 
        user.user_level = 'police'
        user.save()
        
        #collect data to create police
        police_attributes = {
            'user':user,
            'admin':request.user, #creator
            'policeID':request.POST['policeID'],
            'police_station':PoliceStation.objects.get(id=request.POST['police_station']),     
        }
        
        #checking if theres is already a police with that policeID
        if( Police.objects.filter(policeID=request.POST['policeID']) ):
            messages.success(request, 'Police with same ID already exist !')
        else:
            #create police
            Police.objects.create(**police_attributes)
            messages.success(request, 'Police added successfully !')
        return redirect('/police/add')

    return render(request, 'police/add_police.html', context)

def edit_police(request, pk):
    return render(request, 'police/edit_police.html')

def manage_police(request):
    return render(request, 'police/police.html') 