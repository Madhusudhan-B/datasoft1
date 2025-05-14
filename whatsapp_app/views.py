from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .utils.whatsapp import send_whatsapp_message

def send_message_view(request):
    # For testing purposes (replace with form input or request body)
    response = None
    if request.method == "POST":
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        response = send_whatsapp_message(phone, message)
    #return JsonResponse(response)
    return render(request, 'send_messages.html', {'response': response})

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'GET':
        verify_token = 'your_custom_token'
        if request.GET.get('hub.verify_token') == verify_token:
            return HttpResponse(request.GET.get('hub.challenge'))
        return HttpResponse("Invalid token", status=403)

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print("Incoming Webhook:", json.dumps(data, indent=2))
        # You can handle or store incoming messages here
        return HttpResponse(status=200)
    return None