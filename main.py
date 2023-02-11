
all_points = []
print("Please input points in x y representation.\nType END to finish.")
point_no = 1
while True:
    point = input(f'P#{point_no}: ')
    if point == "END":
        break
    x, y = point.split(" ")
    point = (eval(x), eval(y))
    all_points.append(point)
    point_no += 1

order = len(all_points) - 1
print("Resulting polynomial will be of the order", order)

vander_matrix = []
y_points = []
for point in all_points:
    per_row = []
    for i in range(order, -1, -1):
        per_row.append(point[0]**i)
    vander_matrix.append(per_row)
    y_points.append(point[1])


def print_polynomial(sol):
    poly = ""
    for a, i in zip(sol, range(len(sol)-1, -1, -1)):
        if a > 0:
            poly += "+ "
        poly += str(round(a, 4))
        poly += "x^" + str(i) + " "
    print("f(x): ", poly)

import numpy as np  # This part is taken from previous assignment(project_4) that's why doing with numpy (Not part of this assignment)
sol = np.matmul(np.linalg.inv(np.array(vander_matrix)), np.array(y_points))
print("Calculated Polynomial.")
print_polynomial(sol)

def find_value(polynomial, x):
    poly_val = 0
    for s, p in zip(polynomial, range(len(polynomial)-1, -1, -1)):
        poly_val += s * x ** p
    return poly_val

# Displaying function for different values
values = [-1, 0, 1]
for v in values:
    poly_val = find_value(sol, v)
    print(f'f({v}): {round(poly_val, 4)}')

# derivative computation
derivative = []
for s, p in zip(sol, range(order, 0, -1)):
    derivative.append(s*p)
print("Derivative:")
print_polynomial(derivative)



xn = 2
print("Looking for a root with initial guess", xn)
n = 0
while True:
    derivative_at_xn = find_value(derivative, xn)
    function_at_xn = find_value(sol, xn)
    xnplus1 = xn - function_at_xn/derivative_at_xn
    if abs(100*(xnplus1 - xn)/xnplus1) <= 0.0001 and find_value(sol, xn) <= 0.0001:
        print("Root found for x=", round(xnplus1, 4))
        break
    elif abs(100*(xnplus1 - xn)/xnplus1) <= 0.0001 and find_value(sol, xn) != 0:
        print("Algorithm converged but root not found for x=", round(xnplus1, 1))
        break
    if n == 100:
        print("Algorithm didn't converge after 100 iterations.")
        break
    n+=1
    xn = xnplus1





