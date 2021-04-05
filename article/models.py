from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name="Article Author")  #bu user silindiğinde o user'a ait olan article'lar da silinecek
    title = models.CharField(max_length=50, verbose_name="Article Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Article Date")
    article_image = models.FileField(blank= True, null = True, verbose_name = "Add image here")
    def __str__(self):
        return '%s - %s' % (self.title, self.author)
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete= models.CASCADE, verbose_name = "ARTICLE", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="Name")
    comment_content = models.CharField(max_length=200, verbose_name="Comment Text")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']