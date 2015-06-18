def manipulateNumbers(x,y):
  if x > y:
    ans = x + y
  elif x < y:
    ans = x - y
  else:
    ans = "error"
# Another way to account for all possible inputs.
# What happens if we input a string to this function?
# Will it work?
#  elif x == y:
#    ans = x*y
  return ans
  
print manipulateNumbers(1,2)
print manipulateNumbers(2,1)
# print manipulateNumbers(2,2)
# This will give us problems unless we make sure to account for it!
# To fix it we better make sure we account for the case x == y.
print manipulateNumbers(2,2)
