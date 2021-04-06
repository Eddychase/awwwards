
$(document).ready(function(){
  $('form').submit(function(event){
    event.preventDefault()
    form = $("form")

    $.ajax({
      'url':'/ajax/newsletter/',
      'type':'POST',
      'data':form.serialize(),
      'dataType':'json',
      'success': function(data){
        alert(data['success'])
      },
    })// END of Ajax method
    $('#id_eddy').val('')
    $("#id_eddykanyzek@gmail.com").val('')
  }) // End of submit event

}) // End of document ready function