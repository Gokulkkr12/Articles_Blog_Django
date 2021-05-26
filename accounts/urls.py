from django.conf.urls import url
from . import views
app_name='accounts'
urlpatterns =[
    url(r'^signup/$',views.signup_details, name='signup'),
    url(r'^login/$',views.login_details, name='login'),
    url(r'^logout/$',views.logout_details, name='Logout'),

]