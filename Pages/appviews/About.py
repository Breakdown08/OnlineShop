from ..utils import *


def about(request):
    data = {}
    return render(request, 'Pages/About.html', context=data)
