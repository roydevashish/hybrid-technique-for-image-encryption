import math

def solve_quadratic(a, b, c):
	# Calculate the discriminant
	discriminant = b**2 - 4*a*c

	# Check the nature of roots
	if discriminant > 0:
		# Two distinct real roots
		root1 = (-b + math.sqrt(discriminant)) / (2 * a)
		root2 = (-b - math.sqrt(discriminant)) / (2 * a)

		# return f"Two real roots: {root1:.2f} and {root2:.2f}"
		return max(root1, root2)
	
	elif discriminant == 0:
		# One repeated real root
		root = -b / (2 * a)
		return root
	
	else:
		# Complex roots
		real_part = -b / (2 * a)
		imaginary_part = math.sqrt(-discriminant) / (2 * a)
		return (f"Two complex roots: {real_part:.2f} + {imaginary_part:.2f}i "
					f"and {real_part:.2f} - {imaginary_part:.2f}i")


def solveforx(height, width, x):
	a = 1
	b = height+width
	c = (height*width) - x
	root = solve_quadratic(a, b, c)
	return math.ceil(root)
