'use strict';

let express = require('express');
let fs = require('fs');
let jsonfile = require('jsonfile');
let parser = require('body-parser');
let path = require('path');

let app = express();
app.use(parser.json());

let config = {};
let file = path.resolve(__dirname, 'config.json');

//Load or create the configuration file
try {
	fs.accessSync(file, fs.F_OK);
} catch(e) {
	jsonfile.writeFileSync(file, {
		common: {
			red: 128,
			green: 128,
			blue: 128
		}
	});
} finally {
	config = jsonfile.readFileSync(file);
}

app.get('/', (req, res) => {
	res.send(config);	
});

app.post('/', (req, res) => {
	let tempConfig = { common: {} };

	if(req.body && req.body.hasOwnProperty('common') &&
	req.body.common.hasOwnProperty('red') &&
	req.body.common.hasOwnProperty('green') &&
	req.body.common.hasOwnProperty('green') && 
	!isNaN(parseInt(req.body.common.red)) && 
	!isNaN(parseInt(req.body.common.green)) && 
	!isNaN(parseInt(req.body.common.blue))) {
		tempConfig.common.red = Math.abs(parseInt(req.body.common.red)) % 256;
		tempConfig.common.green = Math.abs(parseInt(req.body.common.green)) % 256;
		tempConfig.common.blue = Math.abs(parseInt(req.body.common.blue)) % 256;
	} else {
		res.status(400).send('The request is malformed');
		return;
	}

	config = tempConfig;
	jsonfile.writeFileSync(file, config);
	res.send(config);
});

app.listen(80);
