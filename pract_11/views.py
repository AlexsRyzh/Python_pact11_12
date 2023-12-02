from django.http import HttpResponse

# Create your views here.
def index(request):
    name = request.GET.get("name")
    if name == None or name == "":
        return HttpResponse(status=404, content="Name not found in request")

    return HttpResponse(f"Hello {name}!")