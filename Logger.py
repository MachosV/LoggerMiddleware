import base64
import re
import os
import tempfile
from django.http import HttpResponse
from django.conf.urls import url
from .LoggerConfig import *
from ..urls import urlpatterns


class MonitorLogger(object):

    log_file_path = tempfile.gettempdir()+"/djangoaccess.log"

    def __init__(self):
        if os.access(LOG_FILE_FOLDER_PATH, os.W_OK):
            self.log_file_path = LOG_FILE_FULL_PATH
        new_url = "^" + URL
        new_url = url(new_url, get_from_file)
        urlpatterns.insert(0, new_url)

    def process_request(self, request):
        data = request.method+" "
        data += request.path+"\n"
        for header in sorted(filter(lambda k: re.match(r'(HTTP_|CONTENT_)', k), request.META)):
            data += header.title().replace("_", "-")+": "+request.META[header]+"\n"
        data += "\n"+request.body
        ip = request.META['REMOTE_ADDR']
        data = ip+":"+base64.b64encode(data)
        open(self.log_file_path, "a+").write(data+"\n")


def get_from_file(request):
    if request.GET.get(AUTH_PARAMETER) == AUTH_KEY:
        return HttpResponse(open(MonitorLogger.log_file_path, "r").read())
    else:
        return HttpResponse("Omae wa mo shindeiru!")