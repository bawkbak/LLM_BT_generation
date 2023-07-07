import os

def remove_front_until(text, specified_text):
    index = text.find(specified_text)
    if index != -1:
        return text[index:]
    else:
        return text


def find_file(file_name, directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[0] == file_name:
                return os.path.join(root, file)
    return None

def append_tab(input_string, num_tabs):
    new_strings = ""
    strings = input_string.split("\n") 
    for string in strings:
        # print("debug")
        # print(string)
        if string == "->" or string == "?":
            prefix = ""
            for i in range(num_tabs):
                prefix += '\t'
            new_strings = new_strings + string
        else:
            prefix = "\n"
            for i in range(num_tabs):
                prefix += '\t'
            new_strings = new_strings + prefix + string
    
    return new_strings

def subtree_assembly(raw):
    lines = raw.split("\n")  # Split the input string by newlines
    result = []

    for line in lines:
        if line.startswith("\t"):
            num_tabs = line.count("\t")  # Count the number of tabs in the line
            stripped_line = line.strip()  # Remove leading and trailing whitespaces
            if stripped_line.startswith("\"") and stripped_line.endswith("\""):
                extracted_string = stripped_line[1:-1]  # Extract the string between quotation marks
                result.append((extracted_string, num_tabs))
            else:
                extracted_string = stripped_line[0:2]
                result.append((extracted_string, num_tabs))

    # Print the extracted strings and the number of tabs for each string
    # for string, num_tabs in result:
    #     print(f"String: {string}, Number of Tabs: {num_tabs}")


    # # #
    final = "->"
    for string, num_tabs in result:
        final = final + "\n"
        if string != "->":
            directory_path = "subtree/" + string + ".tree"

            with open(directory_path, 'r') as file:
                subtree = file.read().rstrip()
            new_subtree = append_tab(subtree, num_tabs)

            for i in range(num_tabs):
                final = final + "\t"
            final = final + new_subtree
        else:
            for i in range(num_tabs):
                final = final + "\t"
            final = final + string
    
    return final

        
