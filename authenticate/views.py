from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from home import urls
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from home.models import Profile

# Create your views here.
@csrf_exempt
def loginPage(request):
    if request.method == 'POST':
        print('login')
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            print("credentials are incorrect.")
            return redirect("signupPage")
        # print(username,password)
    print('lol')
    return render(request, 'loginPage.html')
    

def logoutPage(request):
    print("logout")
    logout(request)
    return redirect("home")

@csrf_exempt
def signupPage(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        user = request.POST['username']
        age = request.POST['age']
        email = request.POST['email']
        password1 = request.POST['password']
        confirmpass = request.POST['confirmpass']

        if password1 == confirmpass:
            if not User.objects.filter(username=user).exists():
                if not User.objects.filter(email=email).exists():
                    user=User.objects.create_user(username = user, email = email, password=password1)
                    user.save()
                    user_model = User.objects.get(username= user)
                    customer = Profile(user = user_model, username=user, email= email, age=age)
                    customer.save()
                    print("New User Created")
                    login(request, user)
        return redirect('home')
    return render(request, "signupPage.html")


    