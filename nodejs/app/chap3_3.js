var express = require('express');
var app = express();
    // set up handlebars view engine
var handlebars = require('express3-handlebars').create({ defaultLayout:'main' });

var fortunes = [
	"Conquer your fears or they will conquer you.", 
	"Rivers need springs.",
	"Do not fear what you don't know.",
	"You will have a pleasant surprise.", 
	"Whenever possible, keep it simple."
];

app.set('port', process.env.PORT || 3000);

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');

app.get('/', function(req, res) { 
		res.render('home');
});
app.get('/about', function(req, res) {
		var randomFortune = fortunes[Math.floor(Math.random() * fortunes.length)];
        res.render('about', { 
			fortune: randomFortune,
			isLogged: true,
			users: ["parkoon", "kimyang", "choikoon", "leeyang"],
			kv: {a:30, b:2, c:4 }
		});
});
    // 404 catch-all handler (middleware)
app.use(function(req, res, next){ 
		res.status(404);
        res.render('404');
});
    // 500 error handler (middleware)
app.use(function(err, req, res, next){ 
		console.error(err.stack);
        res.status(500);
        res.render('500');
});
app.listen(app.get('port'), function(){
        console.log( 'Express started on http://localhost:' +
        app.get('port') + '; press Ctrl-C to terminate.' );
});