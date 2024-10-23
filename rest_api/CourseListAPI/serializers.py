from rest_framework import serializers
from decimal import Decimal
from .models import Course, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=["id", "slug","title"]

class CourseSerializer(serializers.ModelSerializer):
    course_price = serializers.IntegerField(source = "price")
    price_after_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    class Meta:
        model = Course
        fields=["id","title","price", "course_price","price_after_tax","category"]
        depth=1
    def calculate_tax(self, course:Course):
        return Decimal(course.price) * Decimal(1.1)