from django.db import models

# Create your models here.


class FeedModel(models.Model):
    class Meta:
        db_table = 'feed_list'
        verbose_name = 'feed'
        verbose_name_plural = 'feeds'

    link = models.CharField(blank=False, max_length=600)

