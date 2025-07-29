/**
* Problem Name: 389. Find the Difference
* Attempted : # 30-07-2025
*/

/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function (s, t) {
    const splitt = t.split("")
    for (let i = 0; i < s.length; i++) {
        const index = splitt.indexOf(s[i]);
        if (index > -1) { // only splice array when item is found
            splitt.splice(index, 1); // 2nd parameter means remove one item only
        }
    }
    return splitt[0];
};

console.log(findTheDifference("abcd", "abcde"))
console.log(findTheDifference("", "y"))