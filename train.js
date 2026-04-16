/*A-TASK (NodeJS)

⭐️Savol:Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi. */


//⭐️SOLUTION
function countLetters(char, str){
  const splitted = str.split(""); //array
  const filtered = splitted.filter(ele=>ele===char);
  return filtered.length
}

//⭐️RESULT 
console.log(countLetters("e","engineering"));
