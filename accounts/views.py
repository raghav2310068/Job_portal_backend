from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .forms import UserForm
from .models import Users
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Users
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class IndexView(View):
    def get(self, request):
        return render(request, "accounts/login.html", {"error": None})

    def post(self, request):
        action = request.POST.get("action")

        if action == "login":
            email = request.POST.get("email")
            password = request.POST.get("password")

            # 🔥 validation
            if not email or not password:
                return render(
                    request,
                    "accounts/login.html",
                    {"error": "Email and password are required"},
                )

            try:
                user = Users.objects.get(email=email)

                if user.password == password:
                    request.session["user_id"] = user.id  # 🔥 yaha add kar
                    return redirect("/api/jobs/")
                else:
                    return render(
                        request,
                        "accounts/login.html",
                        {"error": "Wrong password"},
                    )

            except Users.DoesNotExist:
                messages.error(
                    request, "You are not registered. Please register first."
                )

                return redirect("register")

        elif action == "register":
            return redirect("register")

        return render(request, "accounts/login.html")


class RegisterView(View):
    def get(self, request):
        user_registration_form = UserForm()
        return render(
            request,
            "accounts/register_user.html",
            context={
                "user_registration_form": user_registration_form,
            },
        )

    def post(self, request):
        user_registration_form = UserForm(request.POST)
        if user_registration_form.is_valid():
            user_registration_form.save()
            return redirect("login")
        return redirect("/")
