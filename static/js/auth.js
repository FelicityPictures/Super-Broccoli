//OAUTH STUFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

window.onload = function(){
    console.log('callback');
    /*gapi.load('auth2', function() {
	console.log('auth2');
        gapi.auth2.init({
	    client_id: 'PLACEHOLDER'});
	console.log('afer');
	});*/
    var hi=gapi.auth2.getAuthInstance();
    var options=new gapi.auth2.SigninOptionsBuilder();
    options.setPrompt('select_account');
    console.log(options);
    console.log(hi);
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
	    console.log('location: '+window.location);
	    //if (window.location=='http://www.coursebroccoli.stuycs.org/login' || window.location=='http://www.coursebroccoli.stuycs.org/login/error') {
	    if (window.location=='http://localhost:5000/login' || window.location=='http://localhost:5000/login/error') {
		console.log('gotta go home');
		window.location='/home';
	    }
	    //console.log('signin success, going home');

	    //window.location='/home';
	    //console.log(response);
	},
	error: function(XMLHttpRequest, textStatus, errorThrown) {
	    //window.location='/login';
	    //console.log(response);
	    //console.log(XMLHttpRequest);
	    //console.log(textStatus);
	    console.log(errorThrown);
	    if (errorThrown=='UNAUTHORIZED' || errorThrown=='Unauthorized') {
		console.log('Wrong credz');
		console.log('errorThrown is unauthorized');
		signOut();
		window.location='/login/error';
		console.log(window.location);
	    };
	}
    });

};

function signOut() {
    //console.log('start');
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut();/*.then(function () {
	//console.log('User signed out.');
	var url='/logout';
	$.get(url, function(e) {
	    //console.log('signout fxn');
	    window.location='/home';
	});
    });
    };*/
}

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
