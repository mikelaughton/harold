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
		xs = ["qpk{}".format(i) for i in range(len(find_questions))]
		dummy_eq = equation
		for question,x in zip(find_questions,xs):
			dummy_eq = dummy_eq.replace(question,x)
		expr = sympy.sympify(dummy_eq)
		return expr

def evaluate_equation(equation,responses):
	'''
	Needs {'qpk1':'True','qpk2':'3'}... returns a number based on equation provided.

	equation - sympy expression object
	responses - dict_items as above
	'''
	return equation.subs(responses.items())
