
let utils = require("./utils");

// Handle Window Exports:
utils.expose_on_window("$", require("jquery"));
let _ = require("lodash");
utils.expose_on_window("_", _);

let tt = require("./terminal_typeout");
utils.expose_on_window("set_terminal_typeout", tt.set_terminal_typeout);

$(()=>{
    console.log("Hello Alex");
});
