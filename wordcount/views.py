from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter
def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    counts=len(fulltext.split())
    wordlist=fulltext.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    print(worddictionary.items())
    sortedwords=sorted(worddictionary.items(),key=itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':counts,'sortedwords':sortedwords})

def aboutus(request):
    return render(request,'aboutus.html')
