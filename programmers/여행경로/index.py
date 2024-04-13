from collections import defaultdict


def solution(tickets):
    ticket_dict = defaultdict(list)
    for begin, end in tickets:
        ticket_dict[begin].append(end)
    for begin in ticket_dict.keys():
        ticket_dict[begin].sort()

    def dfs(curr, path, ticket_dict):
        if len(path) == len(tickets)+1:
            return path
        for idx, dest in enumerate(ticket_dict[curr]):
            del ticket_dict[curr][idx]
            path_tmp = path[:]
            path_tmp.append(dest)
            result = dfs(dest, path_tmp, ticket_dict)
            if result:
                return result
            ticket_dict[curr].insert(idx, dest)
        return []

    curr, path = "ICN", ["ICN"]
    return dfs(curr, path, ticket_dict)