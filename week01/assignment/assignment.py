'''
Time Guesstimate to complete:
Proficient with all the "Know how to" statements:                       1 hour
Familiar with the "Know how to" statements, but need to review a few:   1 - 4 hours
Need to review most the "Know how to" statements:                       4 - 8 hours
Need to review/relearn all the "Know how to" statements:                8+ hours

All ASSERTS must pass. Everything in this assignment should have been learned
previously. If there are holes in your knowledge, then this is the time to 
fill them (meaning learn the concepts). Take the time to learn by reading
the provided links. There are no group "prove" assignments in this class.

Make sure to write comments above your functions, explaining in your own
words what the functions does. Your comments are your "digital signature",
showing that you both wrote the code and understand how it works.

Grading:
Not passing an assert or answering #10 and #12: 0 points (code must pass all asserts--this is only true of this first assignment)
'''

from unittest import TestCase
from cse251functions import *

# 1) TODO write a function called 'perform_math' that takes three parameters:
#      - initial_value: int
#      - value: int
#      - operation: str
#      - return value: float
#      The function should perform the mathematical operation, represented
#      by the string operation parameter, on the initial_value and value.
#      Delete these instructions and replace with your own description of that the function does.

def perform_math(initial_value: int, value: int, operation: str) -> float:
    """
    Performs a mathematical operation on two integers and returns the result as a float.

    Parameters:
    initial_value (int): The starting number to perform the operation on.
    value (int): The number used to perform the operation.
    operation (str): The operation to be performed, represented as a string.
                     Can be one of the following: '+', '-', '*', '/', '**' (exponentiation).

    Returns:
    float: The result of the operation between initial_value and value.

    Raises:
    ValueError: If an unsupported operation is provided.
    ZeroDivisionError: If a division by zero is attempted.
    """
    
    if operation == '+':
        return float(initial_value + value)
    elif operation == '-':
        return float(initial_value - value)
    elif operation == '*':
        return float(initial_value * value)
    elif operation == '/':
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return float(initial_value / value)
    elif operation == '**':
        return float(initial_value ** value)
    else:
        raise ValueError(f"Unsupported operation: {operation}")


def find_word_index(word_to_find: str, words: list) -> int:
    """
    Returns the index of the specified word in the provided list of words.

    Parameters:
    word_to_find (str): The word whose index is to be found.
    words (list): A list of strings where the search for the word will occur.

    Returns:
    int: The index of the word_to_find in the list.

    Raises:
    ValueError: If the word is not found in the list.
    """
    return words.index(word_to_find)


def get_value_from_dict_using_key(key: str, word_dict: dict) -> str:
    """
    Returns the value associated with the specified key from the given dictionary.

    Parameters:
    key (str): The key to search for in the dictionary.
    word_dict (dict): A dictionary where the key-value pair is stored.

    Returns:
    str: The value associated with the given key.

    Raises:
    KeyError: If the key is not found in the dictionary.
    """
    return word_dict[key]


def get_list_of_urls_from_dict(key: str, url_dict: dict) -> list:
    """
    Returns the list of URLs associated with the specified key from the given dictionary.

    Parameters:
    key (str): The key to search for in the dictionary.
    url_dict (dict): A dictionary where the key is mapped to a list of URLs.

    Returns:
    list: The list of URLs associated with the given key.

    Raises:
    KeyError: If the key is not found in the dictionary.
    """
    return url_dict[key]


def find_url(urls: list, name: str) -> str:
    """
    Searches for and returns the first URL in the list that contains the specified name.
    If no such URL is found, returns an empty string.

    Parameters:
    urls (list): A list of URL strings to search within.
    name (str): The name or keyword to search for in the URLs.

    Returns:
    str: The first URL that contains the specified name, or an empty string if none is found.
    """
    for url in urls:
        if name in url:
            return url
    return ""


def find_str_in_file(filename: str, str_to_find: str) -> bool:
    """
    Checks if the specified string is present in the contents of a given file.

    Parameters:
    filename (str): The name of the file to search within.
    str_to_find (str): The string to search for in the file.

    Returns:
    bool: True if the string is found in the file, False otherwise.

    Raises:
    FileNotFoundError: If the file does not exist.
    """
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            return str_to_find in contents
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")


class MyParentClass:
    """
    A class that holds an integer value, a list of values, and a name, 
    and provides a method to access an element in the list by index.

    Attributes:
    value (int): An integer value.
    values (list): A list of values.
    name (str): A string representing the name.

    Methods:
    get_value_using_index(index: int) -> int: 
        Returns the value from the 'values' list at the specified index.
    """

    def __init__(self, value: int, values: list, name: str):
        self.value = value
        self.values = values
        self.name = name

    def get_value_using_index(self, index: int) -> int:
        """
        Returns the value from the 'values' list at the given index.

        Parameters:
        index (int): The index of the value to retrieve from the list.

        Returns:
        int: The value at the specified index in the 'values' list.
        """
        return self.values[index]


class MyChildClass(MyParentClass):
    """
    A class that extends MyParentClass by adding an additional 'age' attribute.

    Attributes:
    value (int): An integer value inherited from MyParentClass.
    values (list): A list of values inherited from MyParentClass.
    name (str): A string representing the name, inherited from MyParentClass.
    age (int): An additional integer attribute representing age.

    Methods:
    Inherits all methods from MyParentClass.
    """

    def __init__(self, value: int, values: list, name: str, age: int):
        # Call the constructor of the parent class with appropriate parameters
        super().__init__(value, values, name)
        self.age = age


def pass_by_reference_mutable_example(lists_are_passed_by_reference_and_mutable: list, str_to_add: str) -> str:
    """
    Appends the given string to the provided list and returns the element at index 0.

    Parameters:
    lists_are_passed_by_reference_and_mutable (list): The list to which the string will be appended.
    str_to_add (str): The string to append to the list.

    Returns:
    str: The value at index 0 of the list after the string has been appended.
    """
    lists_are_passed_by_reference_and_mutable.append(str_to_add)
    return lists_are_passed_by_reference_and_mutable[0]


def pass_by_reference_immutable_example(strings_are_pass_by_reference_and_immutable: str, str_to_add: str) -> str:
    """
    Concatenates the given string to the provided string and returns the new string.

    Parameters:
    strings_are_pass_by_reference_and_immutable (str): The original string to which another string will be appended.
    str_to_add (str): The string to append to the original string.

    Returns:
    str: The new string resulting from concatenation of the original string and the string to add.
    """
    return strings_are_pass_by_reference_and_immutable + str_to_add


# Don't change any of the assert lines. All asserts should pass. You should see "All tests passed!" if all assert pass.
# If an assert doesn't pass, you will see an AssertionError (see https://www.w3schools.com/python/ref_keyword_assert.asp).
# The AssertionError will show you why it didn't pass (meaning, it is not an error with the assertion code, but with your code)

def main():
    ''' Know how to:
        - Call a function
        - Pass in parameters to a function in the correct order
        - Use correct parameter data types
        - Return a value from a function
        - Return correct data type from a function
        - Return from all call paths in a a function
        - Write an IF statement
        - Reading: https://www.geeksforgeeks.org/python-functions/
    '''
    assert perform_math(10, 1, "+") == 11
    assert perform_math(1, 10, "+") == 11
    assert perform_math(10, 1, "-") == 9
    assert perform_math(1, 10, "-") == -9
    assert perform_math(10, 2, "*") == 20
    assert perform_math(2, 10, "*") == 20
    assert perform_math(10, 2, "/") == 5
    assert perform_math(2, 10, "/") == 0.2
    assert perform_math(10, 3, "//") == 3
    assert perform_math(3, 10, "//") == 0
    assert perform_math(10, 3, "**") == 1000
    assert perform_math(3, 10, "**") == 59049

    ''' Know how to:
        - Use a list
        - Use the index function on a list
        - Reading: https://www.geeksforgeeks.org/python-lists/
    '''
    assert find_word_index("a", ["a", "b", "c", "h"]) == 0
    assert find_word_index("b", ["a", "b", "c", "h"]) == 1
    assert find_word_index("c", ["a", "b", "c", "h"]) == 2
    assert find_word_index("h", ["a", "b", "c", "h"]) == 3

    ''' Know how to:
        - Use a dictionary
        - Use a key to get the value in a dictionary
        - Understand that a dictionary value can be list
        - Know how to get the list using a key
        - Know how to write a FOR loop
        - Know how to use "in" keyword
        - Reading: https://www.geeksforgeeks.org/python-dictionary/
    '''
    word_dict = {"k1": 1, "k2": 2, "k3": 3, "k4": 10}
    assert get_value_from_dict_using_key("k1", word_dict) == 1
    assert get_value_from_dict_using_key("k2", word_dict) == 2
    assert get_value_from_dict_using_key("k3", word_dict) == 3
    assert get_value_from_dict_using_key("k4", word_dict) == 10
    movie_dict = {"people": ["http://127.0.0.1:8790/1", "http://127.0.0.1:8790/2", "http://127.0.0.1:8790/3"], "films":
                  ["http://127.0.0.1:8790/film1", "http://127.0.0.1:8790/film2", "http://127.0.0.1:8790/film3"]}
    urls = get_list_of_urls_from_dict("films", movie_dict)
    url = find_url(urls, "film3")
    assert url != None

    '''
        - Know how to make a Python Class
        - Know how to write a constructor
        - Know how to make attributes in a constructor
        - Understand how to use "self" in Python
        - Know how to instantiate an object of a class (shown below)
        - Know how to obtain the value using the object's attribute (shown below)
        - Know what a method is and how to write one
        - Know how to return a value from a method
        - Know to obtain a value at a specific index in a list
        - Know how to extend a class
        - Understand that an extended/child class inherits everything from parent class
        - Readings: https://www.geeksforgeeks.org/python-classes-and-objects/, https://www.geeksforgeeks.org/extend-class-method-in-python/, https://realpython.com/python-super/
    '''
    # 13) TODO instantiate an object using MyParentClass with the following three parameters: (1, [5, 6, 7], "3")
    obj = ...
    assert obj.value == 1
    assert obj.values == [5, 6, 7]
    assert obj.name == "3"
    assert obj.get_value_using_index(0) == 5
    assert obj.get_value_using_index(1) == 6
    assert obj.get_value_using_index(2) == 7

    # 14) TODO instantiate an object using MyChildClass with the following four parameters: (1, [5, 6, 7], "3", 10).
    # 15) TODO: do NOT duplicate the code in the parent class when writing the child class. For example, the parent
    # class constructor already creates the value, values, and name parameters. Do not write these in the child
    # class. Instead, the child constructor should call the parent constructor. Same for the 'get_value_using_index'
    # function, do not rewrite this in the child class.
    childObj = ...
    assert childObj.value == 1
    assert childObj.values == [5, 6, 7]
    assert childObj.name == "3"
    assert childObj.age == 10
    assert childObj.get_value_using_index(0) == 5
    assert childObj.get_value_using_index(1) == 6
    assert childObj.get_value_using_index(2) == 7
    assert isinstance(childObj, MyParentClass) == True

    '''
        - Know how to open a file
        - Know how to read lines from a file
        - Understand how to compare strings
        - Readings: https://www.geeksforgeeks.org/open-a-file-in-python/, https://www.geeksforgeeks.org/with-statement-in-python/
    '''
    assert find_str_in_file("data.txt", "g") == True
    assert find_str_in_file("data.txt", "1") == False

    '''
        - Know the difference between pass-by-reference and pass-by-value.
        - Reading: https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference (read the first answer)
        - Technically python is pass-by-object-reference, if you are intested in the difference, read https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/
    '''
    l = ["abc", "def", "ghi"]
    pass_by_reference_mutable_example(l, "jkl")
    assert len(l) == 4
    assert l[3] == "jkl"
    s = "strings are immutable"
    new_string = pass_by_reference_immutable_example(
        s, " so adding to it creates a new object in memory")
    assert id(s) != id(new_string)
    assert len(new_string) != len(s)

    print("All tests passed!")


if __name__ == '__main__':
    main()
    create_signature_file()
 