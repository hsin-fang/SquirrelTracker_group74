from django.shortcuts import render
from .models import Sight
from django.shortcuts import redirect
from .forms import SightForm


# Create your views here.
def homepage_view(request):
    return render(request,'sightings/homepage.html')

def map_view(request):
    sights = Sight.objects.all()[:100]
    context = {
            'sights':sights,
            }
    return render(request, 'sightings/map.html', context)


def list_sights(request):
    sights = Sight.objects.all()
    fields = ['Unique_Squirrel_Id','Longtitude','Latitude','Date','Shift']
    context = {
            'sights':sights,
            'fields':fields,
            }
    return render(request, 'sightings/list.html', context)


def update_sights(request,Unique_Squirrel_Id):
    sight = Sight.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    if request.method == 'POST':
        form = SightForm(request.POST, instance = sight)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightForm(instance = sight)

    context = {
            'form':form,
            }
    return render(request, 'sightings/update.html', context)


def add_sights(request):
    if request.method == 'POST':
        form = SightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightForm()

    context = {
            'form':form,
            }

    return render(request, 'sightings/add.html', context)


def stats_view(request):

    sights = Sight.objects.all()

    # shift
    AM_n = sights.filter(Shift='AM').count()
    PM_n = sights.filter(Shift='PM').count()
    AM_pct = AM_n/(AM_n + PM_n )
    AM_pct = "{:.2%}".format(AM_pct)
    PM_pct = PM_n/(AM_n + PM_n)
    PM_pct = "{:.2%}".format(PM_pct)
    # age
    Juvenile_n = sights.filter(Age='Juvenile').count()
    Adult_n = sights.filter(Age='Adult').count()
    Juvenile_pct = Juvenile_n / (Juvenile_n + Adult_n)
    Juvenile_pct = "{:.2%}".format(Juvenile_pct)
    Adult_pct = Adult_n / (Juvenile_n + Adult_n)
    Adult_pct = "{:.2%}".format(Adult_pct)
    # Primary_Fur_Color
    Black_n = sights.filter(Primary_Fur_Color='Black').count()
    Gray_n = sights.filter(Primary_Fur_Color='Gray').count()
    Cinnamon_n = sights.filter(Primary_Fur_Color='Cinnamon').count()
    Black_pct = Black_n / (Black_n+Gray_n+Cinnamon_n)
    Black_pct = "{:.2%}".format(Black_pct)
    Gray_pct = Gray_n / (Black_n+Gray_n+Cinnamon_n)
    Gray_pct = "{:.2%}".format(Gray_pct)
    Cinnamon_pct = Cinnamon_n / (Black_n+Gray_n+Cinnamon_n)
    Cinnamon_pct = "{:.2%}".format(Cinnamon_pct)
    # Location
    Above_Ground_n = sights.filter(Location='Above Ground').count()
    Ground_Plane_n = sights.filter(Location='Ground Plane').count()
    Above_Ground_pct = Above_Ground_n / (Above_Ground_n+Ground_Plane_n)
    Above_Ground_pct = "{:.2%}".format(Above_Ground_pct)
    Ground_Plane_pct = Ground_Plane_n / (Above_Ground_n+Ground_Plane_n)
    Ground_Plane_pct= "{:.2%}".format(Ground_Plane_pct)
    # Runs_From
    True_n = sights.filter(Runs_From=True).count()
    False_n = sights.filter(Runs_From=False).count()
    True_pct = True_n / (True_n+False_n)
    True_pct = "{:.2%}".format(True_pct)
    False_pct = False_n / (True_n+False_n)
    False_pct = "{:.2%}".format(False_pct)

    context = {
            'Total':sights.count(),
            'Shift': {'AM': AM_n,'PM': PM_n},
            'Shift_pct': {'AM': AM_pct,'PM': PM_pct},
            'Age': {'Juvenile': Juvenile_n, 'Adult': Adult_n},
            'Age_pct': {'Juvenile': Juvenile_pct, 'Adult': Adult_pct},
            'Primary_Fur_Color': {'Black':Black_n, 'Gray':Gray_n, 'Cinnamon':Cinnamon_n},
            'Primary_Fur_Color_pct': {'Black':Black_pct, 'Gray':Gray_pct, 'Cinnamon':Cinnamon_pct},
            'Location': {'Above_Ground':Above_Ground_n, 'Ground_Plane':Ground_Plane_n},
            'Location_pct': {'Above_Ground':Above_Ground_pct, 'Ground_Plane':Ground_Plane_pct},
            'Runs_From': {'True':True_n, 'False':False_n},
            'Runs_From_pct': {'True':True_pct, 'False':False_pct},
            }
    return render(request, 'sightings/stats.html', {'context':context})
