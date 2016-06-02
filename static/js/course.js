console.log('loaded')
//OAUTH STUFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

window.onLoadCallback = function(){
    gapi.load('auth2', function() {
        gapi.auth2.init({
	    client_id: 'PLACEHOLDER'});
    });
};

function onSignIn(googleUser) {
    console.log('signin');
    var id_token = googleUser.getAuthResponse().id_token;
    $.ajax({
	url:'/login',
	data: {'id': id_token},
	type: 'POST',
	success: function(response) {
	    //console.log(response);
	    //console.log('location: '+window.location);
	    if (window.location=='http://localhost:5000/login') {
		console.log('gotta go home');
		window.location='/home';
	    }
	    //console.log('signin success, going home');
	    
	    //window.location='/home';
	    //console.log(response);
	},
	error: function(response) {
	    //window.location='/login';
	    //console.log(response);
	    console.log('Wrong credz');
	    signOut();
	    window.location='/login';
	}
    });
    
};

function signOut() {
    //console.log('start');
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
	//console.log('User signed out.');
	var url='/logout';
	$.get(url, function(e) {
	    //console.log('signout fxn');
	    window.location='/home';
	});
    });
};

var signout_button=document.getElementById('signout');
console.log(signout_button);

//signout_button.addEventListener('click', signOut());
signout_button.addEventListener('click', function(e) {
    console.log('start');
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
	console.log('User signed out.');
	var url='/logout';
	$.get(url, function(e) {
	    console.log('signout eventlistener');
	    window.location='/login';
	});
    });
});


//D3 STUFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
var margin = {top: 20, right: 120, bottom: 20, left: 120},
    width = window.outerWidth - margin.right - margin.left - 20,
    //960 - margin.right - margin.left,
    height =  window.outerHeight - margin.top - margin.bottom - 150;
//800 - margin.top - margin.bottom;


var i = 0,
    duration = 750,
    root;

var tree = d3.layout.tree()
    .size([height, width]);

var diagonal = d3.svg.diagonal()
    .projection(function(d) { return [d.y, d.x]; });

var svg = d3.select("#tree").append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


var zoom = function zoom() {
    var scale = d3.event.scale,
	translation = d3.event.translate,
	tbound = -height * scale,
	bbound = height * scale,
	lbound = (-width + margin.right) * scale, 
	rbound = (width - margin.left) * scale;
    // limit translation to thresholds
    translation = [
	Math.max(Math.min(translation[0], rbound), lbound),
	Math.max(Math.min(translation[1], bbound), tbound)
    ];
    svg.attr("transform", "translate(" + translation + ")" + " scale(" + scale + ")");
}

//add zoom behavior to svg
d3.select("svg")
    .call(d3.behavior.zoom()
          .scaleExtent([.75,5])
          .on("zoom",zoom));

d3.select(self.frameElement).style("height", "800px");

var getData = function getData() {
    console.log('getData');
    $.get('/courses', function(e) {
	console.log('getting info');
	console.log()
	var info=JSON.parse(e);
	console.log(info);
	
	root = info[0];
	console.log("root: " + root);
	root.x0 = height / 2;
	root.y0 = 0;

	function collapse(d) {
	    if (d.children) {
		d._children = d.children;
		d._children.forEach(collapse);
		d.children = null;
	    }
	}
	root.children.forEach(collapse);
	update(root);
    });
};

if (window.location=='http://localhost:5000/home') {
    getData();
}

var update = function update(source) {
    //	console.log("updating: " + JSON.stringify(source));
    // Compute the new tree layout.
    var nodes = tree.nodes(root).reverse(),
	links = tree.links(nodes);

    // Normalize for fixed-depth.
    nodes.forEach(function(d) { d.y = d.depth * 180; });

    // Update the nodes
    var node = svg.selectAll("g.node")
	.data(nodes, function(d) { return d.id || (d.id = ++i); });

    // Enter any new nodes at the parent's previous position.
    var nodeEnter = node.enter().append("g")
	.attr("class", "node")
	.attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
	.on("click", click);

    nodeEnter.append("circle")
	.attr("r", 1e-6)
	.style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

    nodeEnter.append("text")
	.attr("x", function(d) { return d.children || d._children ? -10 : 10; })
	.attr("dy", ".35em")
	.attr("text-anchor", function(d) { return d.children || d._children ? "end" : "start"; })
	.text(function(d) { return d.name; })
	.style("fill-opacity", 1e-6);

    // Transition nodes to their new position.
    var nodeUpdate = node.transition()
	.duration(duration)
	.attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

    nodeUpdate.select("circle")
	.attr("r", 4.5)
	.style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

    nodeUpdate.select("text")
	.style("fill-opacity", 1);

    // Transition exiting nodes to the parent's new position.
    var nodeExit = node.exit().transition()
	.duration(duration)
	.attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
	.remove();

    nodeExit.select("circle")
	.attr("r", 1e-6);

    nodeExit.select("text")
	.style("fill-opacity", 1e-6);

    // Update the links
    var link = svg.selectAll("path.link")
	.data(links, function(d) { return d.target.id; });

    // Enter any new links at the parent's previous position.
    link.enter().insert("path", "g")
	.attr("class", "link")
	.attr("d", function(d) {
	    var o = {x: source.x0, y: source.y0};
	    return diagonal({source: o, target: o});
	});

    // Transition links to their new position.
    link.transition()
	.duration(duration)
	.attr("d", diagonal);

    // Transition exiting nodes to the parent's new position.
    link.exit().transition()
	.duration(duration)
	.attr("d", function(d) {
	    var o = {x: source.x, y: source.y};
	    return diagonal({source: o, target: o});
	})
	.remove();

    // Stash the old positions for transition.
    nodes.forEach(function(d) {
	d.x0 = d.x;
	d.y0 = d.y;
    });
}

// Toggle children on click.
function click(d) {
    if (d.children) {
	d._children = d.children;
	d.children = null;
    } else {
	d.children = d._children;
	d._children = null;
    }
    update(d);
};
