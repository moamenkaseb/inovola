from django.shortcuts import render , redirect , HttpResponse
from .models import machine , machine_code ,pods , pods_code
# Create your views here.

# machine page
def machine_page(request):
    machines = machine.objects.all()
    code = machine_code.objects.all()

    return render(request , 'pages/page1.html' , {
        'machines':machines,
        'code':code
    })


# pods page
def pods_page(request):
    podss = pods.objects.all()
    code = pods_code.objects.all()
    return render(request , 'pages/page2.html' ,{
        'podss':podss,
        'code':code
    })

