let cont = document.querySelector(".container");
const drawFigure = (figure,size)=>{
    let frg = document.createDocumentFragment();
    if (figure=="square"&&size>1){
        for(let i=0;i<size;i++){
            let div = document.createElement("DIV");
            div.innerText="".padEnd(size,"*");
            frg.appendChild(div);
        }
    } else if(figure=="triangle"&&size>1){
        for(let i=0;i<size;i++){
            let div = document.createElement("DIV");
            div.innerText="".padEnd(i+1,"*");
            frg.appendChild(div);
        }
    } else{
        return "error, error en tamaño o en figura: tamaño>1, figuras: square y triangle";
    }
    cont.appendChild(frg);
}