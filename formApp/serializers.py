from rest_framework import serializers
from django.core.validators import EmailValidator
from .models import *

class CodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codes
        fields = '__all__'

class FormDataSerializer(serializers.ModelSerializer):
    code = CodesSerializer(many=True, read_only=True)

    class Meta:
        model = FormData
        fields = '__all__'

    def validate_montant(self, value):  
        if value <= 0:  
            raise serializers.ValidationError({"montantErr": "Erreur sur le montant"})  
        return value
    
    def validate_mail(self, value):  
        email_validator = EmailValidator()  
        try:  
            email_validator(value)
        except DjangoValidationError:  
            raise serializers.ValidationError({"mailErr": "Adresse mail non valide"}) 

        return value 

    # def create(self, validated_data):
    #     form_data = FormData.objects.create(**validated_data)
    #     form_data.code.add(codes_data)
    #     # for code_data in codes_data:
    #     #     Codes.objects.create(form=form_data, code=code_data)
    #     return form_data