import time

# декоратор в виде класса
class Time_this:
	def __init__(self, num_runs):
		self.num_runs = num_runs

	def __call__(self, func):
		avg_time = 0
		for _ in range(self.num_runs):
			t0 = time.time()
			func()
			t1 = time.time()
			avg_time += (t1 - t0)
		avg_time /= self.num_runs
		print("Декоратор-класс: среднее время выполнения функции %.5f секунд" % avg_time)
		return func()

	def __enter__(self):
		self.num_runs = 1
		self.start = time.time()

	def __exit__(self, *args):
		avg_time = (time.time() - self.start) / self.num_runs
		print("Контекстный менеджер: среднее время выполнения функции %.5f секунд" % avg_time)

@Time_this(10)
def f():
	for j in range(1000000):
		pass


def f2():
	for j in range(1000000):
		pass

# использование декоратор в виде контекстного менеджера
with Time_this(10) as t:
	f2()


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

@time_this(10)
def f():
	for j in range(1000000):
		pass