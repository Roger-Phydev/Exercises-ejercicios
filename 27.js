const areOrthogonal = (vec1,vec2)=>{
    if(!Array.isArray(vec1)||!Array.isArray(vec2)||vec1.length!=vec2.length){
        return "Error, debes introducir dos array del mismo tamaño";
    }
    let pdt=0;
    for(let i=0;i<vec1.length;i++){
        try{
            vec1[i]=parseFloat(vec1[i]);
            vec2[i]=parseFloat(vec2[i]);
        }catch{
            return "Error, los vectores deben contener números";
        }
        pdt+=vec1[i]*vec2[i];
    }
    if(pdt==0) return true;
    return false;
}