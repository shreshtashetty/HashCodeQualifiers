class Solution:

    def __init__(self):
        self.input_list = list()
        self.contributors = dict()
        self.projects = dict()

    # Prepare Input

    def read_file(self, file_path : str) -> None:
        my_file = open(file_path, "r")
        
        result = my_file.read()

        my_file.close()

        self.input_list = result.split()

        return

    def print_data(self):

        for i in self.input_list:
            print(i)

    # Input

    def get_input(self):

        for i in range(2, len(self.input_list)):
        
            num_contributors = int(self.input_list[0])
            num_projects = int(self.input_list[1])
            

            for j in range(i, num_contributors):
                person_index = i
                self.contributors[self.input_list[person_index]]
                i+=1
                num_skills = int(self.input_list[i])
                my_list = []
                for i in range(num_skills*2):
                    my_list.append(self.input_list[i])
                    i+=1

                self.contributors[self.input_list[person_index]] = my_list

            break

        return

    def print_cont(self):
        print()
        for i in self.contributors:
            print(i)


if __name__ == "__main__":
    s = Solution()
    s.read_file("a_an_example.in.txt")
    s.print_cont()