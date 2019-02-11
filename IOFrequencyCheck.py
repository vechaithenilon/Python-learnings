import collections

text =input("Please type the sentence you want to check: ")
def checkio(text: str) -> str:
    check_text = text.lower()
    # Generate a list of frequency for all characters
    count = collections.Counter(check_text)
    # Get only letters
    count = {key: value for key, value in count.items() if key.isalpha()}

    # sorted_value = sorted(count, key=count.get, reverse= True)
    sorted_sorted = sorted(count.items(), reverse=False)
    sorted_value = sorted(sorted_sorted, key=lambda x: (x[1]),  reverse=True)


    # print(type(count))
    print("Count is: ")
    print(count)
    print("Sorted value is: ")
    print(sorted_sorted)

    return sorted_value[0][0]

print(checkio(text))


# if __name__ == '__main__':
#     print("Example:")
#     print(checkio("Hello World!"))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio("Hello World!") == "l", "Hello test"
#     assert checkio("How do you do?") == "o", "O is most wanted"
#     assert checkio("One") == "e", "All letter only once."
#     assert checkio("Oops!") == "o", "Don't forget about lower case."
#     assert checkio("AAaooo!!!!") == "a", "Only letters."
#     assert checkio("abe") == "a", "The First."
#     print("Start the long test")
#     assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
#     print("The local tests are done.")




"""Super clean!!!!"""

import string


def checkio(text):

    """

    We iterate through latyn alphabet and count each letter in the text.

    Then 'max' selects the most frequent letter.

    For the case when we have several equal letter,

    'max' selects the first from they.

    """

    text = text.lower()

    return max(string.ascii_lowercase, key=text.count)

