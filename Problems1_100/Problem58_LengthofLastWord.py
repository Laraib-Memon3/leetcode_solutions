class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1, -1, -1):   # loop backwards
            if s[i] == ' ':                 # check if current char is space
                if count > 0:               # if we already counted a word
                    return count            # return length of last word
            else:
                count = count + 1           # count letters of last word
        
        return count                        # return if loop ends
  

# explanation along with DRY RUN
# Dry Run Example
# Input: s = "Hello World"

# Start from last character → 'd' → not space → count = 1.

# 'l' → not space → count = 2.

# 'r' → not space → count = 3.

# 'o' → not space → count = 4.

# 'W' → not space → count = 5.

# ' ' (space) → since count > 0, return 5.

# ✅ Output = 5 → correct.



# Input:
# s = " fly me to the moon "

# We need the length of the last word → "moon" → length = 4.
# String length = 27, so loop starts at index 26 (last character).

# Index 26 → ' ' (space) → count = 0, skip.

# Index 25 → ' ' (space) → still skip.

# Index 24 → 'n' → not space → count = 1.

# Index 23 → 'o' → not space → count = 2.

# Index 22 → 'o' → not space → count = 3.

# Index 21 → 'm' → not space → count = 4.

# Index 20 → ' ' (space) → since count > 0, return 4.

# ✅ Output = 4.