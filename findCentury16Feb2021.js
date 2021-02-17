function yearCentury(year){
    if (year % 100 == 0){
        return year/100;
    }
    else{
        return Math.floor(year/100) + 1;
    }
}

console.log(yearCentury(1820));