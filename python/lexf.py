def iterate(prefix, alphabet, target_len):
    should_continue = len(prefix) < target_len - 1
    for c in alphabet:
        print(prefix + c)
        if should_continue:
            iterate(prefix + c, alphabet, target_len)

alphabet = input().split()
length = int(input())

iterate('', alphabet, length)