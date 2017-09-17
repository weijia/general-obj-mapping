$(document).ready( function () {
//    $("td.target").on("click", function(a, b, c, d){
//        console.log(a, b, c, d);
//        var text = $(a.currentTarget).text();
//
//    });

    function decodeEntities(input) {
      var y = document.createElement('textarea');
      y.innerHTML = input;
      return y.value;
    }
    $.each($("td.target"), function(key, value){
        var t = $(value).text();
        $(value).text("");
        var inputElem = $('<input value="'+t+'" rows="1" size="50"></input>');
        var i = $(value).append(inputElem);
        inputElem.autocomplete({
          source: '/ajax_select/ajax_lookup/jira_business',
          response: function( event, ui ) {
//            console.log(event);

            $.each(ui.content, function(key, value){
                value.label = decodeEntities(value.label);
                value.value = decodeEntities(value.value);
            })
          }
        });

    });
});