def canPlaceFlowers(flowerbed,n):
        i=0
        count=0
        lenbed = len(flowerbed)
        while i<lenbed:
            if(flowerbed[i]==0)and (i==0 or flowerbed[i-1]==0)and (i==(lenbed-1) or flowerbed[i+1]==0):
              flowerbed[i]=1
              count+=1
            i+=1
        if count>=n:
             print(True)
        else:
             print(False)    
def main():
    flowerbed=[0,1,0,0,0,1]
    n=1
    canPlaceFlowers(flowerbed,n)
main()