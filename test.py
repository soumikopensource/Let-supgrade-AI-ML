



def print_prime(numbers):
    
        if numbers>2:
            for i in range(2,numbers):
                if numbers%i==0:
                    break
            
            else:
                return True
                

x = 2
count = 0

while count < 20:
    
    if print_prime(x)==True:
        print(x)
        count+=1
    x+=1
        
   
     
    
     

    
