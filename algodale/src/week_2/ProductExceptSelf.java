package week_2;

import java.util.Arrays;
/**
 * LeetCode 238. Product of Array Except Self
 */
public class ProductExceptSelf {
	public static void main(String[] args) {
		ProductExceptSelf productExceptSelf = new ProductExceptSelf();
		int[] ints1 = productExceptSelf.productExceptSelf(new int[] {1, 2, 3, 4});
		System.out.println(Arrays.toString(ints1));

		int[] ints = productExceptSelf.productExceptSelf(new int[] {-1,1,0,-3,3});
		System.out.println(Arrays.toString(ints));
	}
	public int[] productExceptSelf(int[] nums) {
		int n = nums.length;
		int[] products = new int[n];

		// 1. 초기값을 모두 1로 설정
		for (int i = 0; i < n; i++) {
			products[i] = 1;
		}

		// 2. 왼쪽 곱 누적
		int before = 1;
		for (int i = 0; i < n - 1; i++) {
			before *= nums[i];
			products[i + 1] *= before;
		}

		// 3. 오른쪽 곱 누적
		int after = 1;
		for (int i = n - 1; i > 0; i--) {
			after *= nums[i];
			products[i - 1] *= after;
		}

		return products;
	}
}
