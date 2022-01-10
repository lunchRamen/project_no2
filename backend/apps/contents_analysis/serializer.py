from apps.user.models import User
from rest_framework import serializers

from .models import ReviewScore, ReviewScoreT


class FirstAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ThirdReviewScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewScoreT
        fields = "__all__"


class FifthReviewScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewScore  # models.py속 모델
        fields = "__all__"  # 통신할 데이터필드 -> 모든 필드 하려면 '__all__'해도 됨
        # fields = ('id','published_date'...,)
