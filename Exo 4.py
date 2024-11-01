"""
import unittest
import luhn

class MyTestCase(unittest.TestCase):
	def test_sommeListe(self):
		self.assertEqual(luhn.sommeListe([1, 2, 3]), 6)
		self.assertEqual(luhn.sommeListe([0]), 6)

	def test_reduire(self):
		self.assertEqual(luhn.reduire(7), 7)
		self.assertEqual(luhn.reduire(17), 8)

if __name__ == '__main__':
    unittest.main()
"""

def sommeListe(l):
	if l == []:
		return "Erreur, liste vide"
	s = 0
	for ele in l:
		s += int(ele)
	return s

def reduire(n):
	if n < 0 or n > 18:
		return "Erreur, entier dicident"
	l = list(str(n))
	return sommeListe(l)

def toListe(n):
	l = []
	while n > 0:
		l.append(n % 10)
		n //= 10
	return l

def double(l):
	l2, n = [], 1
	for ele in l:
		if n == 1:
			ele *= 2
			l2.append(reduire(ele))
		else:
			l2.append(ele)
		n *= -1
	return l2

def final(num):
	code = num % 10
	num //= 10
	l = toListe(num)
	l = double(l)
	total = sommeListe(l)
	total %= 10
	return total + code == 10

print(reduire(17))
print(toListe(497010123456789))
print(double([9, 8, 7, 6, 5, 4, 4, 3, 2, 1, 0]))
print(final(3056493108767124))
