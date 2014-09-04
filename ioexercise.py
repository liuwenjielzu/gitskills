#__name  private var  cannot directly manipulate
#__name__  not private var but special var

print 200
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
