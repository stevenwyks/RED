from django.urls import include,  path
from home.views import HomeNotAuthView, HomeView, StepOneView, AboutUsNotAuthView, AboutUsView

app_name = 'home'
urlpatterns = [
    path('not-auth/', HomeNotAuthView.as_view(), name = 'home_notauth'),
    path('', HomeView.as_view(), name = 'home' ), #login
    path('form/', StepOneView.as_view(), name = 'form'),
    path('about-us-notauth/', AboutUsNotAuthView.as_view(), name='about_us_notauth'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
]