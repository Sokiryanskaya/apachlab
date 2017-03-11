def take_price(first):
	first=first.upper()
	city={'Красноярск':'нет ответа','Иваново':'лучшие условия','Москва':'вам перезвонят'}
	return  city.get(first,'отказано в условиях')
print(take_price('Красноярск'))