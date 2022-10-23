from random import *



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




'''class University:
	def __init__(self, title, faculty):
		self.title = title
		self.faculty = faculty
		self.budget = False;
    
	def check_progress(self, student):
		if student > 3:
			self.budget = True
		self.isbudget()

	def isbudget(self):
		if self.budget == True:
			print('Congratulation! You are on budget!')


class Student:
	def __init__(self, name):
		self.name = name
		self.gladness = 50
		self.progress = 0
		self.alive = True

  def ask_budget(self, university):
		university.check_progress(self.progress)
    
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
    if day % 10 == 0:
			self.ask_budget(univer)
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

univer = University('Step Univer', 'Computer Science')

for day in range(365):
	if obj.alive == False:
		break
	obj.live(day)'''



'''class Human:
	def __init__(self, name):
		self.name = name
		self.gender = 'None'
		self.age = 0
	def live(self):
		print(self.name, 'is alive')
	def happybirthday(self):
		self.age +=1 
		print('I am', self.age)
	def eat(self):
		print('I am eating')

class Parent(Human):
	def work():
		print('I can work')
	def work(self):
		print(self.name,' can work')
	def eat(self):
		super().eat()
		print('It is apple')

class Child(Human):
	def happybirthday(self):
		self.age +=1 
		print('I am', self.age)
	def study(self):
		print(self.name,' can study')

obj = Child('Bob')
obj.study()
obj.live()
obj.happybirthday()
obj.happybirthday()
obj.happybirthday()
child1 = Child('Bob')

child1.study()
child1.live()
child1.happybirthday()
child1.happybirthday()
child1.happybirthday()

parent1 = Parent('Jane')
child1.eat()
parent1.eat()
parent1.work()
parent1.eat()
for i in range(30):
  parent1.happybirthday()'''



# Создать класс Животное. От него наследуются класс котик, собачка и хомяк.
# В классе животное есть 3 поля (характеристики) и 2 поведения (методы)
# В классах конкретных животных нужно добавить еще 1 поведение

class Animal:
  def __init__(self, name):
    self.name = name
    self.gender = 'None'
    self.age = 0
  def eat(self):
    print(self.name, "all eating")

  def sleep(self):
    print(self.name, "all sleeping")
    

class Dog(Animal):
  def playing(self):
    print(self.name, "is playing.")
    

class Cat(Animal):
  def runaway(self):
    print(self.name, "ran away for the whole day, but then returned.")


class Hampster(Animal):
  def running(self):
    print(self.name, "is running around at night, keeping everyone awake.")


obj1 = Dog('Fetch')
obj1.playing()
obj2 = Cat('Katt')
obj2.runaway()
obj3 = Hampster('Mr. Hamps')
obj3.running()
obj4 = Animal("They're")
obj4.eat()
obj4.sleep()