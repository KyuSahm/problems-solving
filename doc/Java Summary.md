# 문법 정리
## 입력 받기
- ``import java.util.*``
- 정수 입력 받기
```java
import java.util.*;

class Change {  
  public static void main(String[] args) {
    .....
    Scanner scanner = new Scanner(System.in);
    int change = scanner.nextInt();    
  }
}
```
- 첫 번째 라인에서 정수 입력 받고, 다음 라인에서 문자열 입력 받아 토큰 분리
```java
// 방법 1
int n = Integer.parseInt(scanner.nextLine());
String line = scanner.nextLine();
String[] directions = line.split(" ");

// 방법 2
int n = scanner.nextInt();
scanner.nextLine(); // 버퍼 비우기
String[] directions = scanner.nextLine().split(" ");
```
## Stack
- ``import java.util.*``
- ``Stack<E> stack = new Stack<>();``
- ``stack.push(E element)``: element를 스택에 추가
- ``E element = stack.pop()``: element를 스택에서 제거
- ``E element = stack.peek()``: 최상위 element를 가져옴. 제거는 않함
- ``Boolean isEmpty = stack.isEmpty()``: 스택이 비었는지 체크
```java
import java.util.*;

class Coin {
  private int value;

  Coin(int value) {
    this.value = value;
  }

  public int getValue() {
    return this.value;
  }
}

class StackExample {
  public static void main(String[] args) {
    Stack<Coin> coinBox = new Stack<>();

    coinBox.push(new Coin(100));
    coinBox.push(new Coin(50));
    coinBox.push(new Coin(500));
    coinBox.push(new Coin(10));

    while (!coinBox.isEmpty()) {
      Coin coin = coinBox.peek();
      System.out.println("coin at top: " + coin.getValue());

      coin = coinBox.pop();
      System.out.println("popped coin: " + coin.getValue());
    }
  }
}
```
## Queue
- ``import java.util.*``
- ``Queue<E> queue = new LinkedList<>();``: Queue Interface를 구현한 대표적인 클래스
- ``queue.offer(E element)``: element를 queue에 추가
- ``E element = queue.poll()``: element를 queue에서 제거
- ``E element = queue.peek()``: header에 위치한 element를 가져옴. 제거는 않함
- ``Boolean isEmpty = queue.isEmpty()``: queue가 비었는지 체크
```java
import java.util.*;

class Coin {
  private int value;

  Coin(int value) {
    this.value = value;
  }

  int getValue() {
    return this.value;
  }
}

class QueueExample {
  public static void main(String[] args) {
    Queue<Coin> coinBox = new LinkedList<>();

    coinBox.offer(new Coin(100));
    coinBox.offer(new Coin(50));
    coinBox.offer(new Coin(500));
    coinBox.offer(new Coin(10));

    while (!coinBox.isEmpty()) {
      Coin coin = coinBox.peek();
      System.out.println("Coin at head: " + coin.getValue());

      coin = coinBox.poll();
      System.out.println("polled Coin: " + coin.getValue());
    }
  }
}
```