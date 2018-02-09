//Server Route Mapping
// Dependencies
const express = require('express');
const app = express();
const router = express.Router();
const port = 8080;

const url = require('url');

var PythonShell = require('python-shell');

//Setting up main python script
var retailscraper = 'retail_hub.py'

//Top-level Path
app.get('/', (request, response) => response.send('Welcome to the Shoppeh API'));

//Router Setup
app.use('/search_api', router);

//Prefixing Path
router.get('/', (request, response) => {

  var ip = request.header('x-forwarded-for') || request.connection.remoteAddress;
  if (ip === "::1") {
     ip = 'localhost';
   }

  console.log('Processing request from %j...', ip)

  var urlParts = url.parse(request.url, true);
  var parameters = urlParts.query;
  var searchquery = parameters.query;

  var options = { mode: 'text',
  pythonPath : 'C:/Users/daniel.roberts/AppData/Local/Continuum/anaconda3/python.exe', //C:/Users/Daniel/Anaconda3/python.exe
  scriptPath: 'py',
  args: [searchquery]}

  console.log('Search Term: %j', searchquery);

  //pyshell.send(searchquery);

  PythonShell.run(retailscraper, options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log(response.statusCode.toString())
  response.writeHead(response.statusCode.toString(), {"Content-Type": "application/json"});
  response.write(results.toString());
  console.log('Results Recieved')
  response.end();
});

  console.log('Request Sent')

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
