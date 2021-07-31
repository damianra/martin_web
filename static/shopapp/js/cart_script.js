var cart_array = new Array();

$(document).ready(function(){
    var total = 0;
    $(".add_cart").click(function(e){
        var id = $(this).attr("data-id");
        var name_id = "name_" + id;
        var price_id = "price_" + id;
        var cant = 1;
        var name = $("#"+name_id).text();
        var price = $("#"+price_id).text();
        var exist = false;

        cart_array.forEach(function(producto, index) {
            if(producto.producto == name){
                exist = true;
                cart_array[index]["cantidad"] += 1;
                cart_array[index]["precio"] = parseInt(cart_array[index]["cantidad"]) * parseInt(price);
            }
        });

        if(!exist){
            cart_array.push({"producto":name, "cantidad":parseInt(cant), "precio": price});
        }

        $(".count").text(cart_array.length);
    });

    $("#cart_button").click(function(){
        total = 0;
        cart_array.forEach(function(producto, index) {
            var row = '<tr scope="row" class="del" id="product_'+index+'">' + 
            '<td class="del"><button type="button" class="del_cart btn btn-outline-dark mt-auto" data-id="'+ index +'">X</button></td>' +
            '<td class="del">' + producto.producto + '</td>' +
            '<td class="del">' + producto.cantidad + '</td>' +
            '<td class="del">' + producto.precio + '</td>';
            total = total + parseInt(producto.precio);
            $("#cart_table").append(row);
        });
        var row_total = '<tr scope="row" class="del">' + 
        '<td class="del"></td>' +
        '<td class="del"></td>' +
        '<td class="del"></td>' +
        '<td class="del" id="total">Total: $' + total + '</td>';
        $("#cart_table").append(row_total);
    });

    $(".dismiss_buy").click(function(){
        $("tr").remove(".del");
        $("td").remove(".del");
    });

    $("#finish_buy").click(function(){
        var link_data = "";
        cart_array.forEach(function(producto, index) {
            link_data += producto.producto + '%20' +
            '%20' + 'x' + producto.cantidad + '%20' +
            '%20' + producto.precio + '%0A' + ' ---- ';
        });
        
        window.open("https://api.whatsapp.com/send?phone=34123456789&text="+link_data+" ----- TOTAL: " + total);
        location.reload();
    });

    $(document).on('click','.del_cart', function(){
        var id = $(this).attr("data-id");
        total = total - (parseInt(cart_array[id]['precio']) * parseInt(cart_array[id]['cantidad']));
        if(total < 0){
            total = 0;
        }else if(cart_array.length == 0){
            total = 0;
        }
        $("#total").text('Total: $'+total);
        $("tr").remove("#product_"+id);
        cart_array.splice(id,1);
    });

});