package week_2;

import java.util.HashMap;
import java.util.Map;

/**
 * LeetCode 242. Valid Anagram
 * 문제: 2개의 단어가 주어졌을때 두 단어가 애너그램 문자라면 True, 아니면 false를 반환해라
 */
public class IsAnagram {

	public static void main(String[] args) {
		IsAnagram isAnagram = new IsAnagram();
		boolean anagram1 = isAnagram.isAnagram("anagram", "nagaram");
		System.out.println(anagram1);
		boolean anagram2 = isAnagram.isAnagram("rat", "car");
		System.out.println(anagram2);
	}

	public boolean isAnagram(String s, String t) {
		if (s.length() != t.length()) return false;

		Map<Character, Integer> map = new HashMap<>();

		for (int i = 0; i < s.length(); i++) {
			map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
		}

		for (int i = 0; i < t.length(); i++) {
			if (!map.containsKey(t.charAt(i))) return false;

			map.put(t.charAt(i), map.get(t.charAt(i)) - 1);
			if (map.get(t.charAt(i)) == 0) {
				map.remove(t.charAt(i));
			}
		}
		return map.isEmpty();
	}
}
