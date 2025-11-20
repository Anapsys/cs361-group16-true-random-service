//
// definitions
//
var express = require('express');
var exphbs = require('express-handlebars');
const { PythonShell } = require('python-shell');

var app = express();
var port = process.env.PORT || 3002;

const pythonOptions = {
    mode: 'text',
    args: []
};

//
// middleware
//
app.engine('handlebars', exphbs.engine({
    defaultLayout: null
}))
app.set('view engine', 'handlebars')

// static, json, urlencoded
app.use(express.static('static'))
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

//
// route service
//

// Route to get a random number from (random_number_generator.py)
// NOTE: this route uses ASYNC syntax to allow it to wait
app.get('/', async (req, res) => {

    let theNumber = 'undefined';

    try {
        console.log("Acquiring pixel...");

        await PythonShell.run('random_number_generator.py', pythonOptions, function(err) {
            if (err) throw err;
        })
        .then(messages=>{

            // Capture the last line from the script
            theNumber = messages[messages.length - 1];
            console.log(theNumber);

            let lineArray = theNumber.split('\n');
            let lastLine = lineArray[lineArray.length - 1];

            console.log("Finished");
            res.send({'number': lastLine});
        });

    } catch (err) {

        // Handle error
        console.error("Python execution failed:", err);
        res.status(500).json({error: "Failed to acquire pixel from random_number_generator.py"})
    }

});

// Start server on the port
app.listen(port, function () {
    console.log("== Server is listening on port", port)
});