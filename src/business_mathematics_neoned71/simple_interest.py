


def simple_interest_I(p,r,t):
    return p*r*t

def simple_interest_FA(p,r,t):
    return p+simple_interst_I(p,r,t)

def simple_interest_reverse_P_from_FA(fa,r,t):
    return fa/(1+t*r)

def simple_interest_reverse_R_from_FA(fa,p,t):
    return (fa-p)/(p*t)


def simple_interest_reverse_T_from_FA(fa,p,r):
    return (fa-p)/(p*r)


