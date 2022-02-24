from collections import defaultdict

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

    # Shreshta's Parser
    def fileParser(self, path):
        with open(path, 'r') as f:
            lines = f.readlines()
            # print(lines)
            num_contribs, num_projs = lines[0].split()
            num_contribs = int(num_contribs)
            num_projs = int(num_projs)
            contribs, projs = {}, {}
            flag = 0
            i = 1
            while i < len(lines):
                line = lines[i].split()
                if len(line) > 2:
                    flag = 1
                if flag == 0:
                    # print("Contribs:", line)
                    name = line[0]
                    num_skills = int(line[1])
                    i += 1
                    if name not in contribs:
                        contribs[name] = []

                    for j in range(i, num_skills+i):
                        line = lines[j].split()
                        contribs[name].append((line[0], int(line[1])))
                    i += num_skills

                else:
                    line = lines[i].split()
                    if len(line) > 2:
                        proj_name = line[0]
                        projs[proj_name] = []
                        for j in range(1, len(line)):
                            projs[proj_name].append(int(line[j]))
                        i += 1
                    else:
                        projs[proj_name].append((line[0], int(line[1])))
                        i += 1
            # print(contribs, projs)
            self.contributors = contribs
            self.projects = projs
            return 

    def get_right_candidate(self, project = "Logging"):
        num_skills = int(self.projects[project][3])
        for _ in range(num_skills):
            skill = self.projects[project][-1]
            for i in self.contributors.keys():
                for j in self.contributors[i]:
                    #print(j)
                    if(j[0] == skill[0]):
                        if(int(j[1]) >= int(skill[1])):
                            print("match")
                            print(i,j)
                            print(skill)

if __name__ == "__main__":
    s = Solution()
    s.fileParser("a_an_example.in.txt")
    #print(s.projects["Logging"])
    #print(s.contributors)
    
    for i in s.projects.keys():
        s.get_right_candidate(i)
        