from rest_framework.serializers import ModelSerializer
from .models import Job


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
        read_only_fields = ["created_by"]
