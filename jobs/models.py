from django.db import models

class Job(models.Model):
    JOB_TYPES = (
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('contract', 'Contract'),
    )

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, db_index=True)
    category = models.CharField(max_length=100, db_index=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, db_index=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Meta:
    indexes = [
        models.Index(fields=['title', 'location']),
        models.Index(fields=['category', 'job_type']),
    ]
