"""

Task 2, Task 3

"""

import requests
from decimal import *
from datetime import date

getcontext().prec = 4


def currency_rates(val):
    val = val.upper()
    feedback = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if val not in feedback:
        return None

    money = feedback[feedback.find('<Value>', feedback.find(val)) + 7:feedback.find('</Value>', feedback.find(val))]
    day_untreated = feedback[feedback.find('Date="') + 6:feedback.find('"', feedback.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_untreated)
    return f"{Decimal(money.replace(',', '.'))}, {date(day=day, month=month, year=year)}"


print(currency_rates('USD'), 'текущий курс американского доллара') # Доллар американский (по заданию)
print(currency_rates('EUR'), 'текущий курс евро') # Евро (по заданию)
print(currency_rates('AZN'), 'текущий курс азербайджанского маната') # Для примера - азербайджанский манат
print(currency_rates('CAD'), 'текущий курс канадского доллара') # Для примера - канадский доллар
print(currency_rates('CNY'), 'текущий курс китайского юаня') # Для примера - китайский юань
print(currency_rates('NOK'), 'текущий курс норвежского крона') # Для примера - норвежский крон
print(currency_rates('BYN'), 'текущий курс белорусского рубля') # Для примера - белорусский рубль
print(currency_rates('BRL'), 'текущий курс бразильского реала') # Для примера - бразильский реал
print(currency_rates('INR'), 'текущий курс индийского рупия') # Для примера - индийский рупий
print(currency_rates('SGD'), 'текущий курс сингапурского доллара') # Для примера - сингапурский доллар
print(currency_rates('TRY'), 'текущий курс турецкого лира') # Для примера - турецкий лир
print(currency_rates('JPY'), 'текущий курс японского иена') # Для примера - японский иен
print(currency_rates('CHF'), 'текущий курс швейцарского франка') # Для примера - швейцарский франк