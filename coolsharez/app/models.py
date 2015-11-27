from django.db import models


class Category(models.Model):  # extends models
    name = models.CharField(max_length=200)  # suzdava table in database s pole name
    description = models.CharField(max_length=1000)
    picture = models.ImageField()

    def __unicode__(self):
        return self.name


class Quote(models.Model):
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='quotes')  # using  category

    def __unicode__(self):
        return self.description
