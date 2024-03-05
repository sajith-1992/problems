# to find min and max sum 
def miniMaxSum(arr):
    arr.sort()
    minimum_sum = sum(arr[:4])
    maximum_sum = sum(arr[1:]) 
    print(minimum_sum,maximum_sum)
      
  
miniMaxSum()