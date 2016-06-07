console.log("course info");

var selected = null, //selected element
mouseX = 0, mouseY = 0,
x = 0, y = 0; //top and left values of element

var currNode = null;
var currRoot = "XXXDEPT";
var schedNodes = [];  //codes of courses in schedule
var roots = []; //history of roots

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


var isValidCode = function isValidCode(code){
    //code exists and code does not identify a department
    return /^XXX/g.test(code) == false && code != null
};


var showInfo = function showInfo(d){
    if (isValidCode(d.code)){
	
				currNode = d;
				console.log(d);
				var panel = document.getElementById("info");
				var head = panel.children[0];
				var body = panel.children[1].children;
				head.innerHTML = d.code + " " + d.name;

				//prereqs
				body[1].innerHTML = d.parent != null && isValidCode(d.parent.code) ?
						d.parent.name
						: "None";

				//dependencies
				if (d.children)
						body[4].innerHTML = d.children.map(function(e){
								return e.name;}).join(", ");
	
				else if (d._children)
						body[4].innerHTML = d._children.map(function(e){
								return e.name;}).join(", ");

				else
						body[4].innerHTML = "None";

				body[7].innerHTML = d.misc;
				//course description
				body[9].innerHTML =	d.description;

    }
};


var addToPlanner = function addToPlanner(e){
    e.preventDefault();
    //course is selected and does not already exist in schedule
    if (currNode != null && schedNodes.indexOf(currNode.code) == -1){
				schedNodes.push(currNode.code)
		
				d3.select("#list").append("li")
						.classed("list-group-item", true)
						.text(currNode.code + " " + currNode.name);
		}
};

var changeRoot = function changeRoot(e){
		e.preventDefault();
		console.log(currNode);
		if (currRoot != currNode.code){
				roots.push(currRoot);
				currRoot = currNode.code;
				getData(currRoot);
		}
};

var treeBack = function treeBack(e){
		if (roots.length == 1 && currRoot != roots[0])
				currRoot = roots[0];
		else if (roots.length > 1)
				currRoot = roots.pop();
		
		getData(currRoot);
};


$(document).ready(function(e){
		$("#add").click(addToPlanner);
		$("#root").click(changeRoot);
		//roots.push('XXXDEPT')
});

