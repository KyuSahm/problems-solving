import time
import operator

def find_next_job(jobs, prev_end_time):
    min_index = -1
    min_take_time = 1e9
    
    i = 0 
    while i < len(jobs):
        start_time, take_time = jobs[i]
        if start_time < prev_end_time and take_time < min_take_time:
            min_take_time = take_time
            min_index = i
        elif start_time > prev_end_time:
            break
        i += 1        
        
    return min_index
        
def solution(jobs):
    # jobs list를 index 0에 대해 오름차순 후, index 1에 대해서 오름차순
    jobs.sort(key=operator.itemgetter(0, 1))
    answer = 0
    jobs_len = len(jobs)
    #print(jobs)
    
    current_time = 0
    while len(jobs) > 0:
        next_job_index = find_next_job(jobs, current_time)
        
        if next_job_index == -1:
           start_time, take_time = jobs.pop(0)
           current_time = start_time + take_time
           answer += take_time     
        else:
           start_time, take_time = jobs.pop(next_job_index)
           if start_time <= current_time:
              current_time = current_time + take_time
              answer += current_time - start_time
           else:
              current_time = start_time + take_time
              answer += take_time 
    
    answer = int(answer/jobs_len)
    #print(answer)    
    
    return answer

if __name__ == '__main__':
  startTime = time.time()
  a = [[0, 3], [1, 9], [2, 6]]
  print("first solution: {}".format(solution(a)))

  a = [[1, 3], [1, 8], [2, 6]]
  print("first solution: {}".format(solution(a)))

  a = [[0, 3], [1, 9], [4, 6]]
  print("first solution: {}".format(solution(a)))


  endTime = time.time()