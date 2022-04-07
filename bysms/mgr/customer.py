# -*- coding = utf-8 -*-
from django.http import JsonResponse
import json
from common.models import Customer

def dispatcher(request):  #将请求参数统一放入request的params属性中，方便后续处理
                        #GET请求，参数再request对象的GET属性中

    # 根据session判断用户是否是登录的管理员用户
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未登录',
            'redirect': '/mgr/sign.html'},
            status=302)#响应码 302

    if request.session['usertype'] != 'mgr':
        return JsonResponse({
            'ret': 302,
            'msg': '用户非mgr类型',
            'redirect': '/mgr/sign.html'},
            status=302)

    if request.method == 'GET':
        request.params = request.GET
    #POST/PUT/DELETE请求参数从requrst对象的body属性中获取
    elif request.method in ['POST', 'OUT', 'DELETE']:
        #根据接口，POST/PUT/DELETE请求的消息体都是json格式
        request.params = json.loads(request.body)#request.body获取的是request里的原始字符串
                                                # json.losds把获取的json格式的字符串变成python的对象 字典形式的
    #根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_customer':
        return listcustomer(request)
    elif action == 'add_customer':
        return addcustomer
    elif action == 'modify_customer':
        return modifycustomer(request)
    elif action == 'del_customer':
        return delcustomer(request)

    else:
        return JsonResponse({'ret':1, 'msg':'不支持该类型http请求'})

def listcustomer(request):#返回一个QuerSet对象，包含所有的表记录
    qs = Customer.objects.values()
    retlist = list(qs) #将QuerSet对象转化为list类型否则不能被转化为json字符串
    return JsonResponse({'ret': 0, 'retlist': retlist})

def addcustomer(request):
    info = request.params['data']  #从请求消息体中获取要添加的客户的信息
    record = Customer.objects.create(name = info['name'], #create创建记录
                                     phonenumber = info['phonenumber'],
                                     address = info['address']
    )
    return JsonResponse({'ret':0, 'id':record.id})

def modifycustomer(requset):
    #从请求消息中 获取修改客户的信息  找到该客户，并且进行修改操作
    customerid = requset.params['id']
    newdata = requset.params['newdata']

    try:#根据id从数据库找到相应的客户记录
        customer = Customer.objects.get(id = customerid)
    except Customer.DoesNotExist:
        return {
            'ret': 1 ,
            'msg': f"id为'{customerid}'的客户不存在"
        }
    if 'name' in newdata:
        customer.name = newdata['name']
    if 'phonenumber' in newdata:
        customer.phonenumber = newdata['phonenumber']
    if 'address' in newdata:
        customer.addresss = newdata['address']
    customer.save() #注意 一定要执行save才能将修改信息保存到数据
    return JsonResponse({'ret': 0})

def delcustomer(request):
    customerid = request.params['id']
    try:  # 根据id从数据库找到相应的客户记录
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return {
            'ret': 1,
            'msg': f"id为'{customerid}'的客户不存在"
        }
    customer.delete()
    return JsonResponse({'ret': 0})

