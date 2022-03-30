import random


def spin_ball():
    spin = str(random.randint(35, 36))
    if spin == "37":
        print(f"The ball spin is : 00")
        return("00")
    else:
        print(f"The ball spin is : {spin}")
        return(spin)
