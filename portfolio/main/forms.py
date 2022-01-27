from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):
    # form input fields for the frontend 
	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': 'Full name...',
            # comment if not using form control in templates
			'class': 'form-control'
		}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': 'Email...',
			'class': 'form-control'
		}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': 'Message...',
			'class': 'form-control',
            # update this if template changes
			'rows': 6,
		}))

	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)