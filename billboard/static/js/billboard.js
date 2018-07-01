$(".btn-plus" ).on( "click", function() {
    $("#add-block").css("display","block");
    $(".btn-plus").css("display","none");
    $(".btn-valid").css("display","inline-block");
  });

 $("#btn-close" ).on( "click", function() {
    $("#add-block").css("display","none");
    $(".btn-plus").css("display","inline-block");
    $(".btn-valid").css("display","none");
  });

  $("#btn-check" ).on( "click", function() {
    if($(".inp-title").val().length === 0 || $(".inp-description").val().length === 0 || $(".inp-author").val().length === 0){
        alert("all the fields are mandatory !")
    }
  });