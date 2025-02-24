import json
from django.forms.models import model_to_dict
from django.http import JsonResponse,HttpResponse
from products.models import Product
def api_home(request,*args,**kwargs):
    #1. Echo Get Data
    #2. Django Model Instance as an API response
    #3. django model instance to dictionary


    ######################## 1. Echoing get data##########################################
    # # to access data of params
    # name = request.GET.get('name')
    # age = request.GET.get('age')

    # body = request.body #byte string of json data
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    ##################################################################


    #####################################2. django model instance as an API response ##########################
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        data = model_to_dict(model_data,fields=['id','title','price']) #3.  model instance to dictionary
    return JsonResponse(data)
    # return HttpResponse(data,headers={'content-type':'application/json'}) 
  