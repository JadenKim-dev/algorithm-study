def solution(phone_book):
    phone_book.sort()
    for idx in range(len(phone_book) - 1):
        if phone_book[idx+1].startswith(phone_book[idx]):
            return False
    return True

# --------------------------------

def solution(phone_book):
    phone_book.sort()
    return not any(b.startswith(a) for a, b in zip(phone_book, phone_book[1:]))