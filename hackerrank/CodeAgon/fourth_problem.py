from collections import deque
query_count = int(input())

for _ in range(query_count):
    program_count, _ = [int(p) for p in input().split()]
    program_graph = {}
    for i in range(1, program_count+1):
        dependencies = [int(p) for p in input().split()]
        program_graph[i] = []
        if dependencies[0] == 0:
            pass
        else:
            program_graph[i] = list(reversed(sorted(dependencies[1:])))
    wanted_programs = [int(p) for p in input().split()]
    # print(program_graph)

    installed_programs = set()
    installed = []
    for wanted_p in wanted_programs:
        # BFS to sort via the nodes with the LEAST dependencies
        currently_installed = []
        queue = deque()
        queue.appendleft(wanted_p)
        while queue:
            node = queue.popleft()
            if node in installed_programs:
                continue
            # # if node in currently_installed:
            # #     currently_installed[currently_installed.index(node)] = None
            # if node in currently_installed:
            #     currently_installed[currently_installed.index(node)] = None
            #     continue
            installed_programs.add(node)
            currently_installed.append(node)
            for dep in program_graph[node]:
                queue.append(dep)
        installed.append(list(reversed(currently_installed)))

    first_list = [item for sublist in installed for item in sublist]
    first_list = list(sorted(first_list, key=lambda x:(len(program_graph[x]), x)))

    new_list = []
    added = set()
    to_add = {

    }
    for i in first_list:
        if len(program_graph[i]) == 0:
            new_list.append(i)
            added.add(i)
        else:
            for dep in program_graph[i]:
                if dep in added:
                    continue
                if len(program_graph[dep]) == 0:
                    new_list.append(dep)
                    added.add(dep)
                else:
                    pass
    print(new_list)
    # print(len(first_list))
    # print(' '.join(str(i) for i in first_list))