from ..utils import *

def homepage(request):
    #news = New.objects.all().filter(is_private=False)
    data = {}
    return render(request, 'Pages/HomePage.html', context=data)


