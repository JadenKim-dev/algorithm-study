def num_to_bin(num):
    return bin(num)[2:]

def get_perfect_tree_size(num):
    curr = 1
    while curr - 1 < num:
        curr *= 2
    return curr - 1

def fill_with_zero(binary, length):
    return (length - len(binary)) * '0' + binary

# 부모가 0이라면, 그 자식 요소들은 모두 0이어야 함
# 부모는 전체 범위의 정중앙의 수임
# 재귀적으로 범위를 반씩 쪼개가면서, 조건을 만족하는지 테스트
    # 부모가 0이면 자식들이 모두 0인지 확인
    # 부모가 1이면 그냥 pass

def is_all_zero(binary):
    return '1' not in binary
    
def is_valid(binary):
    if len(binary) == 1:
        return True
    middle = len(binary) // 2
    if binary[middle] == '0':
        return is_all_zero(binary[:middle]) and is_all_zero(binary[middle+1:])
    else:
        return is_valid(binary[:middle]) and is_valid(binary[middle+1:])

def solution(numbers):
    answer = []
    for num in numbers:
        binary = num_to_bin(num)
        floor_mult = get_perfect_tree_size(len(binary))
        binary = fill_with_zero(binary, floor_mult)
        answer.append(1 if is_valid(binary) else 0)
        
    return answer
