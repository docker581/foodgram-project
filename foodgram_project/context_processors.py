from data.models import Purchase


def purchases_number(request):
    if request.user:
        return {
            'purchases_number': Purchase.objects.filter(user=request.user).count()
        }
