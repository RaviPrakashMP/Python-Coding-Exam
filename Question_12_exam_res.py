Eng = int(input("Enter the marks scored in English:"))
Sci_Th = int(input("Enter the marks scored in Science Theory:"))
Sci_pra = int(input("Enter the marks scored in Science Practical:"))
Sci = Sci_Th + Sci_pra
Mat = int(input("Enter the marks scored in Mathematics:"))

Total = ((Eng + Sci + Mat)/275)*100

if Sci_Th < 25:
    print("The student has failed")

elif Sci_pra < 8:
    print("The student has failed")

elif Eng < 25:
    print("The student has failed")

elif Mat < 35:
    print("The student has failed")
    
    
elif Total > 90:
    print("The student has scored Grade A")

elif 75 < Total < 90:
    print("The student has scored Grade B")

elif 35 < Total < 75:
    print("The student has scored average Grade")

elif total < 35:
    print("The student has failed")
    
