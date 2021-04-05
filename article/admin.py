from django.contrib import admin

from .models import Article, Comment  #aynı folder'daki models dosyasından Article'ı al

# Register your models here.

#  admin.site.register(Article)  #admin panelinde göstericez 
# bunu decorator olarak yazıyoruz:
 
admin.site.register(Comment)



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title","content"]
    list_filter = ["created_date", "author"]

    class Meta:
        model = Article