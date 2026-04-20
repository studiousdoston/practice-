/*B-TASK (NodeJS)
⭐️ SAVOL: Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/

// ⭐️ Masalaning yechimi
function countNums(str) {
  return str.split("").map(Number).filter(Boolean).length;
}
console.log(countNums("ad2a54y79wet0sfgb9"));

//====================================================================================

/*CHALLANGE TASK: Animals 
⭐️ SAVOL shunday bir funksiya tuzingki unga berilgan argumentdagi harflarni hayvonlar arrayida hayvonlarni harflari bilan solishtirsin va mos kelganlaridan yangi bir array hosil qisin
*/

//⭐️ Masalaning yechimi
const animals = ["fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog", "hen", "mole", "duck", "goat", "dog", "cat", "bat", "cow"];
function findAnimals(word) {
  const animal = animals.map(ele => ele.split(""));
  const letters = word.split("");
  let arrayOfAnimals = [];
  for (let i = 0; i < animal.length; i++) {
    if (animal[i].every(letter => word.includes(letter))) {
      arrayOfAnimals.push(animal[i].join(""))
    }
  }
  return arrayOfAnimals;
};
const foundAnimals = findAnimals("fdgwoalt");
console.log(foundAnimals)

//====================================================================================

// /*A-TASK (NodeJS)
// ⭐️Savol:Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
// MASALAN countLetter("e", "engineer") 3ni return qiladi.
//  */


// // ⭐️ Masalaning yechimi
// function countLetters(char, str) {
//   const splitted = str.split(""); //array
//   const filtered = splitted.filter(ele => ele === char);
//   return filtered.length;
// }
// console.log(countLetters("e", "engineering"));



