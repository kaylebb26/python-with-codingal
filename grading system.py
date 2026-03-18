print("enteryour marks 5 subjects: ")
m=int(input("maths: "))
h=int(input("history: "))
e=int(input("english: "))
s=int(input("science: "))
cs=int(input("computer science: "))
total=m+h+e+s+cs
print("total marks: ",total)
average=total/5
print("average marks: ",average)
if average>=90:
    print("grade: A")
elif average>=80:
    print("grade: B")
else:
    print("grade: C")
    