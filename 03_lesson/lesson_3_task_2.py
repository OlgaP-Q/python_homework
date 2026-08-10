from smartphone import Smartphone


catalog = []

catalog.append(Smartphone("Apple", "iPhone 15 Pro Max", "+79990000000"))
catalog.append(Smartphone("Sumsung", "Galaxy S24", "+79100000000"))
catalog.append(Smartphone("Xiaomi", "Mi 14 Pro", "+79010000001"))
catalog.append(Smartphone("Google", "Pixel 8 Pro", "+79100000001"))
catalog.append(Smartphone("OnePlus", "12", "+79150000000"))


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
