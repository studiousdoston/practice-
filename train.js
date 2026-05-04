/*H-TASK (NodeJS)

shunday function tuzing, u integerlardan iborat arrayni argument sifatida qabul qilib, faqat positive qiymatlarni olib string holatda return qilsin
MASALAN: getPositive([1, -4, 2]) return qiladi "12"
 */

//⭐️ Masalaning yechimi
function getPositive(array) {
  return array.filter(ele => ele > 0).join("")
}
console.log(getPositive([1, -4, 2, -3,]))

//====================================================================================

/*F - TASK(NodeJS)
Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, agar stringda bir hil harf qatnashgan bolsa true, qatnashmasa false qaytarishi kerak.
  MASALAN: getReverse("hello") return true return qiladi
*/
/* ⭐️ Masalaning yechimi
function findDoublers(str) {
  return str.split("").some(letter => str.split("").filter(ele => ele === letter).length > 1)
}
console.log(findDoublers("lovely"))
*/

//====================================================================================

/*E-TASK (NodeJS)

Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"
 */
/*⭐️ Masalaning yechimi
function getReversed(string){
  return string.split("").reverse().join("")
}
console.log(getReversed('lovely'))
*/

//====================================================================================

/*D - TASK(NodeJS)

⭐️ SAVOL: Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
  MASALAN: getHighestIndex([5, 21, 12, 44, 8]) return qiladi 1 sonini.
*/
/*⭐️ Masalaning yechimi
function getHighestIndex(array){
   const highestVal =  Math.max(...array);
   return array.indexOf(highestVal)
 }
console.log(getHighestIndex([5, 21, 12, 44, 8]))
*/
//====================================================================================

/*C-TASK (NodeJS)
⭐️ SAVOL: Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;
*/
/* ⭐️ Masalaning yechimi
 function checkContent(str1, str2){
   if (str1.split('').every(ele => str2.split('').includes(ele)) && str2.split('').every(ele => str1.split('').includes(ele))){
    return true
   }
   else
    return false
 }
console.log(checkContent("mitgroup", "gmtiprou"))
*/

//====================================================================================

/*B-TASK (NodeJS)
⭐️ SAVOL: Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/
/* ⭐️ Masalaning yechimi
function countNums(str) {
  return str.split("").map(Number).filter(Boolean).length;
}
console.log(countNums("ad2a54y79wet0sfgb9"));
*/

//====================================================================================

/*CHALLANGE TASK: Animals
⭐️ SAVOL shunday bir funksiya tuzingki unga berilgan argumentdagi harflarni hayvonlar arrayida hayvonlarni harflari bilan solishtirsin va mos kelganlaridan yangi bir array hosil qisin
*/
/*⭐️ Masalaning yechimi
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
*/

//====================================================================================

/*A-TASK (NodeJS)
⭐️Savol:Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
 */
/* ⭐️ Masalaning yechimi
function countLetters(char, str) {
  const splitted = str.split(""); //array
  const filtered = splitted.filter(ele => ele === char);
  return filtered.length;
}
console.log(countLetters("e", "engineering"));
*/

