from django.db import models

# Create your models here.
class Newjob(models.Model):
    position = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    job_description = models.CharField(max_length=200)
    applied = models.BooleanField(blank=True, null=True)
    type_of_resume_sent = models.CharField(max_length=200)
    date_applied = models.CharField(max_length=200)
    hiring_manager = models.CharField(max_length=200)
    hiring_manager_email = models.CharField(max_length=200)
    interview_status = models.CharField(max_length=200)
    application_origin = models.CharField(max_length=200)
    thankyou_sent = models.BooleanField(blank=True, null=True)
