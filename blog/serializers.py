from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("title 200 tadan oshmasin")
        return value


    def validate_description(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError("description 1000 tadan oshmasin")
        return value