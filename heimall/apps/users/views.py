from django.shortcuts import render
from django.views import View
# Create your views here.


class RegisterView(View):
    def get(self, request):
        return render(request, template_name='register.html')

    def post(self, request):
        pass

    pass

