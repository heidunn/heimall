import re

from django import http
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
# Create your views here.
from apps.users.models import User


class RegisterView(View):
    def get(self, request):

        return render(request, template_name='register.html')

    def post(self, request):
        print("hello")
        """
        业务逻辑：
            # 1, 验证必须传入的参数 all[el, el, el,]
            # 2, 判断用户名是否符合要求
            # 3, 判断密码是否符合要求
            # 4, 判断确认密码是否和密码相同
            # 5, 判断输入的手机号是否符合规范
        """
        # 0, 获取全部数据信息
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        password2 = data.get('password2')
        mobile = data.get('mobile')
        # 1, 验证必须传入的参数 all[el, el, el,]
        if not all([username, password, password2, mobile]):
            return http.HttpResponseBadRequest("参数不能为空"
                                               "")
        # 2, 判断用户名是否符合要求
        if not re.match(r'[0-9a-zA-z_]{5,20}', username):
            return http.HttpResponseBadRequest("用户名不合法")

        # 3, 判断密码是否符合要求
        if not re.match(r'[0-9a-zA-z_]{5,20}', password):
            return http.HttpResponseBadRequest("密码不合法")

        # 4, 判断确认密码是否和密码相同
        if password != password2:
            return http.HttpResponseBadRequest("输入的前后密码不同")

        # 5, 判断输入的手机号是否符合规范
        if not re.match(r'1[3-9]\d{9}', mobile):
            return http.HttpResponseBadRequest("手机号码不合法")

        # 当全部输入合法
        # 数据写入数据库
        try:
            user = User.objects.create_user(username=username, password=password, mobile=mobile)
            # return http.HttpResponse("注册成功")
        except Exception as e:
            return http.HttpResponseBadRequest('error')

        # 返回首页
        return redirect(reverse('contents:index'))


