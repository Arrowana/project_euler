import math
import time

def problem_75_brute_force():
    """Given that L is the length of the wire, for how many values of L <= 1,500,000 can exactly one integer sided right angle triangle be formed? """

    #problem not solved
    for L in range(12, 15*10**5+1):
        #3 sides abc sorted by size
        #c as to be smaller than a+b
        #c = int(math.ceil(L/2)-1)
        formed = 0
        
        for c in range(L/3, int(math.ceil(L/2))):
            #a+b = L-c
            c_square = c**2
            for b in range(int(math.ceil((L-c)/2.0)), c+1):
                a = L-b-c
                if a**2+b**2 == c_square:
                    #print a,b,c
                    formed+=1
                    break

            #Get out of the loop if more than one found
            if formed > 1:
                break

        #If only one right triangle was formed
        if formed == 1:
            print "L: ", L

def problem_75_dichotomy():
    def pythagore_check(a, b, c_2):
        #return cosgamma
        #We only care about the sign the the extra division can be removed /(2.0*a*b) 
        return (a**2+b**2-c_2) 

    right_triangles = 0

    for L in range(12, 15*10**5+1):
        if L%2 != 0:
            continue
        #3 sides abc sorted by size
        #c as to be smaller than a+b
        formed = 0
        
        c_min = L/3
        c_max = int(math.ceil(L/2))
        c_range = range(c_min, c_max)        

        for c in c_range:
            #a+b = L-c
            c_square = c**2
            b_min = int(math.ceil((L-c)/2.0))
            b_max = c

            cosgamma_min = pythagore_check(L-b_min-c, b_min, c_square)
            cosgamma_max = pythagore_check(L-b_max-c, b_max, c_square)

            #Check if there is potentially a solution
            if cosgamma_min*cosgamma_max <= 0:
                """ok"""
                #Dichotomy using al kashi theorem as f(x)        
                x_1 = b_min
                x_2 = b_max
                x_m = 0
                no_sol = 0

                for i in range(1000):
                    x_m = (x_1+x_2)/2
                    f_x_1 = pythagore_check(L-x_1-c, x_1, c_square)
                    f_m = pythagore_check(L-x_m-c, x_m, c_square)

                    #print L, ":"
                    #print f_x_1, f_m
                    #print x_m, x_1, x_2
                    #print "abc", L-x_m-c, x_m, c
                    if f_m == 0.0:
                        formed += 1
                        break
                    elif x_1 == x_m:
                        break
                    elif f_m*f_x_1 > 0.0:
                        #No solution we change the interval
                        x_1 = x_m
                        no_sol += 1
                        if no_sol == 2:
                            break
                    else:
                        x_2 = x_m
                        no_sol = 0

            #If we formed more than 1 triangle the triangle is rejected
            if formed > 1:
                break
        
        if formed == 1:
            print "L:", L, "forms only one triangle"
            right_triangles+=1

    print right_triangles
       
def problem_75_polynome():
    def solve_triangle(c, L):
        # b**2 + (c-L)*b + L(L/2-c)=0
        # obviously if L%2 != 0 we have no solution
        # because the square of an odd number is odd
        delta = (c-L)**2 - 2*L*(L-2*c)
        
        if delta == 0:
            sol = (L-c)/2.0
            return [sol]
        elif delta > 0:
            delta_sqrt = math.sqrt(delta)
            sol1 = ((L-c)+delta_sqrt)/2.0
            sol2 = ((L-c)-delta_sqrt)/2.0
            return [sol1, sol2]
        else:
            return []

    formed_one_right_only = 0
    two_solutions_list = []
    start = time.time()

    for L in range(12, 15*10**5+1):
        #Sol found for this length
        first_sol = False
        two_solutions = False

        #Only even length have solutions
        if L%2 != 0:
            continue
        
        #Check if the solution is a multiple of a solution previously encountered
        for previous_multi_sol in two_solutions_list:
            if L % previous_multi_sol == 0:
                #print "found previously"
                continue
        
        #L/3+1 min possible of c
        #If we had the condition to get delta posivive we get
        #c > (math.sqrt(8)/2.0-1)*L
        for c in range(int((math.sqrt(8)/2.0-1)*L)+1, L-1):
            sols = solve_triangle(c,L)
            for sol in sols:
                if (sol).is_integer():
                    b = int(sol) 
                    a = L-b-c
                    if b-a > 0 and a > 0 and sol > 1 and sol < c:
                        #print "L:", L
                        #print "sol found", "a:", L-b-c, "b:", b, "c:", c
                        if first_sol:
                            two_solutions = True
                            break
                        else:
                            first_sol = True

            #Stop iterating c because we have at least two solutions
            if two_solutions:
                break            
                
        #If L divisible by 100 we print L to track progress
        if L % 1000 == 0:
            print "L:", L
            print formed_one_right_only
            now = time.time()
            print now - start
            start = now

        if two_solutions:
            two_solutions_list.append(L)
            continue
        elif first_sol:
            #print L
            formed_one_right_only += 1
            #print "one sol only"

    print formed_one_right_only 
               
def problem_112():
    """Bouncy numbers"""
    def bounciness(number):
        digits = [int(nb_str) for nb_str in str(number)] 
        digits.append(digits[-1])
        digit_p = digits[0] 
        delta_p = 0
        bounced = -1

        for i, digit in enumerate(digits):
            delta = digit-digit_p

            if delta*delta_p < 0:
                #Bounciness detected return index
                bounced = i    
                break
                
            delta_p = delta 
            digit_p = digit

        return bounced

    bouncy_nbs = 0

    for i in range(100, 548):
        print i, bounciness(i)

        if bounciness(i) > 0:
            #All other number starting with this bouncy sequence are bouncy too
            bouncy_nbs+=1
            perc = 100.0*bouncy_nbs/i 
            print perc
            if perc >= 99.0:
                break
            
def problem_206():
    lower = int(math.sqrt(1020304050607080900))
    upper = int(math.sqrt(1929394959697989990))

    def match_pattern(number):
        number_str = str(number)
        selected_digits = [int(number_str[i]) for i in range(0, len(number_str), 2)]

        for i, digit in zip(range(1, len(selected_digits))+ [0], selected_digits):
            if i == int(digit):
                continue
            else:
                return False

        return True

    lower_square = lower**2
    square_last = lower_square

    i = 0
    while i < upper-lower:
        i+=1
 
        square = square_last + 2*(lower)+1
        print square

        if i % 10 != 0:
            continue
        if match_pattern(square):
            print "found"
            break

        square_last = square

def problem_XX():
    def p(nb):
        stop = nb/2
        prime = True
        for k in range(2, stop):
            if nb % k == 0:
                print "divisible by", k
                prime = False
                break
        return prime

    def b(nb):
        k=2
        while k < nb/2:
            if nb % k == 0:
                if p(k):
                    print "biggest prime divisor", k
                else:
                    print "not", k
            if k % 100 == 0:
                print k

            k+=2

        return k
                
    #Target 600851475143
    print b(600851475143)

if __name__ == '__main__':
    print problem_206()

