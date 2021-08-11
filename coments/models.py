from django.db import models
from users.models import User
from posts.models import Posts
from django.db.models import CASCADE

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=False)
    post = models.ForeignKey(Posts, on_delete=CASCADE, null=False)
    

