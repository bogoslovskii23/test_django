from rest_framework import serializers
from .models import Question, Interview


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class InterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

    questions = QuestionSerializer(read_only=True, many=True, source='question')

