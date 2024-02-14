let d1 = new Date("1996",5,10);
const dayBetween = (dateI,dateF)=>{
    try{
        dateI=dateI.split("/");
        dateF=dateF.split("/");
        let di = new Date(dateI[2],dateI[1]-1,dateI[0]);
        let df = new Date(dateF[2],dateF[1]-1,dateF[0]);
        let diff =Math.abs(df.getTime() - di.getTime());
        return Math.floor(diff/(1000*60*60*24));
    } catch{
        return "error, quizá no usaste el formato dd/mm/aaaa";
    }
}