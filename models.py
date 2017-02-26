import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


class Note(models.Model):
    # note_text => note
    note_text = models.CharField(max_length=200)
    # cost value => income or expense
    cost_value = models.IntegerField(default=0)
    # cost_total use for display each total for each note
    cost_total = models.IntegerField(default=0)
    # pub_date => use for arranging
    pub_date = models.DateField('date published')
        
    def __str__(self):
        return self.note_text
        
    