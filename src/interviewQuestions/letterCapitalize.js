/*
Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space.
    */
function LetterCapitalize(str) { 
  var newStr = ""
  var lastEle = str.split(" ")[str.length - 1]
  
  for (var pet of str.split(" ")) {
    if (pet === lastEle) {
      newStr += pet.charAt(0).toUpperCase() + pet.sclice(1)
    }
    else {
      newStr += (pet.charAt(0).toUpperCase() + pet.slice(1) + " ")
    }
  }

  // code goes here  
  return newStr; 

}
   
// keep this function call here 
console.log(LetterCapitalize(readline()));
