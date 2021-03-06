import csv
filename = open('Student_marks_listt.csv', 'r')
file = csv.DictReader(filename)
  
name = []
maths = []
bio=[]
eng=[]
phy=[]
chem=[]
hindi=[]


for col in file:
    name.append(col['Name'])
    maths.append(col['Maths'])
    bio.append(col['Biology'])
    eng.append(col['English'])
    phy.append(col['Physics'])
    chem.append(col['Chemistry'])
    hindi.append(col['Hindi'])

maths = [int(marks) for marks in maths]
bio = [int(marks) for marks in bio]
eng = [int(marks) for marks in eng]
phy = [int(marks) for marks in phy]
chem = [int(marks) for marks in chem]
hindi = [int(marks) for marks in hindi]


print('Topper in Maths is',name[maths.index(max(maths))])
print('Topper in Biology is',name[bio.index(max(bio))])
print('Topper in English is',name[eng.index(max(eng))])
print('Topper in Physics is',name[phy.index(max(phy))])
print('Topper in Chemistry is',name[chem.index(max(chem))])
print('Topper in Hindi is',name[hindi.index(max(hindi))])

total={}
toppers=[]
for i in range(len(name)):
    tot=maths[i]+bio[i]+eng[i]+phy[i]+chem[i]+hindi[i]
    total[name[i]]=tot
for i in range(3):
    maxtotal = max(total, key=total.get)
    toppers.append(maxtotal)
    del total[maxtotal]
print('Best students in the class are',toppers[0],'first rank, ',toppers[1],'second rank, ',toppers[2],'third rank')
