from django.conf.urls import include, url
from django.contrib import admin

from sayit.views import HomeView, HowView, MusiciansView, OrderView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^$', AboutView.as_view(), name='about'),
    url(r'^$', MusiciansView.as_view(), name='musicians'),
    url(r'^$', OrderView.as_view(), name='order'),
    url(r'^admin/', include(admin.site.urls)),
]
