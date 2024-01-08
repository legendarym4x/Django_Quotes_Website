from django.forms import ModelForm, CharField, DateField, TextInput, DateInput, Textarea, ModelChoiceField, \
    ModelMultipleChoiceField, SelectMultiple, Select
from .models import Author, Quote, Tag


class AuthorForm(ModelForm):
    fullname = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control"}))
    born_date = DateField(widget=DateInput(attrs={"class": "form-control", "placeholder": "MM/DD/YYYY"}))
    born_location = CharField(max_length=200, widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(widget=Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = ('fullname', 'born_date', 'born_location', 'description')


class QuoteForm(ModelForm):
    quote = CharField(widget=Textarea(attrs={"class": "form-control"}))
    author = ModelChoiceField(Author.objects.all(), widget=Select(attrs={"class": "form-select"}))
    tags = ModelMultipleChoiceField(Tag.objects.all(), widget=SelectMultiple(attrs={"class": "form-select"}),
                                    required=False)

    class Meta:
        model = Quote
        fields = ('quote', 'author', 'tags')
