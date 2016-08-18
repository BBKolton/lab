var system = require('system');
var args = system.args;

console.log(args);

var page = require('webpage').create();
page.viewportSize = {width: 1200, height: 700};
page.open('http://' + args[1], function(status) {
  console.log("Status: " + status);
  if(status === "success") {
    page.render('/home/ubuntu/lab/front/static/' + args[1] + '.png');
    console.log('/home/ubuntu/lab/node/' + args[1]);
  }
  phantom.exit();
});
