from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from django.conf import settings
from courses.models import Course, Category, Review

'''class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['title']
'''

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        price = serializers.DecimalField(max_digits=10, decimal_places=2)
        fields = ('id', 'category', 'title', 'image', 'slug', 'owner',
                  'price', 'currency', 'overview')

#serializer for CustomUser registration
class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
