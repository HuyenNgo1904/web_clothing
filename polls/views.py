from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

### Trang chủ admin -
def home(request):
    return render(request, 'polls/admin/index.html')


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse("polls:home"))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="polls/admin/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    return render(request, 'polls/admin/login.html', messages.error(request, "You have successfully logged out."))


def get_profile(request):
    return render(request, 'polls/admin/profile.html')