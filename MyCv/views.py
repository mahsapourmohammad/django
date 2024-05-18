from django.shortcuts import render,HttpResponse
from .models import Profile
# Create your views here.
def index(request):
    students= Profile.objects.all()
    context={
        'students': students
    }
    return render(request, 'MyCv/index.html',context)