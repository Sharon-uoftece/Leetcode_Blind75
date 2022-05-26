/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (n === 1) {
        return 1;
    } else if (n == 2) {
        return 2;
    }
    
    let ans = Array(n).fill(0);
    ans[0] = 1;
    ans[1] = 2;
    
    for (let i = 2; i < n; i += 1) {
        ans[i] = ans[i-1] + ans[i-2];
    }
    
    console.log(ans);
    
    return ans[ans.length - 1];
};