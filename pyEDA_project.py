

from pyeda.inter import *

#convert integer to 5 bit binary rep
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
#end in_to_bin()

#checks if prime
def is_prime(num):
    if num == 2:
        return False
    for i in range(2, (num//2) +1):
        if((i % num) == 0):
            return False
    else: 
        return True
#end of is_prime()


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
test_16_20 = {x[0]: 1, x[1]: 0, x[2] : 0, x[3]: 0, x[4]: 0, y[0]: 1, y[1]: 0, y[2] : 1, y[3]: 0, y[4]: 0}

print("RR(27,3) is", bool(RR.restrict(test_27_3)))
print("RR(16,20) is", bool(RR.restrict(test_16_20)))

#create even bool formula  and bdd 
even_bool = ~y[4]
EVEN = expr2bdd(even_bool)

test_14 = {y[0]: 0, y[1]: 1, y[2] : 1, y[3]: 1, y[4]: 0}
test_13 = {y[0]: 0, y[1]: 1, y[2] : 1, y[3]: 1, y[4]: 1}


print("EVEN(14) is", bool(EVEN.restrict(test_14)))
print("EVEN(13) is", bool(EVEN.restrict(test_13)))

#create prime bool formula
flag = 0
prime_expr = ""
for i in range(32):
    if(is_prime(i)):
        i_str = int_to_bin(i)

        prime_bool = ""
        m = 0
        
        for char in i_str:
            if char == "1":
                prime_bool += f"x[{m}]" 
            else:
                prime_bool += f"~x[{m}]"
            if(m < 4):
                prime_bool += " & " 
            m += 1
        
        if flag != 0:
            prime_expr += " | "
        else:
            flag = 1
        prime_expr += prime_bool

prime_expr = expr(prime_expr)
PRIME = expr2bdd(prime_expr)

test_7 = {x[0]: 0, x[1]: 0, x[2] : 1, x[3]: 1, x[4]: 1}
test_2 = {x[0]: 0, x[1]: 0, x[2] : 0, x[3]: 1, x[4]: 0}

print("PRIME(7) is", bool(PRIME.restrict(test_7)))
print("PRIME(2) is", bool(PRIME.restrict(test_2)))

#create RR2 bool formula and bdd
y_to_z = {y[0] : z[0], y[1] : z[1], y[2] : z[2], y[3] : z[3], y[4] : z[4]}
x_to_z = {x[0] : z[0], x[1] : z[1], x[2] : z[2], x[3] : z[3], x[4] : z[4]}

RR2 = (RR.compose(y_to_z) & RR.compose(x_to_z))

RR2.smoothing(z)
                                                         
test_27_6 = {x[0]: 1, x[1]: 1, x[2] : 0, x[3]: 1, x[4]: 1, y[0]: 0, y[1]: 0, y[2] : 1, y[3]: 1, y[4]: 0}
test_27_9 = {x[0]: 1, x[1]: 1, x[2] : 0, x[3]: 1, x[4]: 1, y[0]: 0, y[1]: 1, y[2] : 0, y[3]: 0, y[4]: 1}

print("RR2(27,6) is", bool(RR2.restrict(test_27_6)))
print("RR2(27,9) is", bool(RR2.restrict(test_27_9)))
                                                        

#create RR2star formula and bdd

#create StatementA bool formula and bdd
    
