from django.shortcuts import render
from .models import PollingUnit, Lga, Ward
from django.core.paginator import Paginator
from django.db import connection

# Create your views here.


def index(request):
    pu = PollingUnit.objects.all()
    paginator = Paginator(pu, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'polling_units': page_obj,
    }
    # def dictfetchall(cursor):
    #     columns = [col[0] for col in cursor.description]
    #     return [
    #         dict(zip(columns, row))
    #         for row in cursor.fetchall()
    #     ]
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM bincom_test.polling_unit LIMIT 0, 5")
    #     # rows = cursor.fetchall()
    #     rows = dictfetchall(cursor)
    #     context = rows[0]
        # return rows
    return render(request, 'core/all-polling-unit.html', context)


def each_pu(request, id):
    pu = PollingUnit.objects.get(uniqueid=id)
    lga = Lga.objects.get(lga_id=pu.lga_id)
    ward = Ward.objects.get(uniqueid = pu.ward_id)
    context = {
        'pu':pu,
        'lga':lga,
        'ward':ward
    }
    return render(request, 'core/each-pu.html', context)

def lga(request):
    lga = Lga.objects.all()
    pu_list = []
    print(dir(lga))
    # for lg in lga:
    #     pu = PollingUnit.objects.filter(lga_id=lg.lga_id)
    context = {
        'lga':lga,
    }
    print(pu_list)
    return render(request, 'core/all-lga.html', context)


def each_lga(request, id):
    lga = Lga.objects.get(lga_id=id)
    pu = PollingUnit.objects.filter(lga_id=id)
    context = {
        'pu':pu.count(),
        'lga':lga
    }
    return render(request, 'core/each-lga.html', context)

