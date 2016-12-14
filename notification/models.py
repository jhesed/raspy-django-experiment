from django.db import models

# Create your models here.

class Notification(models.Model):
    villager_id = models.IntegerField()
    house_coordinates = models.CharField(max_length=50, help_text='i.e. 99,402,20')
    gmap_coordinates = models.CharField(max_length=50, blank=True)
    is_active = models.IntegerField()  # 0 = inactive, 1 = active
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return 'Alarm by villager {0} on {1} ({2})'.format(
            self.villager_id, str(self.date_created), 
            "ACTIVE" if self.is_active == 1 else "INACTIVE")