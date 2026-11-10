def c_ke_f(c):
    return c * 9 / 5 + 32

def f_ke_c(f):
    return (f - 32) * 5 / 9

print (c_ke_f(100))                     #212
print (f_ke_c(212))                     #100.0
print (round(f_ke_c(c_ke_f(37)), 2))    #37.0