from rest_framework import serializers
from CourseListAPI.models import Course, Category
from decimal import Decimal
from rest_framework.validators import UniqueValidator
from rest_framework.validators import UniqueTogetherValidator
import bleach


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "slug","title"]

    
class CourseSerializer(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Course
        fields=["id","title","price","price_after_tax","category", "category_id"]    
        extra_kwargs = {'title': {'validators': [UniqueValidator(queryset=Course.objects.all())]}} 
        # no two Course objects have the same title and price combination.
        validators = [
            UniqueTogetherValidator(
                queryset=Course.objects.all(),
                fields=['title', 'price']
            ),
        ]
    def calculate_tax(self, course:Course):
        return Decimal(course.price) * Decimal(1.1)

    def validate_price(self, value):
        if value<10:
            raise serializers.ValidationError("Price cannot be less than 10")
        return value
    
    def validate_title(self, value):
        if len(value)<10:
            raise serializers.ValidationError("Price cannot be less than 10")
        return bleach.clean(value)