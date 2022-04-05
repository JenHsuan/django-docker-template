from django.http import HttpResponse
from django.http import HttpResponse

# Create your views here.
def first_view(request):
        return HttpResponse("123")
