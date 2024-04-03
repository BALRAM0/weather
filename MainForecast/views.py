from django.shortcuts import redirect, render,HttpResponse
from .models import UploadedFile
import weather
import AIcode


obj = weather.API()
aiobj= AIcode.AI()
# Create your views here.

def main(request):
    city = request.GET.get('city','delhi')
    context=obj.run(city)

    return render(request,'main.html',context)

def about(request):
    return render(request,'aboutus.html')

def ai(request):
    
    if request.method == 'POST' and request.FILES['fileToUpload']:
        file = request.FILES['fileToUpload']
        uploaded_file = UploadedFile(file=file)
        
       
        uploaded_file.save() 
        data=UploadedFile.objects.all().values_list()
        data=data[::-1]
        image=data[0]
        print(type(image))
        imagepath=image[1]
        print(imagepath)
      
        print(data)
        
        c,d=aiobj.temp(imagepath)
        fellslike=(c+d)//2
        context={ 
                 
            'image':imagepath,
            'HUMIDITY':aiobj.humidity(imagepath),
            'chanceofrain':aiobj.chanceofrain(imagepath),
            'tempmax':c,
            'tempmin':d,
            'cloud':aiobj.cloud(imagepath),
            'priciptition':aiobj.priciption(imagepath),
            'flike':fellslike
        }
        # Perform further processing with the uploaded file (e.g., save to a specific location, process the image, etc.)
        # Your custom code goes here...
        return render(request, 'uplod.html', context)
    return render(request, 'ai.html')
    
    
    
    