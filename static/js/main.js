

function redirect_to_search(){
    var company1 = $("#company1").val();
    var company2 = $("#company2").val();

    window.location.href = "/search?company1=" + company1 + "&company2=" + company2; 
}