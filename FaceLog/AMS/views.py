from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from AMS.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, login, logout

import cv2
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import threading


# Create your views here.
def showDemoPage(request):
    return render(request, 'demo.html')

def showLoginPage(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackend.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            return HttpResponseRedirect('get_user_details')
            
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/login.html")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" is logged in")
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("login")



class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def stream(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  
        pass