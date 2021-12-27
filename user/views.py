# from django.shortcuts import render
# from django.views import View
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from .forms import SignupForm, LoginForm
#
#
# class Signup(View):
#     def get(self, request):
#         return render(request, 'signup.html', {SignupForm})
#
#     def post(self, request):
#         data = request.POST
#         user = SignupForm(data)
#
#         if user.is_valid():
#             user.save(commit=True)
#             return HttpResponse('OK')
#         else:
#             return HttpResponse('Failed')
#
#
# class Login(View):
#     def get(self, request):
#         return render(request, 'login.html', {})
#
#     def post(self, request):
#         data = request.POST
#         user = LoginForm(data)
#         if user.is_valid():
#             user = authenticate(request, username=user.data['username'], password=user.data['password'])
#             if user:
#                 login(request, user)
#                 return HttpResponse('OK')
#             else:
#                 return HttpResponse('Failed')
#         else:
#             return HttpResponse('Failed')