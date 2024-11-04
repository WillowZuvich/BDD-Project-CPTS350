

from pyeda.inter import *

def int_to_bin(num):
    new_bin = ""
    i = 0
    while num > 0:
        if num % 2:
            new_bin += "1"
        else:
            new_bin += "0"
        num = int(num/2)
        i += 1
    if i < 5:
        while i < 5:
            new_bin += "0"
            i += 1
    new_bin = new_bin[::-1]
    return new_bin

x = bddvars('x', 5)
y = bddvars('y', 5)
z = bddvars('z', 5)  

#create RR bool formula and bdd
flag = 0
RR_expr = ""
for i in range(32):
    for j in range(32):
        if((((i+3) % 32) == (j % 32)) or (((i+8) % 32) == (j % 32))):
            i_str = int_to_bin(i)
            j_str = int_to_bin(j)
            
            RR_bool = ""
            a = 0
            m = 0
        
            for char in i_str:
                if char == "1":
                    RR_bool += f"x[{m}]" 
                else:
                    RR_bool += f"~x[{m}]"
                RR_bool += " & " 
                m += 1
            for char in j_str:
                if char == "1":
                    RR_bool += f"y[{a}]"
                else:
                    RR_bool += f"~y[{a}]"
                if a < 4:
                    RR_bool += " & "
                a += 1
            if flag != 0:
                RR_expr += " | "
            else:
                flag = 1
            RR_expr += RR_bool
            

RR_expr = expr(RR_expr)
RR = expr2bdd(RR_expr) 

test_27_3 = {x[0]: 1, x[1]: 1, x[2] : 0, x[3]: 1, x[4]: 1, y[0]: 0, y[1]: 0, y[2] : 0, y[3]: 1, y[4]: 1}
print("RR(27,3) is", bool(RR.restrict(test_27_3)))

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
    
