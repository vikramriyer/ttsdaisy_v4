var editor = ace.edit("editor");
document.getElementById('editor').style.fontSize = '14px';
editor.setTheme("ace/theme/monokai");
editor.getSession().setMode("ace/mode/xml");
editor.getSession().setUseWrapMode(true);
var data = "the new text here. "; // This should be fetched from db and copied
editor.setValue(data);

function run_pipeline(bookname, xmldata) {
  url = "http://10.2.16.111:5000/run_daisy_pipeline/";
  data = {'bookname': bookname, 'xmldata': xmldata};
  $.ajax({
      type:"POST",
      url: url,
      data: data,
      success: function (response){
        response = JSON.parse(response);
      },
      error: function(errorThrown){
        swal("OOPS!","Looks like there was an error: " + errorThrown, "error");
      },
      dataType: "text"
    });
}

function get_bookname(){
  var bookname = document.getElementById("hiddenBookName").value
  return bookname
}

function get_data(){
  var xml_file_editor = ace.edit('editor');
  xml_data = xml_file_editor.getSession().getValue();
  return xml_data
}
