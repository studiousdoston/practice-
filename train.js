/*A-TASK (NodeJS)

⭐️Savol:Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi. */


//⭐️SOLUTION
function countLetters(char, str) {
  const splitted = str.split(""); //array
  const filtered = splitted.filter(ele => ele === char);
  return filtered.length;
}

//⭐️RESULT 
console.log(countLetters("e", "engineering"));



//*B-TASK (NodeJS)

//⭐️SAVOL: Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
// MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.

//⭐️SOLUTION
function countNums(str) {
  return str.split("").map(Number).filter(Boolean).length;
}

//⭐️RESULT
console.log(countNums("ad2a54y79wet0sfgb9"));



// CHALLANGE TASK: Animals 
//⭐️ SAVOL shunday bir funksiya tuzingki unga berilgan argumentdagi harflarni hayvonlar arrayida hayvonlarni harflari bilan solishtirsin va mos kelganlaridan yangi bir array hosil qisin

//⭐️SOLUTION:
const animals = ["fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog", "hen", "mole", "duck", "goat", "dog", "cat", "bat", "cow"];
// STEP 1: seperate the individual array elements into arrays consists of words inside the element --> [ 'w', 'o', 'l', 'f' ],
const animal = animals.map(ele => ele.split("")); //✅

// STEP 2: seperate the argument's individual letters into one array: "fdgwoalt" --> [ 'f', 'd', 'g', 'w', 'o', 'a','l', 't' ]
const letter = "fdgwoalt" //✅       // should give us ["goat", "wolf", "dog"]
const letters = letter.split("");

// STEP 3: compare  the two arrays individual elements, and take the elements which exist in both arrays 
let array = [];
for (let i = 0; i < animal.length; i++) {
  if (animal[i].every(letter => letters.includes(letter))) { array.push(animal[i].join("")) }
}
//console.log(array)

// STEP 4: create the function
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
};   //✅
const foundAnimals = findAnimals("fdgwoalt");

//⭐️ RESULT:
console.log(foundAnimals)
