#2) კომენტარებით ახსენით რა არის sequences, iteration და selection. მოიყვანეთ მათი მაგალითები

#Sequences aris magalitad tanimdevroba magalitad ragaceebis shesruleba mimdevrobit

#Iteration aris gameoreba ragacis mrvaljer shesruleba

#selection aris ragacis archeva

#3) კომენტარებით ახსენით, რა არის ალგორითმი და ჩამოთვალეთ რა გზები არსებობს მის წარმოსადგენად.

#algoritmi gamoiyeneba imashi rom amocanebi da problemebi gadavchrat. algoritmi yoveltvis iwyeba da mtavrdeba aseve unda iyos zusti pasuxi da unda sruldebodes saboloo shedegamde



#4) შეეცადეთ თქვენით მიხვდეთ, თუ რა პასუხს გამოიტანს შემდეგი კოდი:

#print(True or False and False or True and False or False and False or False and True and False or True)
#print(5 > 10 or 7 * 7 / 7 == 7 and False or True and "1234" != "1234" and 7 + 3 * 3 + 1 == 15 and True and True or 100 > 100 or True)

print(True or False and False or True and False or False and False or False and True and False or True)

#orive gamoitans trues magram meore upro martivi da swori pormit aris

#პირველ რიგში დაუყევით and ლოგიკურ ოპერატორებს, შემდეგ კი დარჩენილ or ოპერატორებს

#5) მომხმარებელს შემოატანინეთ რიცხვი და თუ ის არის ლუწი და არის 10-ზე მეტი, ან ტოლია 7-ის, დაბეჭდეთ True

num1 = int(input("Enter a number: "))
if (num1 % 2 == 0 and num1 > 10) or num1 == 7:
    print(True)
#6) ივარჯიშეთ შემდეგ ფუნქციებზე: int, str, float, bool. თითოეულზე გააკეთეთ 3-3 მაგალითი

print(5+5)    
print(5+10)
print(5+15)


name = "gio"
name = "lasha"
name = "nika"


print(5.1+7.3)
print(10.1+20.2)
print(12.2+11.1)


x = 7
y = 8

print(x < y)
print(x == y)
print(x > y)

#7) მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ, თუ ის არის ნაკიანი დაბეჭდეთ "This is leap year".(ნაკიანი წელიწადი იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე)

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is leap year")
