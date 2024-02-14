const buttons = document.querySelectorAll(".btn");
const stands = document.querySelectorAll(".cont");
const inputValues = document.querySelectorAll(".val");
const values = document.querySelectorAll(".q");
const screen = document.getElementById("screen");
const buy = document.getElementById("introduce");
const change = document.querySelector(".change");
const reset = document.getElementById("reset");
const products = [
    ["Fanda 355ml",14],
    ["Cola-cola 355ml",18],
    ["Sprite 355ml",14],
    ["Cola-cola zero 355ml",16],
    ["Cola-cola 600ml",25],
    ["Mundol 600ml",21],
    ["Sprite 600ml",20],
    ["Cola-cola zero 600ml",21],
    ["Fanda 600ml",20]
];
let cost=0;
let product=[];
let getMoney=false;
let next=true;
const writeScreen = str=>{
    screen.innerHTML=str;
}
for(let i=0;i<7;i++){
    inputValues[i].addEventListener("change",v=>{
        values[i].innerHTML=`cantidad: ${v.target.value}`;
    });
}
for(let i=0;i<9;i++){
    buttons[i].addEventListener("click",()=>{
        if(next){
            writeScreen(`selección: ${products[i][0]} costo: $${products[i][1]} Introduce el dinero`);
            for(let j=0;j<9;j++){
                if(j!=i){
                    stands[j].style=`background: #AAA`;
                    buttons[j].style=`background: #FFF`;
                }
            };
            stands[i].style=`background: #C3C600`;
            buttons[i].style=`background: #2C4`;
            screen.scrollIntoView({
                behavior:"smooth"
            });
            product=[i,products[i][0]];
            cost=products[i][1];
            getMoney=true;
        } else{
            screen.scrollIntoView();
            writeScreen("Debes dar click al botón continuar");
        }
    })
}
buy.addEventListener("click",()=>{
    if(getMoney){
        let money=[];
        inputValues.forEach(item=>{
            money.push(parseInt(item.value));
        })
        let status= operate(money,cost);
        console.log(status);
        if(status[0]){
            change.innerHTML=`<h4>Su producto: ${product[1]}</h4>`;
            if(product[0]>3){
                change.innerHTML+=`<img src="images/botella.png">`;
            }else{
                change.innerHTML+=`<img src="images/lata.jpg">`;
            }
            change.innerHTML+=`<h4>Su cambio:</h4>`
            let frg=document.createDocumentFragment();
            for(let j=0;j<7;j++){
                addItems(j,status[1][j],frg);
            }
            change.appendChild(frg);
        } else{
            change.innerHTML=`<h4>Dinero insuficiente</h4>`;
            change.innerHTML+=`<h4>Devolviendo dinero:</h4>`;
            let frg=document.createDocumentFragment();
            for(let j=0;j<7;j++){
                addItems(j,status[1][j],frg);
            }
            change.appendChild(frg);
            }
        }
        getMoney=false;
        next = false;
        writeScreen("Procesando...");
        change.scrollIntoView({
            behavior:"smooth"
        })
        reset.style="display:block";
        for(let j=0;j<9;j++){
            stands[j].style=`background: #AAA`;
            buttons[j].style=`background: #FFF`;
        }
    }
);
reset.addEventListener("click",()=>{
    next=true;
    screen.scrollIntoView({
        behavior:"smooth"
    })
    writeScreen("Bienvenido!!! Selecciona una opción");
    change.innerHTML="";
    reset.style="display: none";
    for(let j=0;j<7;j++){
        inputValues[j].value=0;
        values[j].innerHTML=`Cantidad: 0`;
    }
})
const operate = (received,cost)=>{
    let quantities = [100,50,20,10,5,2,1];
    let total=0;
    for(let i=0;i<7;i++){
        total+=quantities[i]*received[i];
    }
    if(total<cost){
        return [false,received];
    }else{
        total = total-cost;
        let change=[];
        for(let i=0;i<7;i++){
            change[i]=Math.floor(total/quantities[i]);
            total=total%quantities[i];
        }
        return [true,change];
    }
}
const addItems = (index,times,fragment)=>{
    let imgs=[
        "images/cien.jpeg",
        "images/cincuenta.jpg",
        "images/veinte.jpg",
        "images/diez.jpg",
        "images/cinco.jpg",
        "images/dos.jpg",
        "images/uno.jpg"
    ];
    if(times>0){
        let div=document.createElement("DIV");
        if(index>2){
            div.classList.add("coin");
        } else{
            div.classList.add("bill");
        }
        for(let i=0;i<times;i++){
            let img=document.createElement("IMG");
            img.src=imgs[index];
            div.appendChild(img);
        }
        fragment.appendChild(div);
    }       
}