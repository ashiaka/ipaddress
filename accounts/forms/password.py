from django import forms
from accounts.models import User

class PasswordForm(forms.ModelForm):
    """
    Form for changing the password.
    """
    password_old = forms.CharField(label="Old password")
    password1 = forms.CharField(label="New password")
    password2 = forms.CharField(label="New password (again)")

    class Meta:
        model = User
        fields = ['password_old', 'password1', 'password2']

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(PasswordForm, self).clean()
        if 'password_old' in self.cleaned_data and \
                        'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data