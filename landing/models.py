from __future__ import unicode_literals

from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):  #customize django admin
        return "Meail: %s, User: %s" % (self.email, self.name)

    class Meta: #Changing name of the model in the DB
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'