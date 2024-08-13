from django.utils.translation import gettext as _
from django_registration.forms import RegistrationForm
from jarrbo_theme.forms import JarrboFormHelper
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from crispy_forms.layout import Submit

User = get_user_model()

class JarrboRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = get_user_model()
        fields = [
            User.USERNAME_FIELD,
#            User.get_email_field_name(),
			"first_name",
			"last_name",
            "password1",
            "password2",
        ]
        
    def __init__(self, *args, **kwargs):
        super(JarrboRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = JarrboFormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('register', _('Create account')))
        
class JarrboPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(JarrboPasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = JarrboFormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('reset', _('Reset password')))
        
class JarrboSetPasswordForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super(JarrboSetPasswordForm, self).__init__(user, *args, **kwargs)
        self.helper = JarrboFormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('reset', _('Reset password')))

class JarrboPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(JarrboPasswordChangeForm, self).__init__(user, *args, **kwargs)
        self.helper = JarrboFormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('change', _('Change password')))
        
class JarrboAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(JarrboAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = JarrboFormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('login', _('Login')))



