from django.conf.urls import url
from bhptale import views


app_name="bhptale"

urlpatterns=[
    url(r'^homepage/$', views.homepage),
    url(r'^about/$', views.testimonial),

]