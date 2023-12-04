from django.forms import ModelForm, CharField, TextInput, DateField
from .models import Tag, Note ,Author_note


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['nametag']

class NoteForm(ModelForm):

   # name = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=500, required=True, widget=TextInput())

    class Meta:
        model = Note
        fields = ['description']
        exclude = ['tags', 'authors']

class AuthorForm(ModelForm):
    fullname = CharField(min_length=10, max_length=250, required=True, widget=TextInput())
    born_date = CharField(min_length=10, max_length=250, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=500, required=True, widget=TextInput())

    class Meta:
        model = Author_note
        fields = ['fullname', 'born_date', 'born_location', 'description']
