from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User
# Create your views here.


# this function will show and add items
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)

        # if fm.is_valid():             Sort method
        #     fm.save()

        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']

        UserObj=User(name=nm, email=em, password=ps)
        UserObj.save()
        return redirect('addandshow')
        # fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})


# This function will Update/Edit
def update_data(request,id):
    # for update, when method is post
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('addandshow')
    
    # for rendering the page, when method is get
    pi=User.objects.get(pk=id)
    fm=StudentRegistration(instance=pi)
    context={
        'form':fm,
    }
    return render(request, 'enroll/updateStudent.html', context)




#this function will delete items
def delete(request, id):
    # if request.method=='POST':
    pi=User.objects.get(pk=id)
    pi.delete()
    return redirect('addandshow')
    # fm=StudentRegistration()
    # stud=User.objects.all()
    # return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})
    # return render(request, 'enroll/addandshow.html')