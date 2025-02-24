from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=256, null=False)
    text = models.TextField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title


