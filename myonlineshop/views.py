from django.shortcuts import render
from django.http import HttpResponse
from . models import Product,Contact,Order,OrderUpdate
from math import ceil
import json 

# Create your views here.

def index(request):
       products = Product.objects.all()
       print(products)      
       allProds=[]
       catprods =Product.objects.values('category','id')
       cats={item['category'] for item in catprods}
       for cat in cats:
              prod=Product.objects.filter(category=cat)
              n=len(prod)
              nSlides= n//4 +ceil((n/4)-(n//4))
              allProds.append([prod,range(1,nSlides),nSlides])
       params= {'allProds':allProds}
       return render(request,"myonlineshop/index.html",params)
def searchMatch(query,item):
       ''' return true  only quer '''
       if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
              return True
       else:
              return False
def search(request):
       query = request.GET.get('search')     
       products = Product.objects.all()
       print(products)      
       allProds=[]
       catprods =Product.objects.values('category','id')
       cats={item['category'] for item in catprods}
       for cat in cats:
              prodtemp=Product.objects.filter(category=cat)
              prod= [item for item in prodtemp if searchMatch(query,item) ]
              n=len(prod)
              nSlides= n//4 +ceil((n/4)-(n//4))
              if len(prod)!=0:
                     allProds.append([prod,range(1,nSlides),nSlides])
       params= {'allProds':allProds}
       if len(allProds) == 0 or len(query)<4:
              params={'msg':"Plzzz make sure to enter relevant search query"}
       return render(request,"myonlineshop/search.html",params )  

       
def about(request):     
       return render(request,"myonlineshop/about.html")    
def contact(request):
       thank=False
       if request.method=="POST":              
              name = request.POST.get('name','')
              email = request.POST.get('email','')
              phone = request.POST.get('phone','')
              desc = request.POST.get('desc','')
              print(name,phone,desc,email)
              contact=Contact(name=name, email=email,phone=phone,desc=desc)   
              contact.save()
              thank=True
       return  render(request,"myonlineshop/contact.html",{'thank':thank})        
     
def checkout(request):
       if request.method=="POST":
              item_json= request.POST.get('itemJson', '')
              name = request.POST.get('name','')
              email = request.POST.get('email','')
              phone = request.POST.get('phone','')
              address = request.POST.get('address1','')+ " " + request.POST.get('address2','')
              city = request.POST.get('city','') 
              state = request.POST.get('state','')
              zip_code= request.POST.get('zip_code','')
              order=Order(name=name, email=email,phone=phone,address=address,city=city,state=state,zip_code=zip_code,
                    item_json=item_json)
              order.save() 
              update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
              update.save()             
              thank = True
              id = order.order_id                                                              
              return render(request ,"myonlineshop/checkout.html",{'thank':thank,'id':id})  
       return render(request, 'myonlineshop/checkout.html')  
def productview(request,myid):
       product=Product.objects.filter(id=myid)
       print(product)
       
       return render(request,"myonlineshop/productview.html",{'product':product[0]})
def tracker(request):
       if request.method=="POST":
              orderId = request.POST.get('orderId','')
              email = request.POST.get('email','')
            
              try:
                  order=Order.objects.filter(order_id=orderId,email=email)
                
                  if len(order)>0:
                         update=OrderUpdate.objects.filter(order_id=orderId)
                         updates=[]
                         for item in update:
                                 updates.append({'text':item.update_desc,'time':item.timestamp})
                                 response=json.dumps({'status':'success', 'updates':updates,'itemJson':order[0].item_json},default=str)
                         return HttpResponse(response)
                  else:
                     return HttpResponse('{"status":"error"}')
              except Exception as e :
                     return HttpResponse('{"status":"error"}')        
       return render(request,"myonlineshop/tracker.html" )   
     
