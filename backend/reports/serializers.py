from rest_framework import serializers

from reports.models import AdReport, UserReport


class AdReportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('reporter', 'ad')
        model = AdReport


class UserReportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('reporter', 'reported')
        model = UserReport
