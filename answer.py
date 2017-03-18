def get_answer(question):
	question=str(question)
	question=question.lower()
	answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
	return answers.get(question,'зачем')
print(get_answer('ненес'))