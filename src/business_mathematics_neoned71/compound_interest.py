import math

# Total amount at the end of term
def final_amount(p,r,t,n=1):
    return p*((1+r/n)**(t*n))

# names of the function should be sufficient in describing what the function does.
def interest_amount(p,r,t,n=1):
    return (final_amount(p,r,t,n) - p)

# Get the principal value from the final amount, rate of interest and time
def reverse_P_from_FA(fa,r,t,n=1):
    return fa/((1+r/n)**(t*n))

# Get the rate of interest from the final amount, principal value and time
def reverse_R_from_FA(fa,p,t,n=1):
    return n*((fa/p)**(1/(n*t))-1)

# Get the time from the final amount, rate of interest and principal value
def reverse_T_from_FA(fa,p,r,n=1):
    return (1/n)*math.log(fa/p)/math.log(1+r/n)


