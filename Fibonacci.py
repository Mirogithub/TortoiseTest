def print_odds(reslist):

    countodds = []
    for i in reslist:
        if i % 2 != 0:
            countodds.append(i)
    countodds= len(countodds)
    countevens= len(reslist) - countodds
    print(f'In the Fibonacci list you have {countodds} odds and {countevens} even values')



def fibonacci(a):

    if type(a) != int or a < 1:
        return print("Please enter correct value!")

    for b in range(a):

        if (b == 0):
            prev1 = prev2 = 1;
            reslist = [prev1];
        else:
            res = prev1 + prev2
            prev1 = prev2
            prev2 = res

            if res > a:
                break
            reslist.append(res)
    # print(reslist)
    print_odds(reslist)


fibonacci(4000000)

# The comment to test Tortoise
# The comment to test Tortoise 2
