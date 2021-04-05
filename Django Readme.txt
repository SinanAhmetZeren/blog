1. pip install Django==3.1.7

2. dir C:\Users\HP\OneDrive\Desktop
	-> django-admin startproject blog

3. Visual Studio Code'da:   python manage.py runserver
	-> server çalıştırılıyor.  localhost:8000 açılıyor, django 8000 ile çalışıyor.
	-> Sayfayı devreye alacağımız zaman:  setting.py'de "DEBUG = TRUE" yerine FALSE olarak değiştirmemiz gerekiyor.

4. Visual Studio Code'da:    python manage.py migrate  - tabloları database'te oluşturuyor.

5. VSC: python manage.py createsuperuser
	(Florestan, sinanahmetzeren@gmail.com  L*****1***

6. python manage.py startapp article (article -> uygulamanın adı)

7. a: models.py'nin içinde:
	class Article(models.Model):  (--> class tanımla)

   b: migrations'un içinde admin.py:
	from .models import Article  #aynı folder'daki models dosyasından Article'ı al
	admin.site.register(Article)  #admin panelinde göstericez 

   c:  settings.py'nin içine:  installed apps:  "article"  

   d: her bir model oluşturduğumda make migrations yapıcaz. 
	-> VSC'de:  python manage.py makemigrations  
	-> python manage.py migrate  (migrations dosyasına göre tablomuzu oluşturuyor.)

8. VSC terminal:  python manage.py shell  [[Terminalden user ve article oluşturma yöntemleri ]]
	-> from django.contrib.auth.models import User
	-> from article.models import Article
	-> newUser = User(username= "deneme kullanıcı", password ="123")
		newUSer.save()  #yeni bir kullanıcı yaratıp save ettik.
	-> newUser2 = User(username = "deneme2")
		newUser2.set_password("123")  # şifreyi şifreleyerek kaydetmek için.
		newUser2.save()
	-> article = Article(title="hello title", content="content1", author= newUser2)
		article.save()
	-> article = Article.objects.create(title="deneme3322", content = "22", author = newUser)
		article.save()
	-> Article.objects.all()  #hepsini seçmek için
	-> Article.objects.get(title="naber2")
	-> article = Article.objects.get(title="hello title")
	-> article.delete()
	-> Article.objects.filter(title__contains = "22")  #iki alt çizgi ile aradık...

9. settings.py -> TEMPLATES -> DIRS: ["templates"]
	belli bir template arandığında templates klasörüne bakacak.  (projenin altında bu klasörü oluşturduk)

	views.py 'nin içine:  
		from django.shortcuts import render, HttpResponse (ekledik)
		def index(reqest):
    			return HttpResponse("<h3> Main Page <h3>")   #request'e karşılık gelen response'ı yazdık.
		veya:	return render(request, "article/index.html")	#index.html'i render edip getirdik.
	urls.py 'nin içine: 
		from article.views import index	
		path('', index, name="index"),  #anasayfaya gittiğimde bu fonksiyon çalışacak.  

10. Static files:  https://docs.djangoproject.com/en/3.1/howto/static-files/  ( kontrol amaçlı... )
	Projenin altında (article'ın), static diye bir folder oluşturduk.  
	Altında style.css dosyası oluşturduk.
	(Index.html'de yazdık:     <link rel="stylesheet" href="../static/style.css"> )
	
	veya 
	
	aşağıdaki daha iyi: 
	{% load static %}  --> index.html'de <!DOCTYPE... satırının altına yapıştırdık.
	örnek: <img src="{% static 'my_app/example.jpg' %}">
	biz nasıl kullandık:     <link rel="stylesheet" href="{% static 'css/style.css' %}">
	static'in yerini belirttik, ona göre relatif pozisyon söylüyoruz.

	veya
	settings.py'nin altına:
		STATICFILES_DIRS = [
    		BASE_DIR / "static",
		]


11. python manage.py startapp user  -> projenin içinde, user adında yeni bir uygulama başlatıldı

12. pip install django-crispy-forms
	settings.py -> installed apps'e ekle.
	aynı dosyanın en sonuna : CRISPY_TEMPLATE_PACK = 'bootstrap4'
	(static file dirs'in altına)


13. Article form oluşturma
	-> https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/ 

14.a. Bootstrap 4 alpha 6 indirme
	static'in altında 2 dosya oluşturduk: css ve js
	bootstrap.min.css'i css folder'ının altına ekledik
	bootstrap.min.js'yi de js folder'ının altına ekledik.

		-> layout'un en başına {% load static %} dedik
		-> sonra:     <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
		-> bootstrap ile ilgili olan tepedeki 1 ve aşağıdaki 3 satırı da sildik. 
			not: tepedekini silince navbar patladığı için yeniden koydum.

   b. Jquery indirme
	js folder'ının altına jquery-3.6.0.min.js
	buradan yapıştır içeriğini- >https://code.jquery.com/jquery-3.6.0.min.js  

    		alt tarafa bu iki satırı ekliyoruz:
			<script src="{static 'js/bootstrap.min.js'"> </script>
    			<script src="{static 'js/jquery-3.6.0.min.js'"> </script>


15. STATIC_ROOT = BASE_DIR / "staticfiles"
	$ python manage.py collectstatic 


16. CK editor yükleme: pip install django-ckeditor
		python manage.py collectstatic 
		-> from ckeditor.fields import RichTextField
		-> değiştirdik:      content = RichTextField()
		->     {{ myform.media }}
	settings.py'nin altına Allowedcontent ekliyoruz, configure etmek için:
		CKEDITOR_CONFIGS = {
		    "default": {
        		"removePlugins": "stylesheetparser",
        		"allowedContent" : True,-----
        		"width": "100%",  ------------biz ekledik

    		}
}


17. pip install pillow
	settings.py:
	MEDIA_URL = '/media/'
	MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
	templates'a 
        'django.template.context_processors.media',

	urls.py:
    	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

	from django.conf import settings
	from django.conf.urls.static import static

18. django clean_up
	pip install django-cleanup
	installed apps-> django_cleanup

19. Article modeline bunu ekliyoruz:
    article_image = models.FileField(blank= True, null = True, verbose_name = "Add image")
	model değiştiği için:  makemigrations & migrate yapıyoruz. sonra da runserver.
	forms.py -> "article_image"
	views.py ->     form = ArticleForm(request.POST or None, request.FILES or None)
