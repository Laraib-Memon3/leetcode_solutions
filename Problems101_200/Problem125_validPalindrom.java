class Solution {
    // Method to check if a given string is a palindrome, considering only alphanumeric characters and ignoring cases
    public boolean isPalindrome(String s) {
        // Convert the string to lowercase to make the comparison case-insensitive
        s = s.toLowerCase();

        StringBuilder sb = new StringBuilder();
        // Iterate through each character in the string
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // Append only alphanumeric characters to the StringBuilder
            if ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')) {
                sb.append(c);
            }
        }

        int left = 0;
        int right = sb.length() - 1;

        // Use two pointers to compare characters from both ends
        while (left <= right) {
            // If characters at the current pointers do not match, it's not a palindrome
            if (sb.charAt(left) != sb.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        // If all characters matched, it's a palindrome
        return true;
    }
}
// time complexity = O(n)
// space complexity = O(n)