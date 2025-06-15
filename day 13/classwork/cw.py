#1)  მომხმარებელს შემოატანინეთ თავისი გულის ცემა გააკეთეთ პატარა გულის ცემის სისტემა რომელიც ითვლის რა თქმა უნდა გულის ცემას  თუ 180 ზე მეტია ამ შემთხვევაში მაღალია თუ 160-დან 170 მდე არის ამ შემთვევაში არის ნორმალური თუ 160-ზე ნაკლებია ამ შემთხვევაში დაბალია 


heart_rate = int(input("Enter your heart rate: "))

if heart_rate > 180:
    print("High heart rate")
elif 160 <= heart_rate <= 170:
    print("Normal heart rate")
elif heart_rate < 160:
    print("Low heart rate")








#2)შექმენი პროგრამა, რომელიც მომხმარებლის მიერ შეყვანილი ასაკის მიხედვით დაადგენს, რომელი ასაკობრივი ჯგუფის წევრია ადამიანი.

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")
