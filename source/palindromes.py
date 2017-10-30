#!python

import string
import re
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)

    # Clean the input to make sure we get correct return
    clean_text = text.lower().strip()
    clean_text = re.sub('\W', '', clean_text)

    # return is_palindrome_iterative(clean_text)
    return is_palindrome_recursive(clean_text)


def is_palindrome_iterative(text):
    reverse_text = text[::-1]

    for i in range(len(text) - 1):
        if text[i] != reverse_text[i]:
            return False
    return True


def is_palindrome_recursive(text, left=None, right=None):
    if left == None and right == None:
        left = 0
        right = len(text) - 1

    if right < left:
        return True
    elif text[left] != text[right]:
        return False
    else:
        return is_palindrome_recursive(text, left + 1, right - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
