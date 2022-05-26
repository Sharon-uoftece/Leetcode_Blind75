var productExceptSelf = function(nums) {
    console.log(nums);
    
    let ans = Array(nums.length).fill(0);
    let temp = 1;
    let zeroCount = 0;
    let mark1 = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == 0 && zeroCount == 0) {
            zeroCount += 1;
            mark1 = i;
            continue;
        } else if (nums[i] == 0 && zeroCount == 1) {
            return Array(nums.length).fill(0);
        }
        
        if (nums[i] != 0 && zeroCount <= 1) {
            temp = temp * nums[i];
        };
    };
    
    console.log("mark1 is: ",mark1);
    
    for (let j = 0; j < ans.length; j++) {
        if (zeroCount == 1) {
            if (j == mark1) {
                ans[j] = temp;
            } else {
                ans[j] = 0;
            }
        } else {
            ans[j] = temp / nums[j];
        };
    }
    
    console.log(temp);
    return ans;
};