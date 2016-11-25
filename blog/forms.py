from django import forms
from .models import Post, Comment, Blogger, Category

# Additional imports for users:
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        image = forms.ImageField()
        fields = ('title', 'text', 'image')

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Blogger
        fields = ('profile_pic', 'bio', 'city', 'country',)

class CommentForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': ('Your thoughts'),
        }

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('text',)
        labels = {
            'text': ('Add a category'),
        }
