import math

def Newton (f, fder, x0, epsilon, Nitermax) :
    n = 1
    xold = x0
    xnew = xold-(f(xold)/fder(xold))
    delta = xnew-xold
    
    while abs(delta) > epsilon and n < Nitermax :
        xnew = xold-(f(xold)/fder(xold))
        n += 1
        delta = xnew - xold
        xold = xnew
        print (xnew, n, delta)
    
    return print('===>','alpha = ',xnew ,'N = ',n)




#========== Fonction 1: ==========

def f1(x):
    return x**4+3*x-9

def f1der(x):
    return 4*x**3+3

print('========== Fonction 1: ==========\n')
Newton(f1,f1der,-2,1e-5,20)
Newton(f1,f1der,2,1e-5,20),print('\n\n')




#========== Fonction 2: ==========

def f2(x):
    return 3*math.cos(x)-2-x

def f2der(x):
    return -3*math.sin(x)-1

print('========== Fonction 2: ==========\n')
Newton(f2,f2der,-5,1e-5,20)
Newton(f2,f2der,-1,1e-5,20)
Newton(f2,f2der,0,1e-5,20),print('\n\n')




#========== Fonction 3: ==========

def f3(x):
    return x*math.exp(x)-7

def f3der(x):
    return math.exp(x)+x*math.exp(x)

print('========== Fonction 3: ==========\n')
Newton(f3,f3der,7,1e-5,20),print('\n\n')




#========== Fonction 4: ==========

def f4(x):
    return math.exp(x)-x-10

def f4der(x):
    return math.exp(x)-1

print('========== Fonction 4: ==========\n')
Newton(f4,f4der,-10,1e-5,20)
Newton(f4,f4der,3,1e-5,20),print('\n\n')




#========== Fonction 5: ==========

def f5(x):
    return 2*math.tan(x)-x-5

def f5der(x):
    return 2/((math.cos(x))**2)-1

print('========== Fonction 5: ==========\n')
Newton(f5,f5der,1.2,1e-5,20),print('\n\n')




#========== Fonction 6: ==========

def f6(x):
    return x**2+3-math.exp(x)

def f6der(x):
    return 2*x-math.exp(x)

print('========== Fonction 6: ==========\n')
Newton(f6,f6der,1.9,1e-5,20),print('\n\n')




#========== Fonction 7: ==========

def f7(x):
    return 3*x+4*math.log(x)-7

def f7der(x):
    return 3+4/x

print('========== Fonction 7: ==========\n')
Newton(f7,f7der,1.7,1e-5,20),print('\n\n')




#========== Fonction 8: ==========

def f8(x):
    return x**4-2*x**2+4*x-17

def f8der(x):
    return 4*x**3-4*x+4

print('========== Fonction 8: ==========\n')
Newton(f8,f8der,-2,1e-5,20)
Newton(f8,f8der,3,1e-5,20),print('\n\n')




#========== Fonction 9: ==========

def f9(x):
    return math.exp(x)-2*math.sin(x)-7

def f9der(x):
    return math.exp(x)-2*math.cos(x)

print('========== Fonction 9: ==========\n')
Newton(f9,f9der,3,1e-5,20),print('\n\n')




#========== Fonction 10: ==========

def f10(x):
    return math.log(x**2+4)*math.exp(x)-10

def f10der(x):
    return (2*x*math.exp(x))/(x**2+4)+math.log(x**2+4)*math.exp(x)

print('========== Fonction 10: ==========\n')
Newton(f10,f10der,2,1e-5,20),print('\n\n')



