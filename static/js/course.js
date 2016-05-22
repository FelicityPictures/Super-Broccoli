console.log('loaded')

var getData = function getData() {
    console.log('getData');
    $.get('/courses', function(e) {
				console.log('getting info');
				var info=JSON.parse(e);
				console.log(info);
    });
};

getData();
