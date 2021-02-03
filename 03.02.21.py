side_a, side_b, side_c = input('Please enter 3 sides of triangle: ').split()
# a, b, c, d, = 1


half_perimeter = (float(side_a) + float(side_b) + float(side_c)) / 2

triangle_square = (half_perimeter * (half_perimeter - float(side_a) * (half_perimeter - float(side_b) * (half_perimeter - float(side_c)) ** 0.5

print(triangle_square)

