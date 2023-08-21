#!/usr/bin/env python3

def print_fibonacci(length):
     if length == 0:
          print([])
     elif length == 1:
          print([0])
     else:
          fibonacci_seq = [0, 1]

          for _ in range(2, length):
               next_number = fibonacci_seq[-1] + fibonacci_seq[-2]
               fibonacci_seq.append(next_number)
               print(fibonacci_seq)
        
try: 
     print_fibonacci(0)
except Exception as e:
    print (e)

try: 
     print_fibonacci(1)
except Exception as e:
    print (e)

try: 
     print_fibonacci(2)
except Exception as e:
    print (e)

try: 
     print_fibonacci(3)
except Exception as e:
    print (e)

try: 
     print_fibonacci(4)
except Exception as e:
    print (e)

try: 
     print_fibonacci(5)
except Exception as e:
    print (e)

try: 
     print_fibonacci(6)
except Exception as e:
    print (e)

try: 
     print_fibonacci(7)
except Exception as e:
    print (e)


   
  