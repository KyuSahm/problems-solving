'''
���� ���� - N���� ǥ��
�Ʒ��� ���� 5�� ��Ģ���길���� 12�� ǥ���� �� �ֽ��ϴ�.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5�� ����� Ƚ���� ���� 6,5,4 �Դϴ�. �׸��� ���� ���� ���� ���� 4�Դϴ�.
��ó�� ���� N�� number�� �־��� ��, N�� ��Ģ���길 ����ؼ� ǥ�� �� �� �ִ� ��� �� N ���Ƚ���� �ּڰ��� return �ϵ��� solution �Լ��� �ۼ��ϼ���.

���ѻ���
N�� 1 �̻� 9 �����Դϴ�.
number�� 1 �̻� 32,000 �����Դϴ�.
���Ŀ��� ��ȣ�� ��Ģ���길 �����ϸ� ������ ���꿡�� �������� �����մϴ�.
�ּڰ��� 8���� ũ�� -1�� return �մϴ�.
����� ��
N	number	return
5	12	4
2	11	3
����� �� ����
���� #1
������ ���� ���� �����ϴ�.

���� #2
11 = 22 / 2�� ���� 2�� 3���� ����Ͽ� ǥ���� �� �ֽ��ϴ�.

��ó

�� ���� - 2020�� 9�� 3�� �׽�Ʈ���̽��� �߰��Ǿ����ϴ�.
'''
def solution(N, number):
    if number == N:
        return 1    
    
    f = [set() for _ in range(9)]
    f[1].add(N)

    for i in range(2, 9):
        result = ''
        for _ in range(i):
            result += str(N)
        f[i].add(int(result))

        for j in range(1, i):
            k = i - j
            for x in f[j]:
                for y in f[k]:
                    result = x + y
                    f[i].add(result)
                    result = x - y
                    f[i].add(result)
                    result = x * y
                    f[i].add(result)

                    if y != 0:
                        result = x // y
                        f[i].add(result)
        if number in f[i]:
            return i
    return -1

if __name__ == '__main__':
  print(solution(5, 12))
  print(solution(2, 11))
