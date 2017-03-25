def cut_cake (parts,vats):
	try:
		return int(vats)/ int(parts)
	except (ZeroDivisionError, TypeError,ValueError:
		return 'Вы что с ума сошли?'
cake=cut_cake (10,12)
print(cake)

