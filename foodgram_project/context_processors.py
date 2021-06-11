from data.models import Purchase


def purchases_number(request):
    return {
        'purchases_number': Purchase.objects.filter(user=request.user).count()
    }
