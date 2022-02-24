
def fileParser(path):
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
                    contribs[name].append([line[0], int(line[1])])
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
        return contribs, projs




fileParser(r'C:\Users\manji\PycharmProjects\HashCodeQualifiers\input_data\b_better_start_small.in.txt')