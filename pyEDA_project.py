

from pyeda.inter import *



x = bddvars('x', 5)
y = bddvars('y', 5)
z = bddvars('z', 5)  

#create RR bool formula and bdd

#create even bool formula  and bdd 
even_bool = ~x[4]
EVEN = expr2bdd(even_bool)

test_14 = {x[0]: 0, x[1]: 1, x[2] : 1, x[3]: 1, x[4]: 0}
test_13 = {x[0]: 0, x[1]: 1, x[2] : 1, x[3]: 1, x[4]: 1}


print("EVEN(14) is", bool(EVEN.restrict(test_14)))
print("EVEN(13) is", bool(EVEN.restrict(test_13)))

#create prime bool formula 

#create RR2 bool formula and bdd

#create RR2star formula and bdd

#create StatementA bool formula and bdd
    
