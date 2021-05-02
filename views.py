from .forms import (JarrboRegistrationForm, JarrboPasswordResetForm, JarrboSetPasswordForm, JarrboPasswordChangeForm, JarrboAuthenticationForm)
from django_registration.backends.activation.views import RegistrationView, ActivationView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView, LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy

class JarrboRegistrationView(RegistrationView):
	template_name = 'jarrbo_auth/registration.html'
	email_body_template = 'jarrbo_auth/activation_email.txt'
	email_subject_template = 'jarrbo_auth/activation_email_subject.txt'
	success_url = reverse_lazy("jarrbo_auth:registration_complete")
	form_class = JarrboRegistrationForm
    
class JarrboActivationView(ActivationView):
	template_name = 'jarrbo_auth/activate.html'
	success_url = reverse_lazy("jarrbo_auth:registration_activation_complete")

class JarrboRegistrationCompleteView(TemplateView):
	template_name='jarrbo_auth/registration_complete.html'

class JarrboActivationCompleteView(TemplateView):
	template_name='jarrbo_auth/activation_complete.html'

class JarrboPasswordResetView(PasswordResetView):
	template_name='jarrbo_auth/password_reset_form.html'
	email_template_name = 'jarrbo_auth/password_reset_email.txt'
	subject_template_name = 'jarrbo_auth/password_reset_subject.txt'
	from_email = 'noreply@jarrbo.nl'
	success_url = reverse_lazy('jarrbo_auth:password_reset_done')
	form_class = JarrboPasswordResetForm

class JarrboPasswordResetDoneView(PasswordResetDoneView):
	template_name = 'jarrbo_auth/password_reset_done.html'

class JarrboPasswordResetConfirmView(PasswordResetConfirmView):
	template_name = 'jarrbo_auth/password_reset_confirm.html'
	form_class = JarrboSetPasswordForm
	success_url = reverse_lazy('jarrbo_auth:password_reset_complete')

class JarrboPasswordResetCompleteView(PasswordResetCompleteView):
	template_name = 'jarrbo_auth/password_reset_complete.html'

class JarrboPasswordChangeView(PasswordChangeView):
	template_name = 'jarrbo_auth/password_change_form.html'
	success_url = reverse_lazy('jarrbo_auth:password_change_done')
	form_class = JarrboPasswordChangeForm
    
class JarrboPasswordChangeDoneView(PasswordChangeDoneView):
	template_name = 'jarrbo_auth/password_change_done.html'

class JarrboLoginView(LoginView):
	authentication_form = JarrboAuthenticationForm
	template_name = 'jarrbo_auth/login.html'

class JarrboLogoutView(LogoutView):
	template_name = 'jarrbo_auth/logout.html'
	
def JarrboProfileView(request):
	if request.user.is_authenticated:
		return render(request, 'jarrbo_auth/profile.html',)
	else:
		view = JarrboLoginView.as_view()
		return view(request)

    
