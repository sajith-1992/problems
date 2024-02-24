# GIVEN:
# ARR[]

# TO FIND
#RATIO  OF +VE,-VE,0 .6 DECIMAL places


def main():
    arr=[1,-2,3,0,4,7]
    
    ratio(arr)


def ratio(arr):
    totalNumber=len(arr)
    print(totalNumber)
    positiveNumber=0

    positiveNumber=sum(1 for num in arr if num>0)
    print(positiveNumber)
    negativeNumber=0

    negativeNumber=sum(1 for num in  arr if num<0)
    print(negativeNumber)
    zeroNumbers=0

    zeroNumbers=totalNumber-positiveNumber-negativeNumber
    print(zeroNumbers)


    positiveNumberRatio=print( "positive number"  "{:.6f}".format(positiveNumber/totalNumber))

  
    negativeNumberRatio=print("negative number :" "{:.6f}".format(negativeNumber/totalNumber))
    
    zeroNumbersRatio=print("zero number:" "{:.6f}".format(zeroNumbers/totalNumber))

