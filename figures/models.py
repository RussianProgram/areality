from django.db import models
from django.urls import reverse

class Figure(models.Model):

    name = models.CharField(max_length=100)
    url = models.URLField()
    images = models.ImageField(upload_to='figures/%Y/%m/%d')
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True, db_index=True)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('figures:detail', args=[self.id])
