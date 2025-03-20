def padding(string, length_of_padding, height, width):
    x = f"{height:03x}{width:03x}"
    padded_string = string + '0' * (length_of_padding - 12) + x + f"{length_of_padding:06x}"
    return padded_string

def removepadding(string):
    padding_length = int(string[-6:], 16)
    height = int(string[-12:-9], 16)
    width = int(string[-9:-6], 16)
    return string[:len(string)-padding_length], height, width