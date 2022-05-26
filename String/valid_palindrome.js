ar isPalindrome = function(s) {
    if (s == ' ') {
        return true
    }
    let ans = '';
    let str = s.toLowerCase();
    console.log("original",s)
    console.log("after",str)
    
    for (let i = 0; i < s.length; i++) {
        let ch = str.charAt(i);
        if ((ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9')) {
            ans += ch;
        }
    }
    let i = 0;
    let j = ans.length - 1;
    
    while (i <= j) {
        if(ans[i] != ans[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true
};