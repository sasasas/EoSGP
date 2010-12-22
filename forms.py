from django import forms

ORG_TYPE_CHOICES = (
	('individual', 'No'),
	('church', 'Yes (my church)'),
	('other', 'Yes (other organisation)'),
)

NEWSLETTER_CHOICES = (
	('Y', 'Yes'),
	('N', 'No'),
)

class ContactForm(forms.Form):
	org_type = forms.ChoiceField(choices=ORG_TYPE_CHOICES, widget=forms.RadioSelect, label='Are you contacting EoSGP on behalf of your church or an organisation?')	
	name = forms.CharField(max_length=50)
	church_or_org = forms.CharField(max_length=100, label='Church or organisation (if applicable)', required=False)
	minister_or_head = forms.CharField(max_length=50, label='Minister/head of organisation (if applicable)', required=False)
	email = forms.EmailField()
	address = forms.CharField(max_length=200, widget=forms.Textarea)
	message = forms.CharField(required=False, widget=forms.Textarea)
	newsletter = forms.ChoiceField(choices=NEWSLETTER_CHOICES, widget=forms.RadioSelect, label='Would you like to receive our newsletter to the address you have given us?')

