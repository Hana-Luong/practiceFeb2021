keys = ["abc", 3, "yo"];
values = [42, "wassup", "something"];
// https://stackoverflow.com/questions/39127989/creating-a-javascript-object-from-two-arrays/39128136


var result = {};
keys.forEach((key, i) => result[key] = values[i]); //review callback function
console.log(result);