const toMorse = {//creamos array de conversión
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "ch":"----",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "ñ":"--.--",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    ".":".-.-.-",
    ",":"--..--",
    "?":"..--..",
    " ":"   "
}
let toLetter = {};
for (key in toMorse){
    toLetter[toMorse[key]]=key;
}
const countLetter = (str,lett) =>{
    let n = 0;
    if(!(str.includes(lett))){
        return n;
    } 
    let aux = str.split("");
    for (i of aux){
        if (i==lett) n++;
    }
    return n;
}
const morseNormal = st =>{
    let nstr = [];
    let init = 0;
    let cursor = 0;
    while (cursor<st.length){
        if (st[init]!=" "){
            while (st[cursor]!=" "&&cursor<st.length){
                cursor++;
            }
            nstr.push(st.substring(init,cursor));
            init = cursor+1;
            cursor++;
        } else{
            if (init<st.length-2&&st[init]==" "&&st[init+1]==" "&&st[init+2]==" "){
                nstr.push("   ");
                init+=3;
                cursor+=3;
            } else{
                init++;
                cursor++;
            }
        }
    }
    return nstr;
}
const morseConverter = str =>{
    let conv = "";
    let sp = countLetter(str," ");
    let p = countLetter(str,".");
    let b = countLetter(str,"-");
    str = str.trim();
    if (str.length == sp + p + b){
        str = morseNormal(str)
        code = Object.keys(toLetter);
        for (pattern of str){
            if (code.includes(pattern)){
                conv+=toLetter[pattern];
            } else{
                conv.concat(pattern);
            }
        }
        return conv;
    } else{
        str = str.split("");
        code = Object.keys(toMorse);
        for ( l in str){
            if (code.includes(str[l])){
                conv+=toMorse[str[l]]+" ";
            } else{
                conv+=str[l];
            }
        }
        return conv;
    }
}