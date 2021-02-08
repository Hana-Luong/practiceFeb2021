// Given an array like
statues = [6, 2, 3, 8];
// How many more numbers needed to make [2, 3, 4, 5, 6, 7, 8]?


var max, min;
var howMany = 0;
function makeArrayConsecutive1(statues){
  max = statues[0];
  min = statues[0];
  for (i = 1; i < statues.length; i++){
    //Step 1: Find max
    if (statues[i] > statues[0]){
      max = statues[i];
    }
    //Step 2: Find min
    if (statues[i] < statues[0]){
      min = statues[i];
    }
  }
  //Step 3: max - min + 1 - length of given array
  howMany = max - min + 1 - statues.length;
  return howMany;
}
console.log(makeArrayConsecutive1); 

function makeArrayConsecutive2(statues) {
  return Math.max.apply(null, statues) - Math.min.apply(null, statues) - statues.length + 1;
}



