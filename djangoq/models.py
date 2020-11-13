from django.db import models
from django_q.models import Schedule

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    schedule_id = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        schedule = Schedule.objects.create(
            name = self.__str__(),
            func = 'djangoq.services.send_email',
            args = f"'{self.email}'",
            schedule_type = Schedule.DAILY,
        )
        self.schedule_id = schedule.pk
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        Schedule.objects.get(pk=self.schedule_id).delete()
        super().delete(*args, **kwargs)