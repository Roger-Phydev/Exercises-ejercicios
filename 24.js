const frg=document.createDocumentFragment();
// 1ro:
const divOne = document.createElement("DIV");
text="usando for: ";
for(let i=1;i<=100;i++){
    text+=`| ${i} |`
}
divOne.innerText=text;
frg.appendChild(divOne);
// 2do:
const divTwo = document.createElement("DIV");
text="usando while: ";
let index=1;
while(index<=100){
    text+=`| ${index} |`;
    index++;
}
divTwo.innerText = text;
frg.appendChild(divTwo);
// 3ro:
const divThree = document.createElement("DIV");
text="usando arrays: ";
let array = ["l"];
while (array.length<=100){
    text+=`| ${array.length} |`
    array.unshift("l");
}
divThree.innerText=text;
frg.appendChild(divThree);
// 4to:
const divFour = document.createElement("DIV");
text="usando strings: ";
let str="s";
while(str.length<=100){
    text+=`| ${str.length} |`
    str+="s";
}
divFour.innerText=text;
frg.appendChild(divFour);
// 5to:
const divFive = document.createElement("DIV");
text="usando método de string: ";
let arr = "".padEnd(100,"string").split("");
for(i in arr){
    text+=`| ${parseInt(i)+1} |`;
}
divFive.innerText=text;
frg.appendChild(divFive);
// 6to:
const divSix = document.createElement("DIV");
let n=0;
text="Usando forEach: "
arr.forEach(element=>{
    n++;
    text+=`| ${n} |`;
})
divSix.innerText=text;
frg.appendChild(divSix);
// 7mo:
const divSeven = document.createElement("DIV");
text = "usando funciones recursivas: ";
n=1;
const recursiveCount = (n,tx) =>{
    if(n==101){
        return tx
    } else if(n<101){
        tx+=`| ${n} |`;
        n++;
        return recursiveCount(n,tx);
    }
}
divSeven.innerText=recursiveCount(n,text);
frg.appendChild(divSeven);
//###############################################################################
document.querySelector(".container").appendChild(frg);