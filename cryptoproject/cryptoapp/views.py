from django.shortcuts import render
from django.http.response import HttpResponse

def home(request):
    import requests
    import json
    price_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,LTC&tsyms=INR")
    price=json.loads(price_request.content)
    api_request=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=json.loads(api_request.content)
    return render(request,'home.html',{'api':api,'price':price})

def prices(request):
    import requests
    import json
    if request.method=="POST":
        quote=request.POST.get('quote')
        quote=str(quote)
        quote=quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote +"&tsyms=INR")
        crypto= json.loads(crypto_request.content)
        return render(request,'prices.html',{'quote':quote,'crypto':crypto})
    else:
        msg='Please Enter Valid Crypto Currency'
        return render(request,'prices.html',{'msg':msg})
