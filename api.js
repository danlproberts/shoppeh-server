//Server Route Mapping
// Dependencies
const express = require('express');
const app = express();
const router = express.Router();
const port = 8080;

const url = require('url');

var PythonShell = require('python-shell');

//Setting up main python script
var retailscraper = 'py/retail_hub.py'
var pyshell = new PythonShell(retailscraper);


//Top-level Path
app.get('/', (request, response) => response.send('Welcome to the Shoppeh API'));

//Router Setup
app.use('/search_api', router);

//Prefixing Path
router.get('/', (request, response) => {

  var urlParts = url.parse(request.url, true);
  var parameters = urlParts.query;
  var searchquery = parameters.query;

/*
PythonShell.run(retailscraper, options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
});
});
*/

pyshell.send(searchquery);

  pyshell.on('retail_hub.py', function (message) {

    console.log(message);

  });

  pyshell.end(function (err) {
    if (err){
        throw err;
    };

    console.log(searchquery);

});
});

//Start port listen
app.listen(port, () => console.log('Listening on port 8080'));

// CORS
// this array is used for identification of allowed origins in CORS
const originWhitelist = ['http://localhost:8080'];

// middleware route that all requests pass through
router.use((request, response, next) => {
  console.log('Server info: Request received');

  let origin = request.headers.origin;

  // only allow requests from origins that we trust
  if (originWhitelist.indexOf(origin) > -1) {
    response.setHeader('Access-Control-Allow-Origin', origin);
  }

  // only allow get requests, separate methods by comma e.g. 'GET, POST'
  response.setHeader('Access-Control-Allow-Methods', 'GET');
  response.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
  response.setHeader('Access-Control-Allow-Credentials', true);

  // push through to the proper route
  next();
});
