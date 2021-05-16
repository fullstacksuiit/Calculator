from django.urls import path

from .views import (
    AdditionView,
    EvalExprView,
    SubtractionView,
    MultiplicationView,
    DivideView,
)

urlpatterns = [
    path("addition", AdditionView.as_view()),
    path("subtraction", SubtractionView.as_view()),
    path("multiplication", MultiplicationView.as_view()),
    path("division", DivideView.as_view()),
    path("evaluate", EvalExprView.as_view()),
]
