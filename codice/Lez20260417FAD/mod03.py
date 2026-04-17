from datetime import date, datetime, timedelta

oggi = date.today()
print(oggi)          # 2026-04-11
print(oggi.year)
print(oggi.month)
print(oggi.day)

adesso = datetime.now()
print(adesso)
print(adesso.year, adesso.month, adesso.day)
print(adesso.hour, adesso.minute, adesso.second)

fra_20_minuti = adesso - timedelta(minutes=24)

# print(f"L'intervallo è iniziato alle ore: {fra_20_minuti}")

print(adesso.strftime("%d/%m/%Y"))   