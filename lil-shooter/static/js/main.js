  function delete_field(field){
    // alert(field)
    $('#'+field).remove();;
  } 

  function addButton(i, type, role) {
    var delete_button = '<button class="btn btn-default pull-right" type="button" onclick=delete_field("'+role+'_'+i+'_'+type+'")>Удалить</button></span>'
    
    var field = '<label>unknown item</label>'
    var added_fields = {'ignore_conf':'Игнорируемые поля при сравнении логов','limit':'Количество тестов','stand':'Номер стенда(0 - Smoke; -1 - Cloud)','debug_cookie':'Дебажная кука', 'add_options':'Дополнительные опции отстрела'}
    if (type in added_fields){
      field ='<div class="input-group col-lg-12 '+role+'_'+i+'_'+type+'" id="'+role+'_'+i+'_'+type+'"><span class="input-group-addon input-group">'+added_fields[type]
    }
    
    if (type == 'ignore_conf'){
      field = field + '<input type="text"  class="pull-left nav nav-justified" id="'+role+'_'+type+'_'+i+' " value="'+$.trim($("#"+role+"_"+type+"_"+0).val())+'" data-bind="value:'+role+'_'+type+'" class="form-control input-sm"/>'
    }
    else if (type == 'limit'){
      field = field + '<input type="number" id="'+role+'_'+type+'_'+i+'" min="0" max="1000000" step="1000" value="'+$.trim($("#"+role+"_"+type+"_"+0).val())+'" data-bind="value:'+role+'_'+type+'" class="form-control input-sm"/>'
    }
    else if (type == 'stand'){
      field = field + '<input type="number" id="'+role+'_'+type+'_'+i+'" min="-1" max="4" step="1" value="'+$.trim($("#"+role+"_"+type+"_"+0).val())+'"data-bind="value:'+role+'_'+type+'" class="form-control input-sm"/>'
    }
    else if (type == 'debug_cookie'){
      var is_debug = ''
      if ($("#"+role+"_"+type+"_"+0).length) {
        is_debug = $("#"+role+"_"+type+"_"+0).is(':checked')
        if (is_debug)
          is_debug = 'checked'
      }
      
      field = '<div class="input-group col-lg-1 ' + role +'_'+i+'_'+type+'" id="'+role+'_'+i+'_'+type+'"><span class="input-group-addon"><input type="checkbox" id="'+role+'_'+type+'_'+i+'" '+is_debug+'></span><span class="input-group-addon">'+added_fields[type]
    }
    else if (type == 'add_options'){
        field = field + '<input type="text" id="'+role+'_'+type+'_'+i+'" value="'+$.trim($("#"+role+"_"+type+"_"+0).val())+'" data-bind="value:'+role+'_'+type+'" class="form-control input-sm"/>'
    }  
    field = field + delete_button + "</div>"
    $('.conf_'+role+'_'+i).append(field);
  }

  function drop_fields(role, n){
     var added_fields = {'ignore_conf':'Игнорируемые поля при сравнении логов','limit':'Количество тестов','stand':'Номер стенда(0 - Smoke; -1 - Cloud)','debug_cookie':'Дебажная кука', 'add_options':'Дополнительные опции отстрела'}
    for (type in added_fields){
      if(( ($('.addButton_'+role+'_'+n+'_'+type).length) == 0) && (($('.input-group .'+role+'_'+n+'_'+type).length) == 0)) {
        showitem='<li role="presentation"><a role="menuitem" tabindex="-1" id="addButton_'+role+'_'+n+'_'+type+'" class="addButton_'+role+'_'+n+'_'+type+'" onclick=addButton("'+n+'","'+type+'","'+role+'")>'+added_fields[type]+'</a></li>'
        $('.item_'+role+'_'+n).append(showitem);
      }
      else if (($('.input-group .'+role+'_'+n+'_'+type).length) > 0){
          $('#addButton_'+role+'_'+n+'_'+type).remove();
      }
    }
  } 