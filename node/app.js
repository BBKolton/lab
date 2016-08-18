var path = require('path');
var childProcess = require('child_process');
var phantom = require('phantomjs-prebuilt');
var binPath = phantom.path
var express = require('express');

var app = express();


app.all('/:site', function(req, res) {phantomparse(req, res)});
app.all('/http://:site', function(req, res) {phantomparse(req, res)});
app.all('/https://:site', function(req, res) {phantomparse(req, res)}); 

function phantomparse(req, res) {
	
	console.log('request ' + req.params.site);

	var childArgs = [
		path.join(__dirname, 'phantom.js'),
		req.params.site
	]

	childProcess.execFile(binPath, childArgs, function(err, stdout, stderr) {
		console.log('err: ' + err)
		console.log('stderr: '  + stderr)
		console.log('stdout: '  + stdout)
		console.log('last');
		res.send(200);
	})
}

app.listen(1234, function() {
	console.log('server up!')
})
