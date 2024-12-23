def matrix_to_string(hex_matrix):
    """
    Hex matrix to string formate.
    """
    string = ""
    for row in hex_matrix:
        for col in row:
            string += col

    return string

def string_to_matrix(string, hex_matrix):
    i = 0
    for row in range(len(hex_matrix)):
        for col in range(len(hex_matrix[row])):
            hex_matrix[row][col] = string[i:i+6]
            i+=6
    
    return hex_matrix