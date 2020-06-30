from django.contrib import admin
from .models import Article
from ckeditor.fields import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class PostAdminForm(forms.ModelForm):

    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = ('title', 'image', 'body', 'author')


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Article, PostAdmin)
