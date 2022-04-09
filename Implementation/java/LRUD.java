import java.util.*;

class LRUD {  
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int n = Integer.parseInt(scanner.nextLine());
    String line = scanner.nextLine();
    String[] directions = line.split(" ");

    int x = 1, y = 1;

    for (String direction: directions) {
      int nextX = 0, nextY = 0;
      switch (direction) {
        case "L":
          nextX = x;
          nextY = y - 1;
          break;
        case "R":
          nextX = x;
          nextY = y + 1;
          break;
        case "U":  
          nextX = x - 1;
          nextY = y;
          break;
        case "D":  
          nextX = x + 1;
          nextY = y;
          break;
      }

      if (nextX > n || nextX < 1 || nextY > n || nextY < 1) {
        continue;
      }

      x = nextX;
      y = nextY;
    }

    System.out.printf("answer (%d, %d)\n", x, y);
  }
}