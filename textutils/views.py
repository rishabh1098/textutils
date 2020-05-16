#i have crated this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = request.POST.get('text','off')
    removepunc=request.POST.get('removepunc','off')
    capatilize=request.POST.get('capatilize','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= ""
        for char in djtext: 
            if not(char in punctuations): 
                analyzed=analyzed+char
        print(analyzed)
        params={'purpose':'Remove Punctuations','analyzed_text' : analyzed}
        djtext = analyzed
        #return render(request,'analyzed.html',params)
    if capatilize=="on":
        analyzed= ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        print(analyzed)
        params={'purpose':'Change to upper case','analyzed_text' : analyzed}
        djtext=analyzed
        #return render(request,'analyzed.html',params)
    if newlineremover=="on":
        analyzed= ""
        for char in djtext :
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        print(analyzed)
        params={'purpose':'Remove Lines','analyzed_text' : analyzed}
        djtext= analyzed
        # return render(request,'analyzed.html',params)
    if spaceremover=="on":
        analyzed= ""
        for index,char in enumerate(djtext) :
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        print(analyzed)
        params={'purpose':'Remove Space','analyzed_text' : analyzed}
        djtext=analyzed
        #return render(request,'analyzed.html',params)
    if charcounter=="on":
        count=0
        for char in djtext :
            if char in djtext:
                count=count+1
        print(count)
        params={'purpose':'Count Charaters','analyzed_text' : count}
        
        #return render(request,'analyzed.html',params)
    if (removepunc!="on" and capatilize!="on" and newlineremover!="on" and spaceremover!="on" and charcounter!="on"):
        return HttpResponse("Error 404")
    return render(request,'analyzed.html',params)
def about(request):
    return render(request,'about.html')
