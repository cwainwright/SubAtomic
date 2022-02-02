from copy import deepcopy

class Table:
    def __init__(self, data: list, headers: bool = True, alignment = "left", padding: int = 3):
        table_data = deepcopy(data)
        self.return_string = "\n"
        max_sizes = self.get_max_sizes(table_data)
        max_sizes = [max_size + padding for max_size in max_sizes]
        if headers:
            self.return_string += self.make_header(table_data[0], max_sizes, alignment)
            table_data.pop(0)
        else:
            self.return_string += self.line(max_sizes, "top")
        for row in table_data:
            self.return_string += self.make_row(row, max_sizes, alignment)
        self.return_string += self.line(max_sizes, "bot")
        
    # Functions to construct table features
    def get_max_sizes(self, data: list):
        max_sizes = [0] * len(data[0])
        for line in data:
            for index, item in enumerate(line):
                max_sizes[index] = (
                    len(item) if max_sizes[index] < len(item) else max_sizes[index]
                )
        return max_sizes

    def align(self, item, max_size, align = "left"):
        return_string = ""
        padding = (max_size - len(item))
        if align == "left":
            return_string += (item + padding * " ")
        elif align == "centre":
            if padding // 2 != 0:
                padding = [round(padding//2)-1, round(padding//2)]
                return_string += (padding[0] * " " + item + padding[1] * " ")
            else:
                return_string += (padding/2 * " " + item + padding/2 * " ")
        elif align == "right":
            return_string += (padding * " " + item)
        else:
            return_string += (item + padding * " ")
        return return_string
    
    def line(self, max_sizes, line = "mid"):
        corners = {
            "top": ["\u250C", "\u252C", "\u2510"],
            "mid": ["\u251C", "\u253C", "\u2524"],
            "bot": ["\u2514", "\u2534", "\u2518"]
        }.get(line, "mid")
        return_string = "\n" + corners[0]
        for index, max_size in enumerate(max_sizes):
            return_string += max_size * "\u2500"
            if index != len(max_sizes) - 1:
                return_string += corners[1]
        return_string += corners[2]
        return return_string

    def make_header(self, headers: list, max_sizes: list, alignment:str = "left") -> str:
        return_string = self.line(max_sizes, "top")
        return_string += self.make_row(headers, max_sizes, alignment)
        return_string += self.line(max_sizes, "mid")
        return return_string
        
    def make_row(self, data: list, max_sizes: list, alignment: str = "left") -> str:
        return_string = "\n"
        for index, item in enumerate(data):
            return_string += "\u2502" + self.align(item, max_sizes[index], alignment)
        return_string += "\u2502"
        return return_string
    
    def __str__(self):
        return self.return_string

if __name__ == "__main__":    
    test_table = [
        ["H1", "H2", "H3"],
        ["H1.1", "H2.1", "H3.1"],
        ["H1.2", "H2.2", "H3.2"],
        ["H1.3", "H2.3", "H3.3"]
    ]
    print(Table(test_table))