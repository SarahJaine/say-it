from django import forms


class UnstyledForm(forms.Form):
	def __init__(self, *args, **kwargs):
		kwargs.setdefault('label_suffix', '')
		super(UnstyledForm, self).__init__(*args, **kwargs)


class OrderForm(UnstyledForm):
	PRODUCT_CHOICES = [
		(2, 'Song and Slideshow'),
		(1, 'Song only')
	]
	LANG_CHOICES = [
		('E', 'English'),
		('F', 'French'),
		('S', 'Spanish')
	]
	STYLE_CHOICES = [
		('U', 'Upbeat pop'),
		('B', 'Slow ballad'),
		('O', 'Other')
	]
	name = forms.CharField(max_length=50,
		widget=forms.TextInput(
			attrs={'placeholder': 'Jane Doe'}))
	email = forms.EmailField(
		widget=forms.TextInput(
			attrs={'placeholder': 'jdoe@example.com'}))
	phone = forms.CharField(max_length=17,
		widget=forms.TextInput(
			attrs={'placeholder': '(555) 555-5555'}))
	product = forms.ChoiceField(choices=PRODUCT_CHOICES)
	language = forms.ChoiceField(choices=LANG_CHOICES)
	occasion = forms.CharField(max_length=50,
		widget=forms.TextInput(
			attrs={'placeholder': 'Birthday'}))
	date = forms.DateField(label='Date of Occasion',
		input_formats='%m/%d/%Y',
		widget=forms.DateInput(
			attrs={'placeholder': '10/29/2017'}))
	recipient = forms.CharField(label="Recipient's Name", max_length=50,
		widget=forms.TextInput(
			attrs={'placeholder': 'Jamal Doe'}))
	relationship = forms.CharField(label="Relationship to Recipient",
		max_length=50,
		widget=forms.TextInput(
			attrs={'placeholder': 'Best Friend'}))
	style = forms.ChoiceField(choices=STYLE_CHOICES)
	message = forms.CharField(label='Any Additional Info', max_length=5000,
		widget=forms.Textarea(
			attrs={'placeholder':
				'I would love for us to be able to dance to this song!'}))