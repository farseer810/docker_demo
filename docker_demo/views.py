#-*- coding: utf-8 -*-
import socket

from django.http import HttpResponse

def index(request):
    text = """<b>Hostname: {0}</b>\n""".format(socket.gethostname())
    return HttpResponse(text)
