# მოსწავლეს შემოატანინეთ სკოლის ტესტში მიღებული ნიშანი, თუ ეს მიღებული ნიშანი
# უდრის 10 - ს, მაგ შემთხვევაში მასწავლებელმა, მშობელთან შეაქოს მოსწავლე, თუ მიღებული
# ნიშანი უდრის 8 -ს ან 9 - ს, მაგ შემთხვევაში, მასწავლებელმა, მშობელს პატარა შენიშვნა მისცეს.
# თუ მიღებული ქულა უდრის 5  - ს მაგ შემთხვევაში, მასწავლებელმა, მშობელს მისცეს შენიშვნა, ხოლო თუ მიღებული
# ნიშანი ნაკლებია 5 ზე, მაგ შემთხვევაში, მასწავლებელმა გააგდოს მოსწავლე სკოლიდან

name = input("ra gkvia?: ")
test = int(input("ra miige testshi?: "))
if test == 10:
    print("yochag " + name + " shen namdvilad shesanishnavi bavshvi xar!!!")
if test == 9:
    print("shen dzalian kargia bavshvi xar " + name + "mcire xarvezebit")
if test == 8 or 7:
    print("damakmayofilebelia magram meti!!!")
if test == 5:
    print("swavla ertad unda amovkachot radgan araris 5-iani kargi nishani!")
if test < 5:
    print("shen samwuxarod gamocdashi migebuli cudi nishnia gamo garicxuli xar skolidan")