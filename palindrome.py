def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    number_in_string = str(x)
    palindrome = number_in_string[::-1]
    if number_in_string == palindrome:
        return True
    else:
        return False


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('palindrome')
    # Each line calls isPalindrome, compares its result to the expected for that call.
    test(isPalindrome(1444), False)
    test(isPalindrome(99999), True)
    test(isPalindrome(3434343443), False)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
