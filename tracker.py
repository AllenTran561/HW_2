def func_counter(func):
   def wrapper(x):
      wrapper.counter += 1
      return func(x)
   wrapper.counter = 0
   return wrapper
