const isAnagram = (firstString,secondString)=>{
    firstString = firstString.toLowerCase();
    secondString = secondString.toLowerCase();
    if (firstString==secondString){
        return false;
    }
    else{
        let reversed = "";
        for (letter in secondString){
            reversed = secondString[letter] + reversed;
        }
        if (reversed==firstString){
            return true;
        }
        else{
            return false
        }
    }
}
let a = "feliz", b = "zileF", c = "nada",d="Feliz";
console.log("Son anagramas???");
console.log(`${a} y ${b} : ${isAnagram(a,b)}`);
console.log(`${a} y ${c} : ${isAnagram(a,c)}`);
console.log(`${a} y ${d} : ${isAnagram(a,d)}`);