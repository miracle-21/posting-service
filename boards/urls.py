from django.urls import path

from boards.views import *

urlpatterns = [
    path('/post', CreateView.as_view()),
    path('/delete/<int:id>', DeleteView.as_view()),
    path('/update/<int:id>', UpdateView.as_view()),
    path('', GetView.as_view()),
]
