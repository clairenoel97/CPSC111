# advanced string processing

'''
string comparison
    often we need to compare two strings in order to determine if the strings are equal or not. we can use string comparison operators to do this:
        1. == (equality)
        2. != (not equal)
        3. <>(less than or greater than)

searching a string
    suppose we want to find out if a string contains a certain character, what should we do?
        we can use the keyword 'in' to search the string

string methods
    a function that is associated with an object called a method. to call a method, we use the form <object>.<method name>()

    useful methods for strings include:
        upper()
        lower()
        find(<character to find>)
        replace(<substring to replace>,<string to replace with>)

Practice Problems
    Problem #1
    Write a function called my_str_len() that accepts a string as an argument and returns the number of characters in the string argument. Your function may not make use of the len() built-in function. Think loops!

    In [9]:
    def my_str_len(word):
        '''

        '''
        count = 0
        for letter in word:
            count += 1
        return count

    print(my_str_len("hello"))
    5
    Problem #2
    Write a function called reverse_string() that accepts a string argument (word) and returns the reverse of word.

    In [10]:
    def reverse_string(word):
        '''

        '''
        reverse = ""
        for i in range(len(word) - 1, -1, -1):
            reverse += word[i]
        return reverse

    print(reverse_string("hello"))
    # palindromes (strings that are the same forward as backward)
    print(reverse_string("madam im adam"))
    print(reverse_string("a man a plan a canal panama"))
    olleh
    mada mi madam
    amanap lanac a nalp a nam a
    Problem #3
    Write a predicate function called is_reverse() that accepts two string arguments (word1 and word2) and returns whether or not word2 is the reverse of word1.

    In [12]:
    def is_reverse_in_place(word1, word2):
        '''

        '''
        i = 0
        j = len(word2) - 1

        if len(word1) != len(word2):
            return False

        while i < len(word1):
            if word1[i] != word2[j]:
                return False
            i += 1
            j -= 1

        return True

    print(is_reverse("hello", "olleh"))
    print(is_reverse("hello", "olelh"))
    True
    False
'''
