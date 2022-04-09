import java.util.*;

class CountThreeOnClock {
  private static int solution1(int n) {
    int answer = 0;    
    for (int hour = 0; hour <= n; hour++) {      
      String h = String.valueOf(hour);
      if (h.indexOf("3") == -1)  {
        for (int minute = 0; minute < 60; minute++) {
          String m = String.valueOf(minute);
            if (m.indexOf("3") == -1) {
              for (int second = 0; second < 60; second++) {
                String s = String.valueOf(second);
                if (s.indexOf("3") != -1) {
                  answer += 1;
                }                
              }  
            }
            else {
              answer += 60;
            }
          }
      } else {
        answer += 3600;
      }
    }
    return answer;
  }

  private static int solution2(int n) {
    int answer = 0;    
    for (int hour = 0; hour <= n; hour++) {      
      if (hour / 10 == 3 || hour % 10 == 3)  {
        answer += 3600;
      } else {
        for (int minute = 0; minute < 60; minute++) {
          if (minute / 10 == 3 || minute % 10 == 3)  {
            answer += 60;
          } else {            
            for (int second = 0; second < 60; second++) {
              if (second / 10 == 3 || second % 10 == 3)  {
                answer += 1;
              }                
            }
          }
        }
      }
    }
    return answer;
  }
  
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    
    System.out.println("answer: " + solution2(n));
  }
}