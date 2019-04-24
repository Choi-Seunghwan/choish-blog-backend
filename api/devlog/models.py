from django.db import models
from django.utils.text import slugify

# Create your models here.

def generate_unique_slug(klass, field):
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb +=1
    return unique_slug

class Devlog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400)
    slug = models.SlugField(unique=True, allow_unicode=True, default="")
    contents = models.TextField()
    tag = models.CharField(max_length=100)
    cover_image_url = models.CharField(max_length=300, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True )
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        #!log
        #슬러그 우선 영어로만 직접 쓰는 방식으로 해놓고
        #나중에 공백일 땐 title unicode 값으로 설정, 이런 식으로 함수 돌리자.
        # self.slug = generate_unique_slug(Post, self.title)
        super(Devlog, self).save(*args, **kwargs)
    