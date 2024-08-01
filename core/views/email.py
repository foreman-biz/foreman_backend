import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@csrf_exempt
@api_view(["POST"])
def send_general_email(request):
    print("we are here")
    try:
        data = request.data
        to_email = data.get("to")
        from_email = data.get("from")
        template_id = data.get("templateId")
        dynamic_template_data = data.get("dynamicTemplateData")
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
        )

        message.dynamic_template_data = dynamic_template_data
        message.template_id = template_id

        sendgrid_api_key = os.getenv("SENDGRID_API_KEY")
        if not sendgrid_api_key:
            print("SENDGRID_API_KEY is not set")
            return Response(
                {"error": "SENDGRID_API_KEY is not set"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)


        return Response(
            {"message": "Email sent successfully", "status_code": response.status_code},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
