#!/usr/bin/env python3

def print_fibonacci(length):
     if length == 0:
          print([])
     elif length == 1:
          print([0])
     else:
          fibonacci_seq = [0,1]

          while len(fibonacci_seq) < length: 
               next_number = fibonacci_seq[-1] + fibonacci_seq[-2]
               fibonacci_seq.append(next_number)

          print(fibonacci_seq)
     
   
        

try: 
    result = print_fibonacci(0)
    print(result)
    print("Test passed")
except:
    print("Error in Calculation")

try: 
    result = print_fibonacci(1)
    print(result)
    print("Test passed")
except:
    print("Error in Calculation")



try: 
    result = print_fibonacci(2)
    print(result)
    print("Test passed")
except:
    print("Error in Calculation")


try: 
    result = print_fibonacci(3)
    print(result)
    print("Test passed")
except:
    print("Error in Calculation")

try: 
    result = print_fibonacci(4)
    print(result)
    print("Test passed")
except:
    print("Error in Calculation")

try: 
    result = print_fibonacci(5)
    print(result)
    print("Test passed")
except:
    print("Error in Calculation")

try: 
    result = print_fibonacci(6)
    print(result)
    print("Test passed")
except:
    print("Error in Calculation")

try: 
    result = print_fibonacci(7)
    print(result)
    print("Test passed")
except:
    print("Error in Calculation")

try: 
    result = print_fibonacci(8)
    print(result)
    print("Test passed")
except:
    print("Error in Calculation")
    
try: 
    result = print_fibonacci(9)
    print(result)
    print("Test passed")
except:
    print("Error in Calculation")

try: 
    result = print_fibonacci(10)
    print(result)
    print("Test passed")
except:
    print("Error in Calculation")


   

