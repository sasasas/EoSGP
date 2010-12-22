from django import forms

ORG_TYPE_CHOICES = (
	('individual', 'An Individual?'),
	('church', 'A Church?'),
	('other', 'An Organisation?'),
)

NEWSLETTER_CHOICES = (
	('Y', 'Yes'),
	('N', 'No'),
)

class ContactForm(forms.Form):
	org_type = forms.ChoiceField(choices=ORG_TYPE_CHOICES, widget=forms.RadioSelect, label='Are you contacting EoSGP as')	
	name = forms.CharField(max_length=50)
	church_or_org = forms.CharField(max_length=100, label='Church/Organization', required=False)
	minister_or_head = forms.CharField(max_length=50, label='Minister/Head of Organisation', required=False)
	email = forms.EmailField()
	address = forms.CharField(max_length=200, widget=forms.Textarea)
	message = forms.CharField(widget=forms.Textarea, label='Message', required=False)
	newsletter = forms.ChoiceField(choices=NEWSLETTER_CHOICES, widget=forms.RadioSelect, label='Would you like to receive our newsletter to the address supplied?')

