from ..utils import *


def bag(request):
    bag_products = BagProduct.objects.filter(user=request.user)
    data = {'bag': bag_products}
    return render(request, 'Pages/Bag.html', context=data)
