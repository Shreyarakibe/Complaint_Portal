from django.db import models  # Provides database-related functionalities
from django.contrib.auth.models import User  # Connects each complaint to a registered user
from django.utils import timezone  # Provides the current timestamp when a complaint is submitted

class Complaint(models.Model):  # Creates a database table named Complaint
    STATUS_CHOICES = [  # Defines the possible complaint statuses
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):  # Defines how complaints appear in Django Admin and Python shell
        return self.title