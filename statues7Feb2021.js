// Given an array like
//statues = [6, 2, 3, 8];
// How many more numbers needed to make [2, 3, 4, 5, 6, 7, 8]?

function makeArrayConsecutive1(arr){
  var max = arr[0];
  var min = arr[0];
  var howMany = 0;
  for (var i=1;i<arr.length;i++){
    if(max<arr[i]){
        max=arr[i];
    }
    if(min>arr[i]){
        min=arr[i];
    }
  howMany=max-min+1-arr.length;
  }
  return (howMany);
}

console.log(makeArrayConsecutive1([6, 2, 3, 8])); 

// you can return like this
// return [max, min, howMany];



/* function makeArrayConsecutive2(statues) {
  return Math.max.apply(null, statues) - Math.min.apply(null, statues) - statues.length + 1;
}
 */


