import time

def calculate_time(func):
   def wrapper():
      start = time.time()
      func()
      end = time.time()
      print("Total time " + start - end)
   return wrapper
