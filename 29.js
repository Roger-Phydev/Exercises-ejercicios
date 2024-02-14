const orderArray = (array,way)=>{
    array.forEach(element => {
        try{
            element=parseFloat(element);
        }catch{
            return "error de formato, el array debe ser de números";
        }
    });
    if(way=="asc"){
        let ans=[array[0]];
        for (let index = 1; index < array.length; index++) {
            let stop=-1
            for(i in ans){
                if((array[index]>=ans[i])){
                    stop=parseInt(i)+1;
                } else if(i==array.length-1){
                    stop==0;
                }
            }
            console.log(ans);
            ans.splice(stop,0,array[index]);
        }
        return ans;
    }else if(way=="desc"){
        let ans=[array[0]];
        for (let index = 1; index < array.length; index++) {
            let stop=-1
            for(i in ans){
                if((array[index]>=ans[i])&&stop==-1){
                    stop=i;
                } else if(i==array.length-1){
                    stop==array.length;
                }
            }
            console.log(stop,array[index]);
            ans.splice(stop,0,array[index]);
        }
        return ans;
    }else{
        return "array válido, pero modo incorrecto. Solo se permite: asc-para ascendente | desc-para descendente";
    }
}