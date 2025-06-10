package week_2;

/**
 * LeetCode 70. Climbing Stairs
 */
public class ClimbStairs {

	public static void main(String[] args) {
		ClimbStairs climbStairs = new ClimbStairs();
		int result = climbStairs.climbStairs(1);
		System.out.println(result);
	}

	public int climbStairs(int n) {
		if (n < 3) return n;

		int pre = 1, cur = 2;
		for (int i = 0; i < n - 2; i++) {
			int next = pre + cur;
			pre = cur;
			cur = next;
		}

		return cur;
	}
}
