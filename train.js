/*A-TASK (NodeJS)

⭐️Savol:Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi. */


//⭐️SOLUTION
function countLetters(char, str) {
  const splitted = str.split(""); //array
  const filtered = splitted.filter(ele => ele === char);
  return filtered.length
}

//⭐️RESULT 
console.log(countLetters("e", "engineering"));


//*B-TASK (NodeJS)

//SAVOL: Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
// MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.

//⭐️SOLUTION
function countNums(str) {
  return str.split("").map(Number).filter(Boolean).length
}

//⭐️RESULT
console.log(countNums("ad2a54y79wet0sfgb9"))

/*
const str = "ad2a54y79wet0sfgb9";
const arr = str.split("")
const nums = arr.map(Number).filter(Boolean)
console.log(nums.length)
*/