#import copy

# Key rotation logic
def rotation(key):
    m = len(key)
    rotated_key = [[0] * m for _ in range(m)]
    #tmp_key = copy.deepcopy(key)
    
    for i in range(m):
        for j in range(m):
            rotated_key[j][m - 1 - i] = key[i][j]
    
    return rotated_key

# check if key is matched with lock according to shift
def check_key(key, lock):
    m = len(key)
    n = len(lock)
    
    # shift_i from 0 to n + m -2
    # shift_j from 0 to n + m -2
    for shift_i in range(n + m - 1):
        for shift_j in range(n + m - 1):
            matched = True
            x = m - 1 - shift_i
            y = m - 1 - shift_j
            for i in range(n):
                for j in range(n):
                    if (x + i >= 0 and x + i <= m - 1 and 
                        y + j >= 0 and y + j <= m - 1):
                       key_value = key[x + i][y + j]
                    else:
                       key_value = 0
                    key_result = key_value + lock[i][j]
                    
                    if key_result != 1:
                        matched = False
                        break
                if not matched:
                    break
            if matched:
                return True
    return False

def solution(key, lock):
    # Check key without rotation
    answer = check_key(key, lock)
    
    if answer:
        return answer
    
    # Check key with 90, 180, 270 degree
    for _ in range(3):       
        key = rotation(key)
        answer = check_key(key, lock)
    
        if answer:
            return answer
    
    return answer

if __name__ == '__main__':
  key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
  lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

  result = solution(key, lock)

  print("result: {}".format(result))