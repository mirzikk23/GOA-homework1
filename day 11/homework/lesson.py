# მომხარებელს შემოატანინეთ მშობლების ასაკი, დედის და მამის ასაკი, შემდეგ თუ დედის ასაკი მეტი იქნება მამის ასაკზე
#დაგვიბეჭდოს რომ დედა დიდი მამაზე, თუ პირიქით მამის ასაკი მეტი იქნება დედის ასაკზე მაგ შემთხვევაში დაგვიბეჭდოს 
#რომ მამა დიდია დედაზე. მინიშნება დაგჭირდებათ (if)

moms_age = int(input("how old is is your mom?: " ))
dads_age = int(input("how old is your dad?: "))

if moms_age > dads_age:
    print("your mom is older than your dad")

if moms_age < dads_age:
    print("your dad is older than your mom")

if moms_age == dads_age:
    print("your dads age and your moms age equals")