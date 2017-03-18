def get_vat(payment, percent=18):
	print(percent)
	try:
		payment = float(payment)
		percent = int(percent)
		vat = payment / 100 * percent
		vat = round(vat, 2)
		return "Сумма НДС: {}" .format(vat) 
	except (TypeError, ValueError):
		return 'Не могу посчитать проверьте'
result = get_vat(400,'dsf')	
print(result)


