from django.urls import re_path

from .views import *
from django.views.generic.base import TemplateView

app_name = 'jarrbo_auth'
urlpatterns = [
    re_path(r'^profile/$', JarrboProfileView, name='profile'),
    re_path(r'^login/$', JarrboLoginView.as_view(), name='login'),
    re_path(r'^logout/$', JarrboLogoutView.as_view(), name='logout'),
    re_path(r'^register/$', JarrboRegistrationView.as_view(), name='register'),
    re_path(r'^register/complete/$', JarrboRegistrationCompleteView.as_view(), name='registration_complete'),
    # to avoid name clash the registration_activation_complete url must be mentioned before registration_activate
    re_path(r'^activate/complete/$', JarrboActivationCompleteView.as_view(),
        name='registration_activation_complete'),
    re_path(r'^activate/(?P<activation_key>[-:\w]+)/$', JarrboActivationView.as_view(),
        name='registration_activate'),
    re_path(r'^password/reset/$', JarrboPasswordResetView.as_view(), name='password_reset'),
    re_path(r'^password/reset/done/$', JarrboPasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,50})/$',
        JarrboPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^password/reset/complete/$', JarrboPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    re_path(r'^password/change/$', JarrboPasswordChangeView.as_view(), name='password_change'),
    re_path(r'^password/change/done/$', JarrboPasswordChangeDoneView.as_view(), name='password_change_done'),
]
