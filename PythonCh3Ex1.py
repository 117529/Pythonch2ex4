#Brigham Holland Chapter 3 exercise 1
hours = 45
rate = 10
if hours >= 40 :
  extra_time = hours - 40
else: 
    extra_time = 0

extra_pay = 0.5 * rate * extra_time

pay = hours * rate + extra_pay
print (pay)

