# if elif else statement

# show ticket pricing
# age: 0 to 3 -> free
# age: 4 to 10 -> ticket price: 150 taka
# age: 11 to 60 -> ticket price: 250 taka
# age: above -> ticket price: 200 taka

age = int(input("Enter your age: "))

if(age==0):
    print("You are not eligible")
elif(0<age<=3):
    print("Ticket is free")
elif(age>=4 and age<=10):
    print("Ticket price is 150 taka only")
elif(age>=11 and age<=60):
    print("Ticket price is 250 taka only")
else:
    print("Ticket price is 200 taka only")
