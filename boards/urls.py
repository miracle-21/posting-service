from django.urls import path

from boards.views import *

urlpatterns = [
    path('', CreateView.as_view()),
    path('/delete/<int:id>', DeleteView.as_view()),
    path('/update/<int:id>', UpdateView.as_view()),
]
