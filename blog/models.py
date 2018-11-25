from django.db import models


class Blog(models.Model):
    title=models.CharField(max_length=200)
    publish_date=models.DateTimeField()
    image=models.ImageField(upload_to='images/')
    body=models.TextField()

    def summary(self):
        return self.body[:100]

    def correctdate(self):
        return self.publish_date.strftime('%b %e,%Y')

    def __str__(self):
        return self.title

