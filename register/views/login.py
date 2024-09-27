from library import BaseView
from django.shortcuts import render
from django.http import JsonResponse

class Login(BaseView):
    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        return JsonResponse("skuidguyshdb");
