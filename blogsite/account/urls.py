from.views import Signup,Signin,SignOut
from django.urls import path

urlpatterns = [
    
    path('reg/',Signup.as_view(),name='reg'),
    path('log/',Signin.as_view(),name='log'),
    path('logout/',SignOut.as_view(),name='logout')
]