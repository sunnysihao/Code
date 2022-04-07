# -*- coding = utf-8 -*-
# -*- coding = utf-8 -*-
from django.http import JsonResponse
import json
from common.models import Medicine

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
    if action == 'list_medicine':
        return listmedicine(request)
    elif action == 'add_medicine':
        return addmedicine
    elif action == 'modify_medicine':
        return modifymedicine(request)
    elif action == 'del_medicine':
        return delmedicine(request)

    else:
        return JsonResponse({'ret':1, 'msg':'不支持该类型http请求'})

def listmedicine(request):#返回一个QuerSet对象，包含所有的表记录
    qs = Medicine.objects.values()
    retlist = list(qs) #将QuerSet对象转化为list类型否则不能被转化为json字符串
    return JsonResponse({'ret': 0, 'retlist': retlist})

def addmedicine(request):
    info = request.params['data']  #从请求消息体中获取要添加的药品的信息
    record = Medicine.objects.create(name = info['name'], #create创建记录
                                     sn = info['sn'],
                                     desc = info['desc']
    )
    return JsonResponse({'ret':0, 'id':record.id})

def modifymedicine(requset):
    #从请求消息中 获取修改药品的信息  找到该客户，并且进行修改操作
    medicineid = requset.params['id']
    newdata = requset.params['newdata']

    try:#根据id从数据库找到相应的药品记录
        medicine = Medicine.objects.get(id = medicineid)
    except Medicine.DoesNotExist:
        return {
            'ret': 1 ,
            'msg': f"id为'{medicineid}'的客户不存在"
        }
    if 'name' in newdata:
        medicine.name = newdata['name']
    if 'sn' in newdata:
        medicine.sn = newdata['sn']
    if 'desc' in newdata:
        medicine.addresss = newdata['desc']
    medicine.save() #注意 一定要执行save才能将修改信息保存到数据
    return JsonResponse({'ret': 0})

def delmedicine(request):
    medicineid = request.params['id']
    try:  # 根据id从数据库找到相应的药品记录
        medicine = Medicine.objects.get(id=medicineid)
    except Medicine.DoesNotExist:
        return {
            'ret': 1,
            'msg': f"id为'{medicineid}'的药品不存在"
        }
    medicine.delete()
    return JsonResponse({'ret': 0})


