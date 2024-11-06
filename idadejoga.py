anos=int(input("Digite a sua idade"))
if anos<=0 or anos>=60:
    print("idade invalida")
elif anos<10:
    print("infantis")
elif anos>=10 and anos<14:
    print("iniciados")
elif anos>=14 and anos<18:
    print("juniores")
else:
    print("seniores")