import os

# Let`s find all the "*.txt"-files 
def give_list_of_files(path):
    list_of_txt = []
    for file in os.listdir(path):
        if file.endswith(".txt"):
            list_of_txt.append(file)
    return list_of_txt

# Let`s count lines and make a counted list of tuples
def count_my_lines(my_list):
    dict_as_counter = {}
    for file in my_list:
        counter = 0
        with open(file) as current_file:
            for line in current_file:
                counter += 1
        dict_as_counter[file] = counter
    counted_list = list(dict_as_counter.items())
    return counted_list

# Let`s bubble them
def sort_my_files(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1):
            if my_list[j][1] > my_list[j+1][1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

# Let`s write a new file
def write_file(my_list):
    with open('the_big_one', 'a') as my_big_file:
        for file in my_list:
            my_big_file.write(file[0]+'\n'+str(file[1])+'\n')
            with open(file[0]) as current_file:
                my_big_file.write(current_file.read())

def main():
    path = input('Введите полный путь до директории: ')
    list_of_files = give_list_of_files(path)
    sorted_list_of_files = sort_my_files(count_my_lines(list_of_files))
    write_file(sorted_list_of_files)
    # Uncomment lines below to print the resul file
    # with open('the_big_one') as my_big_file:
    #     print(my_big_file.read().strip())

main()
