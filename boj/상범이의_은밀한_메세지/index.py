alpha_dict = {alpha:i for alpha, i in zip('abcdefghijklmnopqrstuvwxyz', range(26))}
alpha_list = [c for c in 'abcdefghijklmnopqrstuvwxyz']

encrypted = input()
origin = input()

def get_key_size(diff_list):
    for size in range(1, len(diff_list)//2 + 1):
        key = ''.join(diff_list[:size])
        is_wrong = False
        for i in range(size, len(diff_list), size):
            target = ''.join(diff_list[i:i+size])
            if not key.startswith(target):
                is_wrong = True
                break
        if not is_wrong:
            return size
    return 0

def get_key_line(idx, size, diff_list):
    key_idx = idx % size
    key = diff_list[size-key_idx:size] + diff_list[:size-key_idx]
    return (key*(len(encrypted)//size + 1))[:len(encrypted)]

for idx in range(len(encrypted) - len(origin) + 1):
    diff_list = []
    for j in range(len(origin)):
        diff = alpha_dict[encrypted[idx + j]] - alpha_dict[origin[j]]
        diff = diff if diff >= 0 else diff + 26
        diff_list.append(str(diff))
    size = get_key_size(diff_list)
    if size > 0:
        diff_list = [int(x) for x in diff_list]
        key_line = get_key_line(idx, size, diff_list)
        ans = []
        for i in range(len(encrypted)):
            alpha_idx = alpha_dict[encrypted[i]] - key_line[i]
            alpha_idx = alpha_idx if alpha_idx >= 0 else alpha_idx+26
            ans.append(alpha_list[alpha_idx])
        print(''.join(ans))
        break