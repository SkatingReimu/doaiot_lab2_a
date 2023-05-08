def calc_bmi(h,w):
    bmi = w/(h*h)
    if bmi<18.5:
        return -1
    elif bmi>=18.5 and bmi<=25.0:
        return 0
    else:
        return 1


calc_bmi(h=1.73, w=57)
