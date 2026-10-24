# how oops work? why we use it ?
English = int(input("what is your percentage out of 100 in english; " ))
PCP = int(input("what is your percentage out of 100 in planing a computing project: "))
Ai = int(input("what is your percentage out of 100 in Artificial Intelligence: "))
Programming = int(input("what is your percentage out of 100 in Programming: "))
networking = int(input("what is your percentage out of 100 in Networking:  "))
add = English + PCP +Ai+Programming +networking
print(add)
divide = add/500
print(divide)
percentage = divide* 100
print(percentage)
if percentage >=50 and percentage <60:
    print("Your result is D")
elif percentage >=60  and percentage < 70:
    print("your result is C")  
elif percentage >=70 and percentage < 80:
    print("your result is B")
elif percentage >= 80 and percentage < 90:
    print("your result is A ")
elif percentage >= 90 and percentage < 97 :
    print("your result is A+")
elif percentage >= 97 and  percentage <= 100:
    print("Congratulations! you are position holder student")    
else :
    print("you are Fail, you must work hard")