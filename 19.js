const timeToMilli = (seconds,minutes=0,hours=0,days=0)=>{
    return 1000*(seconds+60*(minutes+60*(hours+24*days)));
}