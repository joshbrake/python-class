# Example function: add numbers
test = 2 # Example global variable
def addNumbers(num1,num2):
  sum = num1 + num2 + test # num1 and num2 are local variables.
  return sum
    
# Now let's call the function to add the two numbers
print addNumbers(1,2)
    