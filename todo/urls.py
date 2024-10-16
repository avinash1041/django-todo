from django.urls import path
from . import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('add/',views.AddView.as_view()),
    path('about/',views.AboutView.as_view()),
    path('redirect/',views.RedirectAbout.as_view()),
    path('todo/<int:pk>/',views.DetailView.as_view(),name='todo'),
    path('update/<int:pk>/',views.UpdateTodoView.as_view(),name='up'),
    path('delete/<int:pk>/',views.DeleteTodoView.as_view(),name='delete')
]
