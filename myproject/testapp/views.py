from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def my_login(request):

    if request.method == 'POST':
        tuser = request.POST.get('username')
        tpass = request.POST.get('password')

        if tuser != "" and tpass != "":
            user = authenticate(username=tuser, password=tpass)

            if user != None:
                login(request, user)
                return redirect('testpage')

    return render(request, 'login.html')


def testpage(request):
    if not request.user.is_authenticated:
        return redirect('testlogin')

    return render(request, 'testpage.html')


def my_logout(request):

    logout(request)

    return redirect('testlogin')
