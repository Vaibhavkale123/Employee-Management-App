from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp



# Create your views here.
def emp_home(request):
    # return HttpResponse("Employee    home page  ")
    emps = Emp.objects.all()
    return render(request, "home.html", {"emps":emps})


def add_emp(request):
    # validation

    if request.method == "POST":
        print("Data is coming")
        # Data fetcch
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        # creeaate  model data  object
        e = Emp()
        e.emp_id = emp_id

        e.name = emp_name
        e.phone = emp_phone
        e.address = emp_address
        e.working = emp_working
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        print("name", e.name)

        e.save()

        return redirect("/emp/home")

        # save data data object

    return render(request, "add_emp.html", {})


def delete_emp(request, emp_id):
    print(emp_id)
    e = Emp.objects.get(emp_id=emp_id)
    e.delete()
    print("deleted", e.name)
    # emp.objects.filter(address="Hyderabad").delete()
    # print("Deleted")
    return redirect("/emp/home")


def update_emp(request, emp_id):
    print(emp_id)
    e = Emp.objects.get(emp_id=emp_id)

    print("updating", e.name)
    # emp.objects.filter(working=True).delete()
    # print("Deleted")
    return render(request, "update_emp.html", {"emp": e})
    # return render(request,"emp/home.html",{"emps":emps})


def do_update(request):
    print("inside do update method")
    if request.method == "POST":
        print("Data is coming")
        # Data fetcch
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        print("emp name from view", emp_name)

        print("emp id from view", emp_id)
        # creeaate  model data  object
        # e=emp()
        e = Emp.objects.get(emp_id=emp_id)

        # e.emp_id=emp_id

        e.name = emp_name
        e.phone = emp_phone
        e.address = emp_address
        e.working = emp_working
        e.department = emp_department
        print("employee working=", emp_working)
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        # e.working= emp_working
        e.save()
        print("name and id updated", e.name, " and ", e.id)

        return redirect("/emp/home")

        # save data data object

    # return render(request,"emp/add_emp.html",{})


