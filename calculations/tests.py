from django.test import TestCase
from .services import *


class TestAddition(TestCase):
    nums = [10, 20]

    def test_addition_service(self):
        self.assertEqual(add(self.nums), 30)

    def test_addition_view(self):
        url = "/calculate/addition"
        response = self.client.get(url, data={"a": self.nums[0], "b": self.nums[1]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.content), 30)


class TestSubtraction(TestCase):
    nums = [20, 10]

    def test_subtraction_service(self):
        self.assertEqual(subtraction(self.nums), 10)

    def test_subtraction_view(self):
        url = "/calculate/subtraction"
        response = self.client.get(url, data={"a": self.nums[0], "b": self.nums[1]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.content), 10)


class TestMultiplication(TestCase):
    nums = [10, 20]

    def test_multiplication_service(self):
        self.assertEqual(product(self.nums), 200)

    def test_multiplication_view(self):
        url = "/calculate/multiplication"
        response = self.client.get(url, data={"a": self.nums[0], "b": self.nums[1]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.content), 200)


class TestDivide(TestCase):
    nums = [20, 10]

    def test_divide_service(self):
        self.assertEqual(division(self.nums), 2)

    def test_divide_view(self):
        url = "/calculate/divide"
        response = self.client.get(url, data={"a": self.nums[0], "b": self.nums[1]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.content), 2)


class TestEvalExpr(TestCase):

    def test_eval_view(self):
        url = "/calculate/evaluate"
        response = self.client.get(url, data={"a": "6-7*2"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'a = -8\n')
