from django.conf.urls import url

from .views import *
from django.views.generic.base import TemplateView

app_name = 'jarrbo_auth'
urlpatterns = [
    url(r'^profile/$', JarrboProfileView, name='profile'),
    url(r'^login/$', JarrboLoginView.as_view(), name='login'),
    url(r'^logout/$', JarrboLogoutView.as_view(), name='logout'),
    url(r'^register/$', JarrboRegistrationView.as_view(), name='register'),
    url(r'^register/complete/$', JarrboRegistrationCompleteView.as_view(), name='registration_complete'),
    # to avoid name clash the registration_activation_complete url must be mentioned before registration_activate
    url(r'^activate/complete/$', JarrboActivationCompleteView.as_view(),
        name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>[-:\w]+)/$', JarrboActivationView.as_view(),
        name='registration_activate'),
    url(r'^password/reset/$', JarrboPasswordResetView.as_view(), name='password_reset'),
    url(r'^password/reset/done/$', JarrboPasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,50})/$',
        JarrboPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password/reset/complete/$', JarrboPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^password/change/$', JarrboPasswordChangeView.as_view(), name='password_change'),
    url(r'^password/change/done/$', JarrboPasswordChangeDoneView.as_view(), name='password_change_done'),
]
