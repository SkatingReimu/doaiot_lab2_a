def calc_bmi(h,w):
    print("height = "+str(h))
    print("weight = "+str(w))
    bmi = w/(h*h)
    print("your bmi is: "+str(bmi))
    if bmi<18.5:
        print("you are underweight")
        return -1
    elif bmi>=18.5 and bmi<=25.0:
        print("your weight is normal")
        return 0
    else:
        print("you are overweight")
        return 1


calc_bmi(h=1.73, w=57)