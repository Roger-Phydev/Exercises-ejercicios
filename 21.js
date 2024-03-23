const uploadInput = document.querySelector(".uf");// file selector
let calc;//the calculator
uploadInput.addEventListener("change",()=>{
    if(uploadInput.files.length==1){
        uploadInput.files[0].text().then(res=>{
            calc = res.replace(/\r\n/g," ").split(" ");
            console.log(calc);
            calculator(calc);
        })
    }
})
const calculator = array =>{
    if(array.length%2==0||array.length==1) return "cantidad de filas insuficientes";
    for(i in array){
        if(i%2==0){
            try{ 
                array[i]=parseFloat(array[i]);
            }catch{
                return "error de formato";
            }
        }
        else if(i%2==1&&!(["+","/","*","-"].includes(array[i]))){
            console.log(`${i}`)
            alert("el archivo debe tener en cada fila un número o una operación, ej: 1 / 5");
            return "error de formato";
        }
    }
    let ans=array[0];
    const container = document.getElementById("container");
    let frg = document.createDocumentFragment();
    for(let i=1;i<array.length;i+=2){
        ans = operate(ans,array[i+1],array[i]);
        let row = document.createElement("DIV");
        row.innerText=`${array[i-1]} ${array[i].replace("*","x")} ${array[i+1]} = ${ans}`;
        frg.appendChild(row);
    }
    let total = document.createElement("DIV");
    total.innerText=`Total: ${ans}`;
    frg.appendChild(total);
    container.appendChild(frg);
}
const operate = (a,b,op)=>{
    if(op=="+"){
        return a+b;
    } else if(op=="-"){
        return a-b;
    } else if(op=="*"){
        return a*b;
    } else if(op=="/"){
        return a/b;
    } else return null;
}