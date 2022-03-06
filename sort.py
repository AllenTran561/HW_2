def sort_list(myList):
   n = len(myList)
   i = 0
   while i < n:
      j = n - i - 1
      while j < n - 1:
         if myList[j] > myList[j + 1]:
            temp = myList[j + 1]
            myList[j + 1] = myList[j]
            myList[j] = temp
         j += 1
      i += 1
   return myList
