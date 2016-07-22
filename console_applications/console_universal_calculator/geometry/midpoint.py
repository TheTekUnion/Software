import math


def midpoint_1d(x1, x2):
    return (x1 + x2) / 2


def midpoint_2d(x1, x2, y1, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return "(" + str(x) + ", " + str(y) + ")"


def midpoint_3d(x1, x2, y1, y2, z1, z2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    z = (z1 + z2) / 2
    return "(" + str(x) + ", " + str(y) + ", " + str(z) + ")"


#Custom amount of dimensions and custom amount of points in development
def midpoint_nd(n_dim):
    #Variables for dimension list
    cur_dim = 1
    dim_ls = []

    while cur_dim <= n_dim:

        #Ask the user for their point input for each dimension
        point1 = float(eval(input("Enter the first point in dimension " + str(cur_dim) + ": ")))
        point2 = float(eval(input("Enter the second point in dimension " + str(cur_dim) + ": ")))

        #Calculate the midpoint of each dimension
        dimension_midpoint = (point1 + point2) / 2
        #Append the nth dimension midpoint to our dimension list
        dim_ls.append(dimension_midpoint)
        cur_dim += 1

    #Return the midpoint as a string without additional punctuation
    if n_dim == 1:
        midpoint_string = str(dim_ls[0])
        return midpoint_string

    #Convert the list to a tuple (2+ dimensions) in order to show parenthesis for orders and then convert it into a string for output
    else:
        midpoint_string = str(tuple(dim_ls))
        return midpoint_string


def midpoint_ndmp(n_dim, m_point):
    #Variables for dimension list
    cur_dim = 1
    dim_ls = []

    #Outer loop used to loop through dimensions
    while cur_dim <= n_dim:
        #Variables for point list
        cur_point = 1
        point_ls = []
        #Inner loop used to loop through points
        while cur_point <= m_point:
            #Input received for all points of all dimensions in this statement
            point_input = float(eval(input("Enter point " + str(cur_point) + " in dimension " + str(cur_dim) + ": ")))
            #Append points to the point_ls
            point_ls.append(point_input)
            cur_point += 1
        #Store the sum of the values in point_ls in the variable dimension_point_total
        dimension_point_total = sum(point_ls)
        #Average the dimension point total
        dimension_midpoint = dimension_point_total / m_point
        #Append each dimension midpoint to the dim_ls
        dim_ls.append(dimension_midpoint)
        #Clear all indexes in point_ls
        del point_ls[:]
        cur_dim += 1

    #Return the midpoint as a string without additional punctuation
    if n_dim == 1:
        midpoint_string = str(dim_ls[0])
        return midpoint_string

    #Convert the list to a tuple in order to show parenthesis for ordered sets and then convert it into a string for output (2+ dimensions)
    else:
        midpoint_string = str(tuple(dim_ls))
        return midpoint_string
