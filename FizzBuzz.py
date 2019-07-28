def fizzbuzz(n): 
  result = []
  for count in range (1, n):
    if count % 3 == 0 and not count % 5 == 0:
      result.append("Fizz")
    elif count % 5 == 0 and not count % 3 == 0:
      result.append("Buzz")
    elif count % 3 == 0 and count % 5 == 0:
      result.append("FizzBuzz")
    else:
      result.append(count)
  return result

