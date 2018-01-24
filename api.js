//Server Route Mapping
// Dependencies
const express = require('express');
const app = express();
const router = express.Router();
const port = 8080;

var PythonShell = require('python-shell');

//Setting up main python script
var retailscraper = 'retail_hub.py'
var pyshell = new PythonShell(retailscraper);


//Top-level Path
app.get('/', (request, response) => response.send('Welcome to the Shoppeh API'));

//Start port listen
app.listen(8080, () => console.log('Listening on port 8080'));

//Router Setup
app.use('/search', router);

//Prefixing Path
router.get('/', (request, response) => {

  var urlParts = url.parse(request.url, true);
  var parameters = urlParts.query;
  var searchquery = parameters.search;

  pyshell.on('Activating python scrapers...', function (message)) {

    console.log(message);

  };

  pyshell.end(function (err) {
    if (err){
        throw err;
    };

    console.log('Done');

});

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
