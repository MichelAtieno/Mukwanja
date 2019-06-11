from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default="")


class Event(models.Model):
    CATEGORIES = (
    ('Entertainment','Entertainment',),
    ('Movies','Movies'),
    ('Conferences','Conferences'),
    ('Sports','Sports'), 
    )
    poster = models.ImageField(upload_to='events/')
    title = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    information = models.CharField(max_length = 500)
    event_category = models.CharField(max_length=50,choices=CATEGORIES)
    

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

    @classmethod
    def search_event(cls, search_term):
        events = cls.objects.filter(event_category__icontains = search_term)
        return events