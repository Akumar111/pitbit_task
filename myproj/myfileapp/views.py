
import pytesseract
from django.shortcuts import render, HttpResponse, redirect
from . models import myuploadfile
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'
# Create your views here.


def index(request):
    context = {
        "data": myuploadfile.objects.all(),
    }
    return render(request, "index.html", context)


def send_files(request):
    if request.method == "POST":
        myfile = request.FILES.getlist("uploadfoles")

        for f in myfile:
            extractedInformation = pytesseract.image_to_string(
                Image.open(f))
            myuploadfile(myfiles=f, info=extractedInformation).save()
            print(extractedInformation)

        return index(request)
        # return HttpResponse("ok")
        # return redirect("fileapp:index")
