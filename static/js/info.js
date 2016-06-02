console.log("course info");

var selected = null, //selected element
		mouseX = 0, mouseY = 0,
		x = 0, y = 0; //top and left values of element

//called at the start of dragging an element
function dragStart(element){
		selected = element;
		x = mouseX - selected.offsetLeft;
		y = mouseY - selected.offsetTop;
}

//while dragging
function moveElement(e){
		mouseX = e.clientX;
		mouseY = e.clientY;
		if (selected){
				//adjust element position by top left corner
				selected.style.left = (mouseX - x) + 'px';
				selected.style.top = (mouseY - y) + 'px';
		}
}

function destroy(){
		selected = null;
}

$("[draggable=true]")
		.mousedown(function(e){
				dragStart(this);
				return false;})
		.mouseup(destroy)
		.mouseleave(destroy)
		.mousemove(moveElement);


var showInfo = function showInfo(d){
		if (/^XXX/g.test(d.code) == false){
				var panel = document.getElementById("info");
				var head = panel.children[0];
				head.innerHTML = d.code + " " + d.name;
				$("#info p").each(function(i){
						$(this).text($(this).text + )
				});
		}
};
