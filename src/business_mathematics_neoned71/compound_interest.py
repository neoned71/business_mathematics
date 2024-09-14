


def interest_amount(p,r,t,n):
    return final_amount(p,r,t) - p

def final_amount(p,r,t,n):
    return p*((1+r/n)**(t*n))

def reverse_P_from_FA(fa,r,t,n):
    return fa/((1+))

def reverse_R_from_FA(fa,p,t):
    return (fa-p)/(p*t)


def reverse_T_from_FA(fa,p,r):
    return (fa-p)/(p*r)


