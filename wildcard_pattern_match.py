def match(first, second):
    pointer1, pointer2 = 0, 0
    while pointer1 < len(first) and pointer2 < len(second):
        if first[pointer1] == '*':
            pointer1 += 1
            while second[pointer2] != first[pointer1] and pointer2 < len(second):
                pointer2 += 1
            if pointer2 == len(second):
                return False
            else:
                pointer1 += 1
                pointer2 += 1
        elif first[pointer1] == '?':
            pointer1 += 1
            pointer2 += 1
        elif first[pointer1] != second[pointer2]:
            return False
    return pointer1 == len(first) - 1


"""
iterate over first
  if char is not a wildcard
    match with pointer at second
  else
    if it is a ?, increment both pointers
    if it is a *, increment second pointer until it finds the char after the *
  
"""
