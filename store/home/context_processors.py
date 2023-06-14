from users.models import Wallet


def balance_context_processor(request):
    balance = 0  # Значение баланса по умолчанию

    if request.user.is_authenticated:
        try:
            wallet = Wallet.objects.get(user=request.user)
            balance = wallet.balance
        except Wallet.DoesNotExist:
            # Обработка случая, когда кошелек не существует
            pass

    return {'balance': balance}