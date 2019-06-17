# -*- coding: utf-8 -*-

# for chinese characters.

from django.shortcuts import render


from .models import UserMessage


# Create your views here.
def getform(request): #request: <WSGIRequest: GET '/form/'>
    all_messages = UserMessage.objects.filter(name='poppy3')
    if all_messages:
        message = all_messages[0]
    #all_messages.delete()
    # # allows you to use for loop
    for message in all_messages:
        message.delete()

        #show data in html





    #   print(message.name)
    # worked but have no idea how it works

    # if request.method == "POST":
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "helloworld4"
    #     user_message.save()

    # user_message = UserMessage()
    # user_message.name = "poppy3"
    # user_message.message = "RUARUARUA3"
    # user_message.address = "SF3"
    # user_message.email = "pp@gmail.com3"
    # user_message.object_id = "helloworld23"
    # user_message.save()
    return render(request, "message_form.html", {
        "my_message": message
    })