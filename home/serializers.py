from rest_framework import serializers
from .models import Blog



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        models = Blog
        exclude = ['created_at' , 'updated_at']