var groupAnagrams = function(strs) {
    let map = new Map();
    let ans = []
    
    for (let i = 0; i < strs.length; i++) {
        let temp = strs[i].split('').sort().join('');
        
        if (map.has(temp)) {
            let original = map.get(temp)
            original.push(strs[i])
            map.set(temp, original)
        } else {
            map.set(temp, [strs[i]])
        }
    }
    
    for (const item of map.keys()) {
        ans.push(map.get(item))
    }
    
    console.log(ans)
    return ans
};