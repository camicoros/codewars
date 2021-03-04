"""
You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, 
containing the names of people who like an item. 
It must return the display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
"""


def likes(names):
    people_count = len(names)
    first_part = ", ".join(names[:2])
    second_part = " "
    third_part = "like"
    if people_count == 0:
        first_part = "no one"
        third_part += "s"
    elif people_count == 1:
        third_part += "s"
    elif people_count == 2:
        first_part = " and ".join(names[:2])
    elif people_count == 3:
        second_part += "and " + names[2] + " "
    elif people_count > 3:
        second_part += "and " + str((people_count - 2)) + " others "
    return "{}{}{} this".format(first_part, second_part, third_part)


def main():
    print(likes([]))
    print(likes(["Alex",]))
    print(likes(["Alex", "Jacob",]))
    print(likes(["Alex", "Jacob", "Mark",]))
    print(likes(["Alex", "Jacob", "Mark", "Max"]))

if __name__ == "__main__":
    main()
