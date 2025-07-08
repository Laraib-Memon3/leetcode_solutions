class Solution {
   public int removeDuplicates(int[] nums) {
        int[] expectednums = new int[nums.length];
 
        int count=0;
        for(int j=0; j<nums.length; j++){
            for(int i=j+1; i<nums.length; i++){
                if(nums[j] == nums[i]){
                    continue;
            }
            else{
                expectednums[j] = nums[i];
                count++;
              //  System.out.println( expectednums[j]);
            }
            }
    }

    return count;}
    }
//time complexity: O(n^2)
//space complexity: O(n)
class Solution2 {
public int removeDuplicates(int[] nums) {
int left = 1;
for (int right = 1; right < nums.length; right++) {
    if(nums[right] != nums[right - 1]) {
        nums[left] = nums[right];
        left++;
    }
}
return left;
}}

//time complexity: O(n)
//space complexity: O(1)