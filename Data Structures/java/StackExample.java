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