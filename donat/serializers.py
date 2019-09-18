from rest_framework import serializers
from .models import DonatorsData, DonationsData, DonatsSourcesData


class DonatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonatsSourcesData
        fields = '__all__'


class DonatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonatorsData
        fields = '__all__'


class DonationsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)
    source = serializers.CharField(write_only=True)
    details = serializers.CharField(write_only=True)


    # donator = DonatorsSerializer(read_only=True)
    # donat_source = DonatsSerializer(read_only=True)

    class Meta:
        model = DonationsData
        fields = '__all__'
        depth = 2
        read_only_fields = ('id', 'donat_source', 'donator')

    def create(self, validated_data):
        donators, donators_create = DonatorsData.objects.get_or_create(name=validated_data.get('name'))
        donat = DonatsSourcesData.objects.create(source=validated_data.get('source'),
                                                 details=validated_data.get('details'))
        donation = DonationsData.objects.create(donator=donators, donat_source=donat,
                                                summ=validated_data.get('summ'))
        return donation
