//OAUTH STUFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

window.onLoadCallback = function(){
    gapi.load('auth2', function() {
        gapi.auth2.init({
	    client_id: '179236941327-flh4rlgnlgs9sh5u6ijnca3557ajei9o.apps.googleusercontent.com'});
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

//jQuery("signout").click(function(e) {
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

//print jQuery("signout");
