from math import floor, ceil
from copy import deepcopy

def get_max_sizes(data: list):
    max_sizes = [0] * len(data[0])
    for line in data:
        for index, item in enumerate(line):
            max_sizes[index] = (
                len(item) if max_sizes[index] < len(item) else max_sizes[index]
            )
    return max_sizes

def align(item, max_size, align = "left"):
    return_string = ""
    padding = (max_size - len(item))
    if align == "left":
        return_string += (item + padding * " ")
    elif align == "centre":
        if padding // 2 != 0:
            padding = [floor(padding//2), ceil(padding//2)]
            return_string += (padding[0] * " " + item + padding[1] * " ")
        else:
            return_string += (padding/2 * " " + item + padding/2 * " ")
    elif align == "right":
        return_string += (padding * " " + item)
    else:
        return_string += (item + padding * " ")
    return return_string

# Functions to construct table features
def line(max_sizes, line = "mid"):
    corners = {
        "top": ["\u250C", "\u252C", "\u2510"],
        "mid": ["\u251C", "\u253C", "\u2524"],
        "bot": ["\u2514", "\u2534", "\u2518"]
    }.get(line, "mid")
    return_string = "\n" + corners[0]
    for index, max_size in enumerate(max_sizes):
        return_string += (max_size)*"\u2500"
        if 0 < index < len(max_sizes):
            return_string += corners[1]
    return_string += corners[2]
    return return_string

def make_header(headers: list, max_sizes: list) -> str:
    return_string = "\n"
    return_string += line(max_sizes, "top")
    return_string += make_row(headers, max_sizes)
    return_string += line(max_sizes, "mid")
    return return_string
    
def make_row(data: list, max_sizes: list) -> str:
    return_string = "\n"
    for index, item in enumerate(data):
        return_string += "\u2502" + align(item, max_sizes[index])
    return_string += "\u2502"
    return return_string

def make_table(data: list, headers: bool = True, padding: int = 3) -> str:
    table_data = deepcopy(data)
    return_string = "\n"
    max_sizes = get_max_sizes(table_data)
    map(lambda max_size: max_size + padding, max_sizes)
    if headers:
        return_string += make_header(table_data[0], max_sizes)
        table_data.pop(0)
    else:
        return_string += line(max_sizes, "top")
    for row in table_data:
        return_string += make_row(row, max_sizes)
    return_string += line(max_sizes, "bot")  
    return return_string

if __name__ == "__main__":    
    test_table = [
        ["This", "is", "a", "header"],
        ["This", "is", "two", "tests"],
        ["This", "is", "three", "tests"],
        ["This", "is", "four", "tests"],
        ["This", "is", "five", "tests"]
    ]
    print(get_max_sizes(test_table))
    print(make_table(test_table))
    print(test_table)