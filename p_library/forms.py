from django import forms  
from p_library.models import Author, Book, Friend, UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import formset_factory

class AuthorForm(forms.ModelForm):  

    full_name = forms.CharField(widget=forms.TextInput, label='Имя')  

    class Meta:  
        model = Author
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить Автора', css_class="btn-success"))
        


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить', css_class="btn-success"))

class BookForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput, label='Название')  

    class Meta:  
        model = Book  
        fields = ('title', 'authors', 'year_release', 'country', 'description', 'publisher', 'ISBN', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить книгу', css_class="btn-success"))
        
  
class UserProfileForm(forms.ModelForm):  
  
    class Meta:
        model = UserProfile
        fields = ('user', 'email')