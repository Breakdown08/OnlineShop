from ..utils import *


def contacts(request):
    data = {}
    return render(request, 'Pages/Contacts.html', context=data)
