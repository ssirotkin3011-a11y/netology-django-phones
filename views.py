from django.shortcuts import render, get_object_or_404

from catalog.models import Phone


def catalog(request):
    """Список всех телефонов с поддержкой сортировки."""
    sort = request.GET.get('sort')

    sort_map = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }

    phones = Phone.objects.all()
    order_field = sort_map.get(sort)
    if order_field:
        phones = phones.order_by(order_field)

    return render(request, 'catalog/catalog.html', {
        'phones': phones,
        'sort': sort,
    })


def phone_detail(request, slug):
    """Страница отдельного телефона."""
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'catalog/phone.html', {'phone': phone})
