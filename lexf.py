def iterate(prefix, alphabet, target_len):
    should_continue = len(prefix) < target_len - 1
    for c in alphabet:
        print prefix + c
        if should_continue:
            iterate(prefix + c, alphabet, target_len)

alphabet = raw_input().split()
length = int(raw_input())

iterate('', alphabet, length)