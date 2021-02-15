//Given an array, find the largest product of two adjacent numbers.

function maxProduct(arr){
    var max = arr[0]*arr[1];
    var firstNum = 0;
    var secondNum = 0;
    for (var i=1;i<arr.length;i++){
        if(max<arr[i]*arr[i+1]){
           max=arr[i]*arr[i+1];
           firstNum i;
           secondNum = i+1;
        }      
    }
    return [max,firstNum, secondNum];
}

console.log(maxProduct([9,8,6,7,9,10,12,9])); 

// NEED TO REVIEW CALLBACK FUNCTION AND ARROW FUNCTION
let adjacentElementProduct = () => {
    let arr = inputArray;
    let product = arr[0] * arr[1];
    for (let i = 0; i < arr.length - 1; i++) {
        product = Math.max(product, arr[i] * arr[i+1]);
    }
    return product;
}