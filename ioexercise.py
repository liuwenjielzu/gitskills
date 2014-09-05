#__name  private var  cannot directly manipulate
#__name__  not private var but special var

'''print 200
with open('/home/icefrog/io','w') as f:
	f.write('hello world!')
	f.write(' making love out of nothing at all')
	

with open('/home/icefrog/io', 'r') as m:
	str = m.read()
	print str
	print str


class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_grade(self):
		print '%s:%s' % (self.name, self.score)


bart = Student('bart', 100)
print bart.name
print bart.score
bart.print_grade()
bart.age = 8
print bart.age
arthas = Student('Arthas mionell', 150)
arthas.print_grade()


class Colleager(Student):
	def print_grade(self):
		print 'Colleage_grade %s:%s' % (self.name, self.score)

jake = Colleager('jake alan', 200)
jake.print_grade()
if isinstance(bart,Colleager):
	print 'true'
else:
	print 'flase'
print len('abc')
print 'abc'.__len__()


class Student(object):
	"""docstring for Stude"""
	__slots__ = ('name', 'score')

bart = Student()
bart.name = 'bart simpson'
bart.score = 190
print '%s: %s' % (bart.name, bart.score)

class GraduStudent(Student):
	#pass
	__slots__ = ('sex', 'height', 'weight')

alan = GraduStudent()
alan.name = 'alan harper'
alan.score = 39
alan.sex = 'male'

print '%s %s %s' % (alan.name, alan.score, alan.sex)

'''
'''
class Student(object):

	@property 
	def score(self):
		return self._score
	
	@score.setter
	def score(self,score):
		if not isinstance(score, int):
			raise ValueError('score must be an integer!')
		if score < 0 or score > 100:
			raise ValueError('score must be between 0 ~ 100!')
		self._score = score

bart = Student()
bart.score = 10
bart.name = 'bart simpson'
print bart.name
print bart.score
'''
# try exercise
'''
try:
	print 'try...'
	r = 10 / 0
	print 'result :', r 
except ValueError,e:
	print e
except ZeroDivisionError, e:
	print 'ZeroDivisionError:',e
except 
finally:
	print 'finally...'
print 'end'
'''
'''
#err.py
import logging  # logging can record error 
#message and make the program continue to run
 
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():

	try:
		bar('0')
	except StandardError, e:
		logging.exception(e)
	finally:
		pass
	

main()
print 'END'
'''

def main():
	try:
		10 / 0
	except ZeroDivisionError:
		raise 

main()