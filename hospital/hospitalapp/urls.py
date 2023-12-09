from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home,name='homepage'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('signup/',views.signup,name='signup'),
    path('upload/',views.upload,name='upload')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)