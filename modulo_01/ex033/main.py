nmr1=float(input('digite um numero'))
nmr2=float(input('digite outro'))
nmr3=float(input('digite mais um'))

if nmr1 > nmr2:
    if nmr1 > nmr3:
        print(nmr1)
    else:
        print(nmr2)
else:
    if nmr2 > nmr3:
        print(nmr2)
    else:
        print(nmr3)