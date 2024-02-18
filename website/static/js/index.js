let selectElement = document.getElementById('ticker_field');

selectElement.addEventListener('change', function() {

    document.getElementById('tickerform').submit();
});

function buyQuantity(){
    buy_quantity= document.getElementById("buy").value
    buy_count = 0;
    for(let i=0; i < buy_quantity.length; i++){
        if (parseInt(buy_quantity[i].value))
            buy_count += parseInt(buy_quantity[i].value);


}
}

function sellQuantity(){
    sell_total= document.getElementById("sell").value
    console.log(sell_total)

}

