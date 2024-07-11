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
"""

ACCOUNTS = [
    {
        "name": "Kabila",
        "token": "1720620421296MpOzj0nA5sjA6xTqkVTXvUOfLLLMFFPODkCbjudx7imhZRQYEve7o4ZgoT10r8Jq7122109324",
        "buy_upgrades": True,
        "buy_decision_method": "profitness",
        "min_balance": 8000000
    },
    {
        "name": "Egor Pavlovskiy",
        "token": "17206242479548KZ9HDf3Bj73Am1eGw03XlNSBnrJuvRn2MkpdNxLcACb4ZT4VG0aeihkTe9ARe2Z680751048",
        "buy_upgrades": True,
        "buy_decision_method": "profitness",
        "min_balance": 20000000
    },
    {
        "name": "KEBA",
        "token": "1720624389973fy8iYpcNJWpnBwqEYI1dCxP9snNOotGWkGRJek1xI8MasGHZoBJZkoDfwsD3EkyP2017765387",
        "buy_upgrades": True,
        "buy_decision_method": "profitness",
        "min_balance": 15000000
    },
    {
        "name": "The Time G MAN X",
        "token": "1720624468635paaOLVul82uBhKxcN6CJywWDePzmPHek3sldDJiiFx3PeHu2zr0eHGL9x8bFHB6P6627481578",
        "buy_upgrades": True,
        "buy_decision_method": "profitness",
        "min_balance": 5000000
    },
     {
        "name": "Adbu Boikek",
        "token": "1720624584149CTSLDAeb5gdzZMepFdV377katDQUvnfCcEcUPPt9WmTXRsvG1dp4YrMv0zdVcOpE6770981609",
        "buy_upgrades": True,
        "buy_decision_method": "profitness",
        "min_balance": 5000000
    },
     {
        "name": "Buo Bobo",
        "token": "1720624673546UitVh6PMRrmH8jhmkOfRg9GHTs5B6NcNpNhIL4JFHrzJyOqSMwMuqkxLRMTUYjE46892368656",
        "buy_upgrades": True,
        "buy_decision_method": "profitness",
        "min_balance": 10000000
    },
     {
        "name": "Lala Lolo",
        "token": "1720624745599ncSWnb5DIAmQfLeLIATEFbt6ZSInb2xX7eII9gWOpgqYH0F3k0M4InH1Ho2JA2r97133733698",
        "buy_upgrades": True,
        "buy_decision_method": "profitness",
        "min_balance": 20000000
    },
     {
        "name": "Coco Dghd",
        "token": "1720624804483NEzH2LDm01xIMiVKryV11HoQCHtKhJ4qfdsKBiCpm2PvTMbOppQZluyoVXpRj0Ub7057649960",
        "buy_upgrades": True,
        "buy_decision_method": "profitness",
        "min_balance": 20000000
    },
     {
        "name": "Fdas Ananas",
        "token": "1720624876673wCl8zodjwKnJ3q7oK8j3YUDFP4l6r34pIUdSAPFFGPSbVJzo3vYXvyLsmEC1gdyG7113926564",
        "buy_upgrades": True,
        "buy_decision_method": "profitness",
        "min_balance": 20000000
    }
]
