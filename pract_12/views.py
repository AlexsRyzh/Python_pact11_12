import io
import os.path

from django.http import HttpResponse,HttpResponseNotAllowed, FileResponse
import json
from django.views.decorators.csrf import csrf_exempt
import matplotlib.pyplot as plt

@csrf_exempt
def gen_graph(request):
    body_json = json.loads(request.body)

    print(body_json)
    if request.method != "POST":
        return HttpResponseNotAllowed("Только POST метод", content="Только POST метод")

    x = body_json['day']
    y = body_json['price']
    plt.plot(x,y)
    buf = io.BytesIO()
    plt.savefig('1.png')

    hash = ' '.join(map(str,x))+" "+' '.join(map(str,x))

    
    # return FileResponse(open('1.png', 'rb'))
    return HttpResponse(hash)