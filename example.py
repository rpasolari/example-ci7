from pytest import approx

def add(a, b):
	return a + b

def test_add():
	assert add(2, 3) == 5, "The addition of numbers is not correct"
def test_add_strings():
	assert add('space', 'ship') == "spaceship", "The addition of strings is not correct"
