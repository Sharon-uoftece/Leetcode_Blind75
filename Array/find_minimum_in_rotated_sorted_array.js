var findMin = function(nums) {
    let length = nums.length;
    if (length == 0) {
        return nums[0];
    };
    
    let ref = nums[0]
    let ans = 0;

    for(let i = 1; i < length; i++) {
        if (nums[i] < ref) {
            ans = i;
        }
        ref = nums[i];
    }

    
    console.log("min position", ans);
    return nums[ans];
};