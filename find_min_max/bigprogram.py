def circel_area(r): return 3.14 *r*r
def trinangel(b,h): return  0.5 * b*h
def square(s): return  s*s
def recrangle(l,w): return l *w
def simoleintrest(p,r,t): return p*r*t
 
while True:
    print("\n1.Circle 2.Triangle 3.Square 4.Rectangle 5.Interest 6.Exit")
    choice = int(input("Enter choice: "))
 if choice == 1:
    print(input(enter radius ))
    print("area",circel_area(r))