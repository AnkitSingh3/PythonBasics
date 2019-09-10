def is_Prime_number(num):
    a = int(num/2);
    for i in range(2,a+1):
        if num % i == 0:
          return 'number is not prime'
    return "number is prime"

print(is_Prime_number(101) )