from django.db import models

# Create your models here.
class TimeSlot(models.Model):
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    room_no = models.CharField(max_length=20, default="101")

    def __str__(self):
        return f"{self.day} - {self.subject_name} ({self.start_time})"