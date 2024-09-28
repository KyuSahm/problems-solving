#
# KAKAO 괄호 변환
def process(u, v):
    if len(u) == 0:
        return ''

    if is_correct(u):
        ans = u
    else:
        ans = correct(u)

    index = find_sep_index(v)
    nu = v[:index]
    nv = v[index:]

    ans += process(nu, nv)

    return ans;

def correct(u):
    u_center = u[1:-1]

    rtn = '('
    for c in u_center:
        if c == '(':
            rtn += ')'
        else:
            rtn += '('
    rtn += ')'
    return rtn

def is_correct(u):
    cnt = 0
    for c in u:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False
    return True


def find_sep_index(str):
    cnt = 0
    for i in range(len(str)):
        if str[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            return i + 1
    return 0

if __name__ == '__main__':
    s = input()

    index = find_sep_index(s)
    u = s[:index]
    v = s[index:]

    answer = process(u, v)
    print(answer)