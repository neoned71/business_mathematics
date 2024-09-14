
# Total interest accrued
def interest_amount(p,r,t):
    return p*r*t

# Total amount at the end of term
def final_amount(p,r,t):
    return p+interest_amount(p,r,t)

# Get the principal value from the final amount, rate of interest and time
def reverse_P_from_FA(fa,r,t):
    return fa/(1+t*r)

# Get the rate of interest from the final amount, principal value and time
def reverse_R_from_FA(fa,p,t):
    return (fa-p)/(p*t)

# Get the time from the final amount, rate of interest and principal value
def reverse_T_from_FA(fa,p,r):
    return (fa-p)/(p*r)


