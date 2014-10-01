def get_permutations(string):
    result = []

    permute(string, 0, result)

    return result

def permute(string, index, result):
    if index >= len(string) - 1:
        result.append(string)
        return

    permute(string, index + 1, result)

    swap_index = index + 1
    while swap_index < len(string):
        str_lst = list(string)

        str_lst[index], str_lst[swap_index] = str_lst[swap_index], str_lst[index]
        string = ''.join(str_lst)

        permute(string, index + 1, result)
        swap_index += 1

permutations = get_permutations('0123456789')
print permutations[1000000 - 1]
