var dep_JSON=$("#dep_data").data();

//var dep_data=JSON.parse(deps);
console.log('ay');

/*$.getJSON('/add', function(data) {
    console.log('hi');
    console.log(data);
    });*/

var deps=dep_JSON.name;
var key=$('#remaster option:selected').text()

var select1=document.getElementById("remaster");
select1.addEventListener('click', function(e) {
    console.log('s1');
    key=$("#remaster option:selected").text();
    var entry=deps[key];
    $("#reslave").empty();
    for (i=0; i<entry.length; i++) {
	$("#reslave").append('<option value="'+entry[i]+'">'+entry[i]+'</option>');
    }
});
			 




