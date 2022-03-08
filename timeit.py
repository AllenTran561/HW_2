import time

def calculate_time(func):
   func()
   return int (time.time())
