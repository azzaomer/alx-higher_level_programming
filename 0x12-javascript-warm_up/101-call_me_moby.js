#!/usr/bin/node
//  function that executes x times a function.
exports.callMeby = function (x, theFunction) {
    while (x > 0){
        theFunction();
        x--;

    }
};