const arrayFormat = (array,mode)=>{
    let n=0;
    if(mode=="runner"){
        array.filter(item=>{
            if(item=="jump"||item=="run") n++;
        });
        if(n==array.length) return true;
        return false;
    }
    else if (mode=="road"){
        array.filter(item=>{
            if(item=="_"||item=="|") n++;
        })
        if (n==array.length) return true;
        return false;
    }
    return false;
}
const race = (runnerArray,roadArray)=>{
    if(arrayFormat(runnerArray,"runner")&&arrayFormat(roadArray,"road")){
        for (i in roadArray){
            if(runnerArray[i]!=undefined){
                if(runnerArray[i]=="jump"&&roadArray[i]=="_") {roadArray[i]="x";}
                else if (runnerArray[i]=="run"&&roadArray[i]=="|") {roadArray[i]="/";}
            }
        }
        if(roadArray.length>runnerArray.length){
            console.log(roadArray,"no recorrió todo");
            return false;
        } else{
            if(roadArray.includes("x")||roadArray.includes("/")){
                console.log(roadArray);
                return false;
            }
            console.log(roadArray);
            return true;

        }
    }else{
        return "error en formato, el array de corredor solo debe contener 'jump' o 'run', y el de carrera solo '|' o '_'";
    }
}