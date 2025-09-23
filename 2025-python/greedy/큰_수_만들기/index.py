def solution(number, k):
    is_omitted = True
    while k and is_omitted:
        is_omitted = False
        for i in range(len(number) - 1):
            if number[i] < number[i+1]:
                number = number[:i] + number[i+1:]
                k -= 1
                is_omitted = True
                break
        if not is_omitted:
            break

    return number[:-k] if k > 0 else number

# --------------

def solution(number, k):
    stack = []
    for n in number:
        while k > 0 and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    result = stack[:-k] if k > 0 else stack
    return ''.join(result)
