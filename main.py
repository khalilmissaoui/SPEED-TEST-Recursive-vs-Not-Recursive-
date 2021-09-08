# Python3 program to compute 
# exponential value 
# using (2^k) -ary method.
import time
  
# prime modulo value
N = 1000000007; 
  
def exponentiation1(bas, exp):
    t = 1;
    while(exp > 0): 
  
        # for cases where exponent
        # is not an even value
        if (exp % 2 != 0):
            t = (t * bas) % N;
  
        bas = (bas * bas) % N;
        exp = int(exp / 2);
    return t % N;
  

def exponentiation(bas, exp , t) :
    if(exp <= 0):
        return t % N ;
    if(exp % 2 != 0):
        return exponentiation (bas * bas % N , int(exp / 2) , (t * bas) % N);
    else:
        return exponentiation (bas * bas % N , int(exp / 2)  , t );
        
    
# Driver Code 
bas = 5;
exp = 100000;
  
start = time.time()
modulo = (bas ** exp) % N;
end = time.time()

print("Slow Method: Answer: {} Time (s): {}: ".format(modulo, end - start));

start = time.time()
modulo = exponentiation1(bas,exp);
end = time.time()

print("Fast Method: NOT Recursive Method : {} Time (s): {}: ".format(modulo, end - start));

start = time.time()
modulo = exponentiation(bas,exp,1);
end = time.time()

print("Fast Method: Recursive Method : {} Time (s): {}: ".format(modulo, end - start));





