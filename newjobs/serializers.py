from .models import Newjob
from rest_framework import serializers

## Class NewjobSerializer is a subclass of serializers.HyperlinkedModelSerializer.
## For serializing and deserializing data into representations such as json.
class NewjobSerializer(serializers.HyperlinkedModelSerializer):
    ## Meta class is for configuring the TodoSerializer class.
    class Meta:
        # model to serialize
        model = Newjob
        # fields to show in json
        fields = ('id','position', 'company_name', 'job_description', 'applied', 'type_of_resume_sent', 'date_applied', 'hiring_manager', 'hiring_manager_email', 'interview_status', 'application_origin', 'thankyou_sent')