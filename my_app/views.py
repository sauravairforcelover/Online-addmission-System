from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import FormData

def webpage1(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            messages.info(request, 'User with this email already exists. Please log in.')
            return redirect('webpage2')
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        messages.success(request, 'Signup successful. You can now log in.')
        return redirect('webpage2')
    return render(request, 'signup.html')

def webpage2(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if FormData.objects.filter(user=user).exists():
                return redirect('receiving')
            else:
                return redirect('webpage3')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('webpage2')
    return render(request, 'login.html')

def webpage3(request):
    if request.method == 'POST':
        form_data = FormData(
            user=request.user,
            student_name=request.POST['student-name'],
            father_name=request.POST['father-name'],
            mother_name=request.POST['mother-name'],
            dob=request.POST['dob'],
            gender=request.POST['gender'],
            address=request.POST['address'],
            religion=request.POST['religion'],
            nationality=request.POST['nationality'],
            phone=request.POST['phone'],
            eid=request.POST['eid'],
            blood_group=request.POST['blood-group'],
            marital_status=request.POST['marital-status'],
            course=request.POST['course']
        )
        form_data.save()
        return redirect('receiving')
    return render(request, 'form.html')

def receiving(request):
    try:
        form_data = FormData.objects.get(user=request.user)
    except FormData.DoesNotExist:
        return redirect('webpage3')
    context = {
        'form_data': form_data
    }
    return render(request, 'receiving.html', context)
