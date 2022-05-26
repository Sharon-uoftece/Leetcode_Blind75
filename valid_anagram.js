var isAnagram = function(s, t) {
    console.log(s,t)
    let ans = new Map();
    //has: if key is in the dictionary
    //get: get the value of that key
    //set: set the value of that key
    
    for(let i = 0; i < s.length; i++) {
        if (ans.has(s[i])) {
            ans.set(s[i], ans.get(s[i])+1)
        }
        else {
            ans.set(s[i],1)
        }
    }
    
    for(let i = 0; i < t.length; i++) {
        if (ans.get(t[i]) == 1) {
            ans.delete(t[i]);
        }
        else if(ans.get(t[i]) > 1) {
            ans.set(t[i],ans.get(t[i])-1);
        }
        else {
            return false;
        }
    }
    
    if (ans.size == 0) {
        return true;
    } else{
        return false;
    }
    console.log(ans);
    
};