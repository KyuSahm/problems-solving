'''
���� ���� - ī��
Leo�� ī���� �緯 ���ٰ� �Ʒ� �׸��� ���� �߾ӿ��� ��������� ĥ���� �ְ� �׵θ� 1���� �������� ĥ���� �ִ� ���� ��� ī���� �ý��ϴ�.
Leo�� ������ ���ƿͼ� �Ʊ� �� ī���� ������� �������� ��ĥ�� ������ ������ ���������, ��ü ī���� ũ��� ������� ���߽��ϴ�.
Leo�� �� ī�꿡�� ���� ������ �� brown, ����� ������ �� yellow�� �Ű������� �־��� �� ī���� ����, ���� ũ�⸦ ������� �迭�� ��� return �ϵ��� solution �Լ��� �ۼ����ּ���.

���ѻ���
���� ������ �� brown�� 8 �̻� 5,000 ������ �ڿ����Դϴ�.
����� ������ �� yellow�� 1 �̻� 2,000,000 ������ �ڿ����Դϴ�.
ī���� ���� ���̴� ���� ���̿� ���ų�, ���� ���̺��� ��ϴ�.

����� ��
brown	yellow	return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]
'''
def solution(brown, yellow):    
    answer = [1, 1]
    yellow_x = 1

    while True:
      if yellow % yellow_x == 0:
        yellow_y = int(yellow / yellow_x)
        brown_cnt = (yellow_x + 2) * 2 + yellow_y * 2

        if brown_cnt == brown:
            x = yellow_x + 2
            y = yellow_y + 2
            answer = [y, x]
            break
      yellow_x += 1  
    return answer

if __name__ == '__main__':
  print(solution(10, 2))
  print(solution(8, 1))
  print(solution(24, 24))
