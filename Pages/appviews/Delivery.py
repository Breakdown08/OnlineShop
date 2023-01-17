from ..utils import *


def delivery(request):
    data = {}
    return render(request, 'Pages/Delivery.html', context=data)
