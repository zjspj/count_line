import sys
import re

def return_content(file_name):
    file_obj = open(file_name, "r")
    file_content = file_obj.read()
    file_obj.close()
    return file_content

def main():
    argument = sys.argv
    file_obj = open(argument[1], "r")
    file_content = file_obj.read()
    file_obj.close()
    line_counter = 0
    if file_content[-2:] == "\n":
        line_counter -= 1
    search_obj = re.compile("\n")
    match_list = search_obj.findall(file_content)
    line_counter += len(match_list)
    print(line_counter)
    return line_counter


if __name__ == "__main__":
    main()





