from django.db import models

# Create your models here.
class CapitalModel(models.Model):
    name = models.TextField()

    @property
    def autocomplete(self):
        """
        Marks the model has having autocomplete.
        """
        return True
