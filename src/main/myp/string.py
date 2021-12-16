"""
Clase para convertir caracteres a su equivalente binario.
"""

class String:

    def strToBinary(str):
        bin_conv = []
 
        for letter in str:
            
            # convert each char to
            # ASCII value
            ascii_val = ord(letter)            
         
            # Convert ASCII value to binary
            binary_val = bin(ascii_val)
            bin_conv.append(binary_val[2:])
         
        return (' '.join(bin_conv))
    
    def isASCII(test_string):        
        res = all(31 < ord(c) < 128 for c in test_string)        
        return res    