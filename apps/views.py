from django.shortcuts import render
from .models import District, Region


def main_page(request):
    districts = District.objects.all()
    regions = Region.objects.all()
    context = {
        'districts': districts,
        'regions': regions

    }
    return render(request, 'apps/main.html', context)


def region_page(request, pk):
    districts = District.objects.filter(region_id=pk)
    context = {
        'districts': districts
    }
    return render(request, 'apps/region.html', context)
