# #  მომხმარებელს შემოატანინეთ ტესტში მიღებული ქულა, თუ ქულა მეტია 90 - ზე და ნაკლებია 100 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა. თუ მიღებული 
# ქულა მეტია 70 - ზე და  ნაკლებია 80 - ზე მაგ შემთხვევაში დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით, თუ მიღებული ქულა მეტია 40 -  ზე და ნაკლებია 70 - ზე მაგ შემთხვევაში 
# # დაპრინტეთ, თქვენ დაგიფინანსდებათ სწავლა 500 ლარტით, ხოლო თუ მიღებული ქულა ნაკლებია 40 ზე, მაგ შემტხვევაში დაპრინტეთ, ტქვენ არ დაგიფინანსდებათ სწავლის პროცესი

score = int(input("how many points did you get in your test?: "))
if score > 90:
    print("your college has been financed fully succsesfully!")
elif score > 70:
    print(" your college has been financed with 1500 GEL")
elif score < 80:
    print(" your college has been financed with 1500 GEL")
elif score > 40:
    print(" your college has been financed with 500 GEL")
elif score < 70:
    print(" your college has been financed with 500 GEL")
elif score > 40:
    print("sorry your college has not been financed at all")