from django.db import models

# Create your models here.
class Event(models.Model):
    poster = models.ImageField(upload_to='events/')
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    information = models.CharField(max_length = 500)

    class Meta:
        ordering = ('-id',)

    def save_event(self):
        self.save()

    def delete_event(self):
        self.delete()

    def __str__(self):
        return self.title

    @classmethod
    def get_event(cls,id):
        one_event = Event.objects.get(id=id)
        return one_event

    @classmethod
    def get_events(cls):
        all_events = Event.objects.all()
        return all_events