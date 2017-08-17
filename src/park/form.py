from django import forms

from . models import Post_form


class PostForm(forms.ModelForm):
	class Meta:
		model=Post_form
		fields=[
		"Number",
		"Slot"

		  ]
