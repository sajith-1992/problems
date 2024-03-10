def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    result=[]
    for i in candies:
        if i + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result

def main():
    candies = [1, 2, 3]
    extra_candies = 2
    result = kidsWithCandies(candies, extra_candies)
    print(result)

main()
#time complesity o(n)
#space complesity is o(1)