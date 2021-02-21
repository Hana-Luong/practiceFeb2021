/**
 * takes in two strings
 * returns a boolean
 * are the two strings equal irrespective of case
 */

function caseInsensitiveStringCompare(str1, str2) {
  // your code here
}

console.log(caseInsensitiveStringCompare('This', 'this'));
// should log true
console.log(caseInsensitiveStringCompare('this', 'that'));
// should log false


/**
 * takes in a string
 * returns a string
 * return will be first letter of each "word"
 * capitalized
 */

function acronyms(str) {
  // your code here
}

'hello'.toUpperCase(); // returns 'HELLO'

console.log(acronyms("there's no free lunch - gotta pay yer way."));
// should log 'TNFL-GPYW'
console.log(acronyms("Live from New York, it's Saturday Night!"));
// should log 'LFNYISN'


/**
 * takes in a string
 * returns the string
 * with the character order reversed
 */

function stringReverse(str) {
  // your code here
}

console.log(stringReverse('this')); // should log 'siht'
console.log(stringReverse('something')); // should log 'gnihtemos'