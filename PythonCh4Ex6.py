#Brigham Holland Chapter 4 exercise 6

def computepay(hour_in, rate_in):
  hours = hour_in
  rate = rate_in
  if hours > 40:
    extra_time = hours - 40
  else:
    extra_time = 0

  extra_pay = 0.5 * rate * extra_time

  pay = hours * rate + extra_pay

  print ('Pay: '),  print (pay)

computepay(45,10)
