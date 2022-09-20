const express = require('express');
const app = express();

app.get('/', (req, res) => res.send('Hello, World333'));

app.listen(3000, () => {
	console.log('My REST Api Running on port 3000!');
})

