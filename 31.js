console.log(date);
const isLoopYear = year=>{
    try{
        year=parseInt(year);
    } catch{
        return "error, el año debe ser un número"
    }
    let day = new Date(year,1,29);
    if(day.getMonth()==1){
        return true;
    } else{
        return false;
    }
}