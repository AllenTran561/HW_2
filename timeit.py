import time

def calculate_time(func):
   def wrapper():
      start = time.time()
      temp = func()
      end = time.time()
      print("Total time " + str (start - end))
      return temp
   return wrapper
