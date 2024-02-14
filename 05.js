const poligonArea = (form,sideA,sideB=0)=>{
    try{
        form = form.toLowerCase();
        sideA = parseFloat(sideA);
        sideB = parseFloat(sideB);
    } catch(e){
        console.log(e);
    }
    if (form=="triangle"){
        return sideA*sideB*0.5;
    }
    else if(form=="square"){
        return sideA**2;
    }
    else if(form=="rectangule"){
        return sideA*sideB
    }
}