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
    var source_content_type_id = $($("td.source_content_type_id")[0]).text();
    var target_content_type_id = $($("td.target_content_type_id")[0]).text();
    $.each($("td.target"), function(key, value){
        var t = $(value).text();
        var source_object_id = $("td.id", $(value).parent()).text();
        if(t!="") return;
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
          },
          change: function(event,ui){
              $(this).val((ui.item ? ui.item.id : ""));
          },
          select: function(event, ui){
            //console.log(event, ui);
            var data = {
                source_content_type: source_content_type_id,
                source_object_id: source_object_id,
                target_content_type: target_content_type_id,
                target_object_id: ui.item.pk
            };

            $.post("/general_obj_mapping/rest_api/mapping_relation/", data, function(result){
                    //elem.attr("state-id", result.id);
                    console.log(result);
                    if(result.id){
                        $(value).text(inputElem.val());
                    }
                });
          }
        });

    });
});