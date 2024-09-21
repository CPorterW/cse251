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

def perform_math(initial_value: int, value: int, operation: str) -> float:
    """A function for performing various mathemetical operations on two numbers.
    
    Parameters:
        initial_value, value: integers that will be used in the operation
        operation: a string form of an operator, +, -, /, *, //, or **

    Returns:
        float: The result of the operation.
    """
    if operation == '+':
        return value + initial_value
    elif operation == '-':
        return initial_value - value
    elif operation == '*':
        return initial_value * value
    elif operation == '**':
        return initial_value ** value
    elif operation == '/':
        return initial_value / value
    elif operation == '//':
        return initial_value // value
    else:
        print('Please use valid parameters.')

def find_word_index(word_to_find:str, words:list) -> int:
    """Finds a word in a list of words and returns the index value of that word.

    Args:
        word_to_find (str): The word this function will search for.
        words (list): The list of words containing the word that is being found.

    Returns:
        int: The index value of the word that was found.
    """
    return words.index(word_to_find)

def get_value_from_dict_using_key(key: str, word_dict: dict) -> str:
    """A function for getting a value from a dictionary based on its key

    Args:
        key (str): The key of the dictionary whose value you're trying to retrieve
        word_dict (dict): The dictionary with the key value pair you're using.

    Returns:
        str: The retrieved value
    """
    return word_dict[key]

def get_list_of_urls_from_dict(key: str, url_dict: dict) -> list:
    """This is a function for retrieving a list from a dictionary.

    Args:
        key (str): The key of the key-value pair whose value you're trying to find
        url_dict (dict): the dictionary you're searching in

    Returns:
        list: The list you were searching for
    """
    return url_dict[key]

def find_url(urls: list, name: str) -> str:
    """This function finds a url in a list of urls by a string that url contains, 
    or else returns an empty string.

    Args:
        urls (list): The list of urls that is to be searched in
        name (str): A string to be found in the url that is to be returned

    Returns:
        str: The url that will be returned
    """
    for url in urls:
        if name in url:
            return url
    return ''

def find_str_in_file(filename:str, str_to_find:str) -> bool:
    """Searches a file for a string and returns true if the string is present,
    false, otherwise.

    Args:
        filename (str): The name of the file for searching
        str_to_find (str): the string that may or may not be in the file

    Returns:
        bool: true or false, depending on whether the str_to_find is in the file.
    """
    with open(filename, 'r') as file:
        fileContents = file.read()
        
        # I love how versatile 'in' is. I forget sometimes that it's not just for
        # for statements and if conditionals, but that it can be used to search entire files
        # like this.
        return str_to_find in fileContents

class MyParentClass: # not MyParentTrap 
    """A class that contains an int, a list, and a string, and a method for retrieving
    a value from the list using the int as an index. 
    
    Attributes:
        value (int): An index integer for retrieving a value from a list
        values (list): A list 
        name (str): A name string

    Methods:
        get_value_using_index(index: int) -> int
            Returns the value from values at the index.
    """
    
    def __init__(self, value: int, values: list, name: str):
        self.value = value
        self.values = values
        self.name = name
        
    def get_value_using_index(self, index: int) -> int:
        """Returns a number from a list based on a given index.

        Args:
            index (int): The index of the list value

        Returns:
            int: The retrieved number
        """
        return self.values[index]

class MyChildClass(MyParentClass):
    """MyParentClass, but with age, too.

    Attributes:
        Everything from MyParentClass
        age (int): An int representing age

    Methods:
        get_value_using_index(index: int) -> int: from MyParentClass
    """
    def __init__(self, value: int, values: list, name: str, age: int):
        super().__init__(value, values, name)
        self.age = age

def pass_by_reference_mutable_example(lists_are_passed_by_reference_and_mutable: list, str_to_add: str) -> str:
    """This function both adds a value to a list and returns the first value of that list. 
    This demonstrates pass-by-reference, which is when a list is passed into a function by
    the address of the space it occupies in the computer's memory. This also demonstrates 
    mutability, which is the ability for a list or array to change without creating a new 
    list or array in a separate place in memory. This means that changes that are made to the 
    list within this function will persist outside the function even though we never pass back
    the list.

    Args:
        lists_are_passed_by_reference_and_mutable (list): a list of strings
        str_to_add (str): a string to be appended to the list

    Returns:
        str: the first string in the list
    """
    lists_are_passed_by_reference_and_mutable.append(str_to_add)
    return lists_are_passed_by_reference_and_mutable[0]
    
def pass_by_reference_immutable_example(strings_are_pass_by_reference_and_immutable: str, str_to_add: str) -> str:
    """This function appends a string to another string and returns the combined string, demonstrating 
    immutability. Immutability means unchangability, meaning that whenever a string is added to or taken
    from, it is really a new string with a different address, assigned to the same variable, but that is 
    why strings must be passed back from functions and assigned to their proper variable, or else the 
    the function would have no effect on the original variable.

    Args:
        strings_are_pass_by_reference_and_immutable (str): A string
        str_to_add (str): The string that will be added to the other string

    Returns:
        str: The combined string
    """
    return strings_are_pass_by_reference_and_immutable + str_to_add

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

    obj = MyParentClass(1, [5,6,7], '3')
    assert obj.value == 1
    assert obj.values == [5, 6, 7]
    assert obj.name == "3"
    assert obj.get_value_using_index(0) == 5
    assert obj.get_value_using_index(1) == 6
    assert obj.get_value_using_index(2) == 7

    childObj = MyChildClass(1, [5,6,7], '3', 10)
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
 