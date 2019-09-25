
def get_palindrome(string):
    cnt = 1
    palindrome_occr = []
    string_len = len(string)

    while string_len != 0:
        for occr in range(0, string_len):
            temp = string[occr:occr+cnt]
            if temp not in palindrome_occr:
                if str(temp) == str(temp)[::-1]:
                    palindrome_occr.append(temp)
        cnt += 1
        string_len -= 1
    return len(palindrome_occr), palindrome_occr


if __name__ == '__main__':
    occr_cnt = 1
    print("Enter string:", end=" ")
    input_string = input()
    pall_len, pall_list = get_palindrome(input_string)
    print("{} palindrome occurrences".format(pall_len))
    for val in pall_list:
        print("Occurrence {}: {}".format(occr_cnt, val))
        occr_cnt += 1

