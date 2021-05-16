import pdb
from django.core.validators import EMPTY_VALUES
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views import View
from .services import *


class BaseView(View):

    def calculate(self, nums=[]):
        raise(NotImplementedError)

    def transform(self, data):
        nums = parse_data(data)
        if nums in EMPTY_VALUES:
            return HttpResponseBadRequest("Incorrect Data or Empty Data")
        return nums

    def get(self, request):
        data = request.GET
        nums = self.transform(data)
        return self.calculate(nums)


class AdditionView(BaseView):
    def calculate(self, nums):
        s = add(nums)
        return HttpResponse(s)


class SubtractionView(BaseView):
    def calculate(self, nums):
        sub = subtraction(nums)
        return HttpResponse(sub)

class MultiplicationView(BaseView):
    def calculate(self, nums):
        pro = product(nums)
        return HttpResponse(pro)

class DivideView(BaseView):
    def calculate(self, nums):
        div = division(nums)
        return HttpResponse(div)

class EvalExprView(View):
    def calculate(self, expr):
        try:
            val = eval(expr)
            return val
        except SyntaxError:
            return None

    def transform(self, data):
        str_response = ""
        ans_template = "{} = {}\n"
        for k, v in data.items():
            expr = v.replace(' ', '+')
            ans = self.calculate(expr)
            if ans in EMPTY_VALUES:
                return HttpResponseBadRequest("Expression is wrong `{} = {}`".format(k, v))
            str_response += ans_template.format(k, ans)
        return str_response

    def get(self, request):
        data = request.GET
        return HttpResponse(self.transform(data))
