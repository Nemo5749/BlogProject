from django.db import models

from django.utils import timezone
from django.utils.html import strip_tags# 重要哦,剥去html标签
from django.contrib.auth.models import User
from django.urls import reverse
class Category(models.Model):
    name=models.CharField("目录",max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='分类'
        verbose_name_plural= verbose_name
class Post(models.Model):
    title = models.CharField('标题',max_length=30)
    body = models.TextField("正文")
    create_time =models.DateTimeField('创建时间',default=timezone.now())
    modified_time=models.DateTimeField('修改时间')
    category = models.ForeignKey(Category, verbose_name='分类',on_delete=models.CASCADE)
    excerpt = models.CharField('摘要',max_length=75,blank=True)
    citeFrom=models.TextField("参考资料",blank=True)
    author =models.ForeignKey(User, verbose_name='作者',on_delete=models.CASCADE)
    def save(self,*args,**kwargs):
        self.modified_time =timezone.now()
        self.excerpt=strip_tags(self.body)[:54]
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    class Meta:
            verbose_name = '文章'
            verbose_name_plural = verbose_name
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
# Create your models here.
