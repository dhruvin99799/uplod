from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create your views here.



def index(request):
    values = []
    if request.method == "POST":
        web_url = request.POST['url']
        resp = requests.get(web_url)
        scrapdata=BeautifulSoup(resp.text,"html.parser")
        table = scrapdata.find('table',class_ ='ws-table-all')
        for data in scrapdata.find_all('tr'):
            for d in data.find_all('td'):
                values.append(d.text)
                print(d.text)
            print('---------')
    return render(request,'index.html',{'data':values})



