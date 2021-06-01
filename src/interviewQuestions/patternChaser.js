/*
Have the function PatternChaser(str) take str which will be a string and return the longest pattern within the string. A pattern for this challenge will be defined as: if at least 2 or more adjacent characters within the string repeat at least twice. So for example "aabecaa" contains the pattern aa, on the other hand "abbbaac" doesn't contain any pattern. Your program should return yes/no pattern/null. So if str were "aabejiabkfabed" the output should be yes abe. If str were "123224" the output should return no null. The string may either contain all characters (a through z only), integers, or both. But the parameter will always be a string type. The maximum length for the string being passed in will be 20 characters. If a string for example is "aa2bbbaacbbb" the pattern is "bbb" and not "aa". You must always return the longest pattern possible.
*/
    


//This is a question where the o(n) complexity could explode if not coded proprely
// There's two possibilities Regex or recursion

function PatternChaser(str) { 
  // code goes here  
  //default answer
  answer = 'null';
  // the regex is not perfect and often misses important sub group
  let re = /(\w+).+(\1)/g;
  var reResults = re.exec(str);
  // since it catches duplicates we will identify them and return them
  //console.log(reResults)
  var tempArray = [];
  reResults.forEach(function(val) {
     if (tempArray[val]){
       // because there are alot of issues with the regex that I use I haven't optimizedd
       // for the largest repeated value
       answer = 'yes '+val

     }
     else {
       tempArray[val] = true;
     }
     });


  return answer;

}
   
// keep this function call here 
console.log(PatternChaser(readline()));
