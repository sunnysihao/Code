from django.shortcuts import render
from django.http import HttpResponse
from common.models import Customer

def listorders(request):
    return HttpResponse("下面是订单信息...")
def hello(request):
    return HttpResponse("hello world")

    #定义好一个html模板
    #<tr>表示一行
    #<th>表示表头
html_template = '''
<!DOCTYPE>
<html>
<head>
<meta charset = "UTF-8">
<style>
table {
    border-collapse: collapse;
}
th,td {
    padding:8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话</th>
        <th>地址</th>
        <th>QQ</th>
        </tr>


        %s


        </table>
    </body>
</html>
'''


def listcustomers(request):
    # 返回一个QuerySet对象，包含所有的表对象
    # 每条表记录都是一个dict对象
    # key是字段名，value是值
    qs = Customer.objects.values()  #objects是django里用来操作数据库的一个管理接口
    #检查url中是否有参数
    ph = request.GET.get('phonenumber', None)
    #如果有，添加过滤条件
    if ph:
        qs = qs.filter(phonenumber = ph)
        #filter 相当于SQL里的WHERE 条件
    # 生成html中要插入的html片段内容
    tableContent = ''
    for customer in qs:
        tableContent += '<tr>'
        for name, value in customer.items():
            tableContent += f'<td>{value}</td>'
        tableContent += '</tr>'
    return HttpResponse(html_template % tableContent)
    # #定义返回字符串
    # retStr = ''
    # for customer in qs:
    #     for name, value in customer.items():  #dict对象的items()方法，取出键值对
    #         retStr += f'{name}:{value} |'
    #     # <br> 表示换行
    #     retStr += '<br>'
    # return HttpResponse(retStr)
