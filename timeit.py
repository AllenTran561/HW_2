import time

def calculate_time(func):
   def wrapper():
      func()
      print(time.time())
   return wrapper
