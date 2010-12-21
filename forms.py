from django import forms

NEWSLETTER_CHOICES = (
	('Y', 'Yes'),
	('N', 'No'),
)

class ContactForm(forms.Form):
	name = forms.CharField(max_length=50)
	name_of_minister = forms.CharField(max_length=50)
	church = forms.CharField(max_length=100)
	email = forms.EmailField()
	address = forms.CharField(max_length=200)
	message = forms.CharField(required=False, widget=forms.Textarea)
	newsletter = forms.ChoiceField(choices=NEWSLETTER_CHOICES, widget=forms.RadioSelect)

