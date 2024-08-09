from django.shortcuts import render
from .forms import StudentForm
from .models import StudentModel

def home(request):
    data = StudentModel.objects.all()
    return render(request, "home.html", {"data":data})

def create(request):
    if request.method == "POST":
        data = StudentForm(request.POST)
        if data.is_valid():
            data.save()
            msg = "Record created"
            fm = StudentForm()
            return render(request, "create.html", {"fm":fm, "msg":msg})
        else:
            msg = "Check errors"
            return render(request, "create.html", {"fm":data, "msg":msg})
    else:
        fm = StudentForm()
        return render(request, "create.html", {"fm":fm})
