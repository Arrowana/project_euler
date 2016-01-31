
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
       
def problem_75():
    problem_75_dichotomy()
