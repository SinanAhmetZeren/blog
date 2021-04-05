from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # form ile modeli bağlantılı hale getirmiş oluyoruz, django alanları ona göre oluşturuyor.
        fields = ["title", "content","article_image"]

