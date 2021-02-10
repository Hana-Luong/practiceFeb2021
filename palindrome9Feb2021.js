stringy_string1 = 'radar' 
stringy_string2 = 'yes'
// Iterative Method (using a for loop)

function palindromeOrNot(str){
    for(i=0; i < Math.floor(str.length/2); i++){
        if (str[i] != str[str.length-i-1]){
            return false;
        }
        return true;
    }
}

let str = '';
let isPalindrome = () => {
    for(let i = 0; i<str.length/2; i++){
        if(str[i] != str[str.length-i-1]){
            return false;
        }
    }
    return true;
}
isPalindrome();


console.log(palindromeOrNot(stringy_string1));
console.log(palindromeOrNot(stringy_string2));