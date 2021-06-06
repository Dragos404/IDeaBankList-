import sys

def add_to_list():
    f = open("idea.txt", "r")
    lines2 = f.readlines()
    f.close()
    return lines2

def del_line(index):
    f = open("idea.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("idea.txt","w")
    for i, line in enumerate(lines):
        if i != int(index):
            f.write(line)
            print(i)
            print(index)
            print(i != index)
    f.close()

def check_if_correct(second_arg, lines2):
    if int(second_arg) >= (len(lines2)-1) or int(second_arg) <= 0:
        exit()

def ask_for_new_idea():
    new_idea = input("what is your new idea? ")
    f = open("idea.txt", "a")
    f.write(new_idea + "\n")
    f.close()
    print_lines_with_leading_number()

def print_lines_with_leading_number():
    f = open("idea.txt", "r")
    lines = f.readlines()
    i = 1
    for line in lines:
        print(f'{i}. {line}')
        i += 1
    f.close()

def main():
    if len(sys.argv) == 1:
        while True:
            ask_for_new_idea()
    elif len(sys.argv) == 2 and sys.argv[1] == "--list":
        print_lines_with_leading_number()
    elif len(sys.argv) == 2 and sys.argv[1] == "--delete":
        print("Specify a number after --delete")
    elif len(sys.argv) == 3 and sys.argv[1] == "--delete" and sys.argv[2].isnumeric():
        print(sys.argv[2])
        # lines2 = add_to_list()
        # check_if_correct(sys.argv[2], lines2)
        del_line(sys.argv[2])
        # print_lines_with_leading_number()
    elif len(sys.argv) == 3 and sys.argv[1] == "--delete" and not sys.argv[2].isnumeric():
        print("Specify a number after --delete")
    else:
        exit()   

if __name__ == "__main__":
    main()



