from math import gcd

def solution(w,h):
    answer = w * h;
    divi = gcd(w, h);
    answer -= divi * (w//divi + h//divi - 1)
    return answer