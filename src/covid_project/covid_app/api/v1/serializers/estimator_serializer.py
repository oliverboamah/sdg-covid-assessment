# third party imports
from rest_framework import serializers

# covid_app imports
from src.covid_project.covid_app.api.v1.serializers.region_serializer import RegionSerializer


class EstimatorSerializer(serializers.Serializer):
    region = RegionSerializer()
    periodType = serializers.CharField(max_length=50000)
    timeToElapse: serializers.IntegerField()
    reportedCases = serializers.IntegerField()
    population = serializers.IntegerField()
    totalHospitalBeds = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
