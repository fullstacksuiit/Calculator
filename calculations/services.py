from django.core.validators import EMPTY_VALUES


def add(nums):
    return sum(nums)

def subtraction(nums):
    sub = nums[0]
    for num in nums[1:]:
        sub = sub - num
    return sub

def product(nums):
    pro = 1
    for num in nums:
        pro = pro*num
    return pro

def division(nums):
    div = nums[0]
    for num in nums[1:]:
        div = div/num
    return div


def parse_data(data):
    nums = []
    if isinstance(data, dict) and data not in EMPTY_VALUES:
        try:
            nums = [float(num) for num in data.values()]
        except ValueError:
            return []
    return nums