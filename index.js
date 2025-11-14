//
// definitions
//

var path = require('path');
const fs = require('fs');
let http = require('http');
var express = require('express');
// add express-handlebars to use handlebars with express view engine
var exphbs = require('express-handlebars');
const { setTimeout } = require('timers');
const { redirect } = require('next/dist/server/api-utils');

var app = express()
var port = process.env.PORT || 3002
const { PythonShell } = require('python-shell');
const pythonOptions = {
    mode: 'text',
    args: []
}

//
// middleware
//

// set express app to use express-handlebars on res.render() call
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

// index
// NOTE: this route uses ASYNC syntax to allow it to wait
app.get('/', async (req, res) => {
    let theNumber = 'undefined';
    try {
        console.log("TRYING")
        await PythonShell.run('random_number_generator.py', pythonOptions, function(err, results) {
            if (err) throw err;
            res.send(results)
            console.log(results)
        })
        .then(messages=>{
            theNumber = messages[messages.length - 1]
            console.log(theNumber)
            lineArray = theNumber.split('\n');
            lastLine = lineArray[lineArray.length - 1]
            console.log(lastLine)
            console.log("Finished")
            res.send({'number': lastLine});
        })
    }
    catch {
        console.error("wtf")
    }
})

//
app.listen(port, function () {
    console.log("== Server is listening on port", port)
})