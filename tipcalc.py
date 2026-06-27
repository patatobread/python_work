Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Welcome to calc")
... bill = float(input("What is the total bill? €"))
... tip = int(input("What percentage are you willing to tip? 10%, 12%, 15% "))
... people = int(input("How many people will split the bill? "))
... 
... if tip == 10:
...     result = bill * 0.1 + bill
... elif tip == 12:
...     result = bill * 0.12 + bill
... elif tip == 15:
...     result = bill * 0.15 + bill
... else:
...     result = bill
... 
... if people > 0:
...     final_bill = result / people
...     print("The total amount is:", result)
...     print("Each has to pay:", final_bill)
... else:
