'''class Human:
  def __init__(self):
    self.name = 'None'
    self.age = 0
    self.gender = 'None'
  def introduce(self):
    print('Hello, my name is', self.name)
  def add_info(self):
    self.name = input('Name: ')
    self.age = int(input('Age: '))
    self.gender = input('Gender: ')

obj = Human()
obj.introduce()
obj.add_info()
obj.introduce()'''

from random import *

class Student:
	def __init__(self, name):
		self.name = name
		self.gladness = 50
		self.progress = 0
		self.alive = True
		
	def study(self):
		print('Study time:')
		self.progress += 0.12
		self.gladness -= 5
		
	def sleep(self):
		print('Sleep time:')
		self.gladness += 3
		
	def chill(self):
		print('Chill time:')
		self.gladness += 5
		self.progress -= 0.1
		
	def is_alive(self):
		if self.progress < -0.5:
			print('You did not study and did not pass the exam. Life is over.')
			self.alive = False
		elif self.gladness <= 0:
			print('You are too unhappy. Life is over.')
			self.alive = False
		elif self.progress > 5:
			print('You passed the exam! Life is completed!')
			self.alive = False
		
	def end(self):
		print('Gladness:', self.gladness)
		print('Progress:', self.progress)
		
	def live(self, day):
		print('Day:',day)
		live_cube = randint(1,3)
		if live_cube == 1:
			self.study()
		elif live_cube == 2:
			self.sleep()
		elif live_cube == 3:
			self.chill()
		self.end()
		self.is_alive()

obj = Student('Bob')

for day in range(365):
	if obj.alive == False:
		break
	obj.live(day)