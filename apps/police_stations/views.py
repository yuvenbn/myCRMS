from django.shortcuts import render
from .models import PoliceStation
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib import messages

# Create your views here.
@login_required(login_url='login') 
def add_police_station(request):
    if(request.method == 'POST'):
        data = {
            'admin':request.user,
            'name':request.POST['name'],
            'code':request.POST['code'],
        }

        police_station = PoliceStation.objects.create(**data)
        messages.success(request, 'Police station added successfully!', extra_tags="success")
        return redirect('/police-stations/add')

    return render(request, 'police_stations/add_police_station.html')

def edit_police_station(request, pk):
    context = {
        'police_station':PoliceStation.objects.get(id=pk)
    }
    if(request.method == 'POST'):
        data = {
            'name':request.POST['name'],
            'code':request.POST['code'],
        }

        PoliceStation.objects.filter(id=pk).update(**data)
        messages.success(request, 'Police station Updated successfully!', extra_tags="success")
        return redirect(f'/police-stations/edit/{pk}')

    return render(request, 'police_stations/edit_police_station.html', context)


def delete_police_station(request, pk):
  
        PoliceStation.objects.filter(id=pk).delete()
        messages.success(request, 'Police Station Deleted successfully!', extra_tags="success")
        return redirect(f'/police-stations/')

def manage_police_stations(request):
    context = {
        'police_stations':PoliceStation.objects.all()
    }
    return render(request, 'police_stations/police_stations.html', context)