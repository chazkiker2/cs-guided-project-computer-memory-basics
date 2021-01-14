def cs_binary_to_ascii(binary):
    result_str = ""
    eight_bits = [binary[i:i+8] for i in range(0, len(binary), n)]
    for bit in eight_bits:
        num = int(bit, 2)
        char = chr(num)
        result_str += char

    return result_str