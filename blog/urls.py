from django.contrib import admin
from django.urls import path, include
from article import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),  #anasayfaya gittiğimde bu fonksiyon çalışacak.  
    path('about/', views.about, name="about"),   
    #path('detail/<int:id>', views.detail, name="detail"),  
    path('articles/', include("article.urls")),  # include'dan sonraki kısım => article'daki urls dosyasına bak.
    path('user/', include("user.urls")), # burada da user'la başlayan url'lerin başka bir url dosyasından gelmesini istiyoruz.
    # son ikisi dinamik url gibi. başında articles veya user olunca ilgili urls.py dosyasına bakıyor.

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
