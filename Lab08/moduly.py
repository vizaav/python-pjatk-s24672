"""
Lab08 - moduły
"""

# importowanie modułu
import datetime

czas = datetime.time(8, 49, 59)
print(czas)
print(str(czas.hour) + "-" + str(czas.minute) + "-" + str(czas.second) + "-twoja-ostatnia-" + str(czas.microsecond))
