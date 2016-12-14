from django.db import models

class Villager(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, 
        blank=True, help_text='i.e. 09xxxxxxxxx')
    # lot_number = models.TextField(null=False, blank=False,
    #     help_text="i.e. 1")
    lot_number = models.CharField(max_length=10, help_text="i.e. 1")
    house_coordinates = models.CharField(max_length=50, help_text='i.e. 99,402,20')
    gmap_coordinates = models.CharField(max_length=50, blank=True)
    date_modified = models.DateField(auto_now=True, blank=True)
    
    # optional used for images
    # needs pillow to be installed
    # house_image_closeup = models.ImageField(upload_to='villager/house/', blank=True)
    # street_image_closeup_1 = models.ImageField(upload_to='villager/street/', blank=True)
    # street_image_closeup_2 = models.ImageField(upload_to='villager/street/', blank=True)

    def __str__(self):
            return "%s, %s %s" %(self.last_name, 
                self.first_name, self.middle_name)