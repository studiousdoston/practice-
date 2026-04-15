// TASK A NODE.JS

function getCharNum(char, str){
  const splitted = str.split("");
  const filtered = splitted.filter(ele=>ele===char);
  return filtered.length
}

//testing 
console.log(getCharNum("i"," I will become the wizard king, my magic is never giving up"));
//passed 