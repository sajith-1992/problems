import math

def gcdOfStrings(str1 , str2 ):

    
    len1 =len(str1)
    len2 = len(str2)
    min_len = min(len1,len2)
  
    for i in range(min_len,0,-1):
        if len1 % i == 0 and len2 % i == 0:
            new = i
            break
    str_new = str1[:new]
    
    if str_new * (len1//new) == str1 and str_new * (len2//new) == str2:
        return str_new
    else:
        return""
def main():
    gcdOfStrings("hai","haihaihai")
main()