import time

# декоратор в виде класса
class Time_this:
	def __init__(self, func):
		self.num_runs = 10
		self.func = func

	def __call__(self):
		avg_time = 0
		for _ in range(self.num_runs):
			t0 = time.time()
			self.func()
			t1 = time.time()
			avg_time += (t1 - t0)
		avg_time /= self.num_runs
		print("Декоратор-класс: среднее время выполнения функции %.5f секунд" % avg_time)
		return self.func()

@Time_this
def f():
	for j in range(1000000):
		pass

f()


# декоратор в виде функции
def time_this(num_runs):
	def decorator(func):
		avg_time = 0
		for _ in range(num_runs):
			t0 = time.time()
			func()
			t1 = time.time()
			avg_time += (t1 - t0)
		avg_time /= num_runs
		print("Декоратор-функция: среднее время выполнения функции %.5f секунд" % avg_time)
	return decorator

@time_this(num_runs=10)
def f():
	for j in range(1000000):
		pass