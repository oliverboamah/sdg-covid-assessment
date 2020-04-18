# third party imports
from rest_framework import serializers


class RegionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50000)
    avgAge = serializers.DecimalField(max_digits=10000, decimal_places=2)
    avgDailyIncomeInUSD = serializers.DecimalField(max_digits=10000, decimal_places=2)
    avgDailyIncomePopulation = serializers.DecimalField(max_digits=10000, decimal_places=2)

    def update(self, instance, validated_data):
        return validated_data

    def create(self, validated_data):
        return validated_data
