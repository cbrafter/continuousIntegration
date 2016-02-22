def test_fibonacci():
	"""
	In this unciton we import fibonnacci.py
	and test we get the correct sequence
	"""
	import fibonacci as fb
	assert fb.Fibonacci(10) == 55
	assert fb.Fibonacci(5) == 5

