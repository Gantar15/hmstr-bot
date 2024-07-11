"""
    ACCOUNTS:
        name -> Имя аккаунта, отображаемое в логах
        token -> Brearer токен аккаунта
        buy_upgrades -> Покупка карточек.
            True -> Включено,
            False -> Выключено
        buy_decision_method -> метод покупки карточек.
            - price -> покупать самую дешевую
            - payback -> покупать ту, что быстрей всего окупится
            - profit -> покупать самую прибыльну
            - profitness -> покупать самую профитную (сколько добыча на каждый потраченный хома-рубль)
        min_balance - минимальный баланс аккаунта.
        buy_combo - покупать ли комбо апгрейды.
"""

ACCOUNTS = [
    {
        "name": "",
        "token": "",
        "buy_upgrades": True,
        "buy_combo": True,
        "buy_decision_method": "profitness",
        "min_balance": 8000000
    },
]
