import io
import os

from django.http import HttpResponse, JsonResponse, FileResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Book, BookVersion, Files as Image
import matplotlib.pyplot as plt
import io

@csrf_exempt
def list_books(request):
    # Search
    if request.method != "GET":
        return HttpResponse(status=405,content="Method not allowed")

    books = Book.objects.all().values()
    ans = []
    for i in books:
        ans.append(i)

    return JsonResponse(ans, safe=False)

@csrf_exempt
def create_book(request):

    if request.method != "POST":
        return HttpResponse(status=405, content="Method not allowed")

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    book = Book.objects.create(**body)
    book.save()

    try:
        bookVersion = BookVersion.objects.get(id=1)
        bookVersion.version = 1
        bookVersion.save()
    except:
        BookVersion.objects.create(version=1)

    return JsonResponse(body)

@csrf_exempt
def update_book(request, id:int):

    if request.method != "PUT":
        return HttpResponse(status=405, content="Method not allowed")

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    book = Book.objects.get(id=id)
    book.name =  body['name']
    book.author = body['author']
    book.description = body['description']
    book.price = body['price']
    book.save()

    bookVersion = BookVersion.objects.get(1)
    bookVersion.version = 1
    bookVersion.save()

    return HttpResponse(content="OK")


@csrf_exempt
def graph(request):

    if request.method != "GET":
        return HttpResponse(status=405, content="Method not allowed")

    bookVersion = BookVersion.objects.get(id=1)

    if bookVersion.version != 1:
        print(1)
        img = Image.objects.get(id=1)
        buffer = io.BytesIO(img.file)


        return FileResponse(buffer,content_type=img.type)

    books = Book.objects.all()

    names = [book.name for book in books]
    prices = [book.price for book in books]
    fig, ax = plt.subplots()


    ax.set_title('Book Prices')
    ax.set_xlabel('Names')
    ax.set_ylabel('Prices')


    # # Create the bar graph
    plt.plot(names, prices)

    # Convert the plot to a binary string and get its mime type
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    mime_type = 'image/png'

    img = None
    try:
        img = Image.objects.get(id=1)
        img.file = buf.read()
        img.save()
    except:
        img = Image.objects.create(type=mime_type, file=buf.read())


    bookVersion.version = 0
    bookVersion.save()

    buf.seek(0)

    return FileResponse(buf, content_type=mime_type)