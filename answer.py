
answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

def get_answer(question, answers):
	#answers = int(answers)
	#answers = answers.upper
	return answers.get(question)

def ask_user(answers):
	try:
		while True:
			user_input = input('Скажи что-нибудь:')
			answer = get_answer(user_input, answers)
			print(answer)
			if user_input == 'пока':
				break
	except (TypeError, ValueError):
		return 'Что-то пошло не так'
ask_user(answers)