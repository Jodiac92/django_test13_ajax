from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def Index(request):
    #JSONTest()
    
    return render(request, 'abc.html')

def Func1(request):
    msg = request.GET.get('msg')
    print(msg)
    context = {'key':msg}
    return HttpResponse(json.dumps(context), content_type="application/json")  # render x 부분파일을 넘기기위해 response  content_type는 json모양이다라고 알려줌

def Func2(request):
    datas = [
        {'irum':'홍길동', 'nai':22},
        {'irum':'엄길동', 'nai':23},
        {'irum':'무길동', 'nai':24},
    ]
    return HttpResponse(json.dumps(datas), content_type="application/json")











import json

def JSONTest():
    lan = {  #dict타입 자료
        'id':111,
        'name':'파이썬',
        'history':[
            {'date':'2019-11-25','exam':'basic'},
            {'date':'2019-11-26','exam':'django'},
        ]
    }
    print(type(lan))
    
    # json encoding : 집합형 자료를 문자열로 변환
    jsonString = json.dumps(lan)
    print(jsonString, type(jsonString))
    print('--------------------------')
    
     # json decoding : 문자열을 집합형 자료로 변환
    dic = json.loads(jsonString)
    print(type(dic))
    print(dic['name'])
    for h in dic['history']:
        print(h['date'], h['exam'])