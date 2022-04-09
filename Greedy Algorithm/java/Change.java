import java.util.*;

class Change {  
  public static void main(String[] args) {
    int[] coinTypes = {500, 100, 50, 10};
    
    Scanner scanner = new Scanner(System.in);
    int change = scanner.nextInt();
    int answer = 0;

    for (int coinType: coinTypes) {
      answer += change / coinType;
      change = change % coinType;
    }

    System.out.println(answer);    
  }
}