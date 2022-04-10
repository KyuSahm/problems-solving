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