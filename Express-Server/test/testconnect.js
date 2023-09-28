var mysql = require('mysql');

var con = mysql.createConnection({
  host: "XXX",
  user: "XXX",
  password: "XXX!",
  database: "cyc"
});

// Each row is an array. i.e. result[0] is first input, result[0].FirstName is "John"
con.connect(function(err) {
  if (err) throw err;
  con.query("SELECT * FROM students LIMIT 5", function (err, result, fields) { // Fields is an array with object info on each field
    if (err) throw err;
    //console.log(result);
  });
});

// Write create HTML file
var fs = require('fs');

// Will rewrites file if it already exists
var fileName = 'testfile.html';
var stream = fs.createWriteStream(fileName);

stream.once('open', function(fd) {
  var html = buildHtml();

  stream.end(html);
});
/*Build HTML file with query data 
function buildHtml(req) {
  var header = "This is the Header1";
  var body = "This is the Body1";

  // Add query data

  return '<!DOCTYPE html>' 
       + '<html><head>' + header + '</head><body>' + body + '</body></html>';
};
*/
/* Read HTML File and sent to local server
var http = require('http'); 
var fs = require('fs');
http.createServer(function (req, res) {
  fs.readFile('demofile1.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    return res.end();
  });
}).listen(8080);
*/