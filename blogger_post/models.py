from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogPost(models.Model):
    author_name = models.OneToOneField(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to="featured/%Y/%m/%d/",blank=True,null=True)
    title  = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50,default='')
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
