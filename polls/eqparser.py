import re, sympy

def get_response(question):
	return 5
	
def validate_equation(equation):
	pass
	
def parse_equation(equation):
	'''
	Turns 3*{1} into 3*whatever the number in response to question 1 is.
	
	equation - string, composed of Python math operators, and questions surrounded by {}.
	'''
	validate_equation(equation)
	responses = {}
	questions = re.compile("({\d+})")
	find_questions = questions.findall(equation)
	if find_questions is not None:
		xs = ["x{}".format(i) for i in range(len(find_questions))]
		dummy_eq = equation
		for question,x in zip(find_questions,xs):
			responses[x] = get_response(question)
			dummy_eq = dummy_eq.replace(question,x)
		expr = sympy.sympify(dummy_eq).subs(responses.items())
		return expr