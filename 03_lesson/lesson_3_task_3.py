from Address import Address
from Mailing import Mailing

to_adress = Address("123456", "Moscow", "Twerskaya", "14", "12")
from_adress = Address("654321", "Saint Petersburg", "Nevsky", "24", "54")

mailing = Mailing(to_adress, from_adress, 350.50, "TRACK123456789")

print(f"Отправление {mailing.track} из {mailing.from_adress.index}"
      f", {mailing.from_adress.city}, {mailing.from_adress.street}"
      f", {mailing.from_adress.house}"
      f" - {mailing.from_adress.apartment} в {mailing.to_adress.index}"
      f", {mailing.to_adress.city}"
      f", {mailing.to_adress.street}"
      f", {mailing.to_adress.house} - {mailing.to_adress.apartment}"
      f".Стоимость {mailing.cost} рублей.")
