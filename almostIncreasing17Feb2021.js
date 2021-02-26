function almostIncreasingSequence(sequence){
  let temp = 0;
  for (i=1; i<sequence.length; i++){
    if (sequence[i]<sequence[i-1]){
      temp++;
      if(temp>1){
        return false;
      }
      if(sequence[i]<=sequence[i-2] && sequence[i+1]<=sequence[i-1]){
        return false;
      }     
    }
  }
  if(temp <= 1){
    return true;
  } 
}
console.log(almostIncreasingSequence([1,3,2,1])); // false
console.log(almostIncreasingSequence([1,3,2])); // true
console.log(almostIncreasingSequence([3,2,1])); // false
console.log(almostIncreasingSequence([1,2,3,2])); // true



/* let count = 0;

for(let i=0; i< sequence.length; i++){

  // check 1 : n is smaller or equal to n-1
  if(sequence[i] <= sequence[i-1]){
    count++;
    // n is smaller or equal to n-2 and n+1 is smaller or equal to n-1
    if(sequence[i] <= sequence[i-2] && sequence[i+1] <= sequence[i-1]){
      count++;
    }
  }
}

// return true with 1 or no remove, otherwise false
return count <= 1;
}


console.log(almostIncreasingSequence([1,3,2,1])); // false
console.log(almostIncreasingSequence([1,3,2])); // true
console.log(almostIncreasingSequence([3,2,1])); // false
console.log(almostIncreasingSequence([1,2,3,2])); // true */