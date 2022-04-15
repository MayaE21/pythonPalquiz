

def evenfibonaccinumbers(efn):

    if efn <= 0:
        print("0,2,4,6,8,10,12,14,")

    elif efn == 1:
        return 0

    elif efn == 2:
        return 1

    else:
        return evenfibonaccinumbers(efn - 1) + 2evenfibonaccinumbers(efn - 2)

    print(evenfibonaccinumbers(15))



