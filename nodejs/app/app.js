const express = require('express');
//const fs = require('fs')
//const os = require('os')
//const notes = require('./notes.js');

//var user = os.userInfo();
//console.log(notes.age);

//fs.appendFileSync('greetings.txt', 'Hello ' + user.username + ' world!');
//fs.appendFileSync('greetings.txt', `Hello ${user.username}`);

const customerRoute = require('./routes/customer');
const productRoute = require('./routes/product');
const app = express();

app.use(express.json({
	limit: '50mb'
}));

app.listen(3000, () => {
	console.log('Server started. port 3000');
})

app.use('/customer', customerRoute);
app.use('/product', productRoute);




