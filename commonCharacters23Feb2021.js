/* function commonCharacters(str1, str2){
    let result_string = []; 
    let count = 0;
    for(i=0; i<str1.length; i++){
        let char = str1[i];
        for(j=0; j<str2.length; j++){
            if( !result_string.includes(char) && (char == str2[j])){
                result_string.push(char);
                console.log(result_string);//just to check
                count ++;
            }
          }
    }
    return count;
}
console.log(commonCharacters("aabbccddefg","aaacccchhh")); */

//https://stackoverflow.com/questions/55079818/common-character-count-in-strings-javascript
function commonCharacterCount(s1, s2) {
    var count = 0;
    s1 = s1.split('');
    console.log(s1);
    s2 = s2.split('');
    console.log(s2);    
    s1.forEach(e => {
    /* forEach is like to call keys-values pairs */
      if (s2.includes(e)) {
        count++;
        s2.splice(s2.indexOf(e), 1);
        /* array.splice(index, howMany, [element1][, ..., elementN]);
        index − Index at which to start changing the array.
        howMany − An integer indicating the number of old array elements to remove. 
            If howMany is 0, no elements are removed.
        element1, ..., elementN − The elements to add to the array. If you dont specify any elements,
            splice simply removes the elements from the array. */
        console.log(s2);
      }
    });        
    return count;
}
console.log(commonCharacterCount("aabcc", "adcaa"));
