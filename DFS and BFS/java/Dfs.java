import java.util.*;

class Dfs {
  private static boolean[] visited = new boolean[9];
  private static int[][] graph = new int[9][];
  private static List<Integer> nodeList = new ArrayList<>();

  private static void dfsOnRecursion(int index) {
    visited[index] = true;
    nodeList.add(index);    
    for (int i : graph[index]) {
      if (visited[i]) continue;
      dfsOnRecursion(i);
    }
  }

  private static void dfsOnStack() {
    Stack<Integer> stack = new Stack<>();
    
    visited[1] = true;    
    nodeList.add(1);
    stack.push(1);

    while (!stack.isEmpty()) {
      int index = stack.peek();

      boolean found = false;
      for (int i : graph[index]) {
        if (!visited[i]) {
          visited[i] = true;          
          nodeList.add(i);
          stack.push(i);
          found = true;
          break;
        }    
      }

      if (!found) {
        stack.pop();
      }      
    }
  }
  
  public static void main(String[] args) {
    graph[0] = new int[0];
    graph[1] = new int[]{2, 3, 8};
    graph[2] = new int[]{1, 7};
    graph[3] = new int[]{1, 4, 5};
    graph[4] = new int[]{3, 5};
    graph[5] = new int[]{3, 4};
    graph[6] = new int[]{7};
    graph[7] = new int[]{2, 6, 8};
    graph[8] = new int[]{1, 7};

    //dfsOnRecursion(1);
    dfsOnStack();

    for (int node: nodeList) {
      System.out.println(node + " ");
    }    
  }
}