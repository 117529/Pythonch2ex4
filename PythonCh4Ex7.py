#Brigham Holland - Python Chapter 4 - Exercise 7
Grade = 0
def computergrade(Grade):
  error_msg_invalid = ('Wrong Input')
  Grade = input('What is the grade?')
  while True:
    try:
      if (float(Grade) >= 0) and ( float(Grade) <= 1 ):
        print('valid input, thanks!')
      else: 
        print (error_msg_invalid)
      Grade = input('What is the grade?')
    except: 
      print (error_msg_invalid)
      Grade = input('What is the grade?')
    Grade = float(Grade) 
    if Grade < 0.6 :
      print ('F')
    elif Grade < .7 :
      print ('D')
    elif Grade < .8 :
      print ('C')
    elif Grade < .9 :
      print ('B')
    elif Grade < 1 :
      print ('A')
computergrade(Grade)
exit()
