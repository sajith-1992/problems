# to find min and max sum 
def miniMaxSum(arr):
    arr.sort()
    minimumsum = sum(arr[:4])
    maximumsum = sum(arr[1:])
    print(minimumsum)
    print(maximumsum)
def main():
  arr=[1,2,3,4,5]
  miniMaxSum(arr)
  
main()