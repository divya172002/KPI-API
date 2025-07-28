from rest_framework import serializers
from .models import FormData, BogieDetails, BogieChecksheet, BMBCChecksheet

class BogieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieDetails
        fields = '__all__'

class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        fields = '__all__'

class BMBCChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BMBCChecksheet
        fields = '__all__'

class FormDataSerializer(serializers.ModelSerializer):
    bogieDetails = BogieDetailsSerializer()
    bogieChecksheet = BogieChecksheetSerializer()
    bmbcChecksheet = BMBCChecksheetSerializer()

    class Meta:
        model = FormData
        fields = ['form_number', 'inspection_by', 'inspection_date',
                  'bogieDetails', 'bogieChecksheet', 'bmbcChecksheet']

    def create(self, validated_data):
        bogie_details_data = validated_data.pop('bogieDetails')
        bogie_checksheet_data = validated_data.pop('bogieChecksheet')
        bmbc_checksheet_data = validated_data.pop('bmbcChecksheet')

        bogie_details = BogieDetails.objects.create(**bogie_details_data)
        bogie_checksheet = BogieChecksheet.objects.create(**bogie_checksheet_data)
        bmbc_checksheet = BMBCChecksheet.objects.create(**bmbc_checksheet_data)

        form = FormData.objects.create(
            bogie_details=bogie_details,
            bogie_checksheet=bogie_checksheet,
            bmbc_checksheet=bmbc_checksheet,
            **validated_data
        )
        return form
