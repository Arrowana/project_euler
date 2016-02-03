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
               
def problem_62():
    """Find smallest cube for which exactly five permutations of its digits are cube"""
    def identify(number):
        return "".join(sorted(str(number)))

    cubes = [['1', 1]]
    
    for i in range(2, 10000):
        identity = identify(i**3)
        matched = False 
        found = False

        for group in cubes:
            if group[0] == identity:
                group.append(i)
                matched = True
                if len(group) == 6:
                    found = True
                    print i
                    winner = group
                break
        
        if matched == False:
            cubes.append([identity, i])
        
        if found:
            break

    print winner
    return (winner[1])**3

if __name__ == '__main__':
    print problem_62()

