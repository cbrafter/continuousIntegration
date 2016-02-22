import unittest as ut

class FibTest(ut.TestCase):
	
	def test_fibonacci(self):
		"""
		In this unciton we import fibonnacci.py
		and test we get the correct sequence
		"""
		import fibonacci as fb
		assert fb.Fibonacci(10) == 55
		assert fb.Fibonacci(5) == 5

	def test_Fib_throws_exeption(self):
		self.assertRaises(ValueError, fb.Fibonacci, -5)
		self.assertRaises(ValueError, fb.Fibonacci, 5.5)
