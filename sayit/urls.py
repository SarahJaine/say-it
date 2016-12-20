from django.conf.urls import include, url
from django.contrib import admin

from sayit.views import HomeView, HowView, MusiciansView, OrderView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^how-it-works/$', HowView.as_view(), name='how'),
    url(r'^musicians/$', MusiciansView.as_view(), name='musicians'),
    url(r'^order/$', OrderView.as_view(), name='order'),
    url(r'^admin/', include(admin.site.urls)),
]
