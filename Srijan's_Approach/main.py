def read_file(file_path : str) -> str:
    my_file = open(file_path, "r")
    return my_file.read()

if __name__ == "__main__":
    print(read_file("a_an_example.in.txt"))