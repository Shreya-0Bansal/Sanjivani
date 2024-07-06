from django.urls import path
from . import views
app_name="home"
urlpatterns = [
    path('captcha', views.CaptchaChallengeView.as_view(), name='captcha-challenge'),
    path('index',views.index,name="index"),
    path('check',views.check,name="check"),
    path('join',views.join,name="join"),
    path('events',views.events,name="events"),
    path('faq',views.faq,name="faq"),
    path('contact',views.contact,name="contact"),
    path('donor/', views.donor, name="donor"),
    path('organ/',views.organ,name="organ"),
    path('looking/',views.looking,name="looking"),
    path('display-donor/<str:donor_id>/',views.display_donor,name='display_donor'),
    path('get_cities/', views.get_cities, name='get_cities'),
]
