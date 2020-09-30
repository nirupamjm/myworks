

< html >
< head >
< script
src = "http://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"
type = "text/javascript" > < / script >
< script
src = "http://www.skulpt.org/static/skulpt.min.js"
type = "text/javascript" > < / script >
< script
src = "http://www.skulpt.org/static/skulpt-stdlib.js"
type = "text/javascript" > < / script >

< / head >

< body >

< script
type = "text/javascript" >
// output
functions
are
configurable.This
one
just
appends
some
text
// to
a
pre
element.
function
outf(text)
{
    var
mypre = document.getElementById("output");
mypre.innerHTML = mypre.innerHTML + text;
}
function
builtinRead(x)
{
if (Sk.builtinFiles === undefined | | Sk.builtinFiles["files"][x] == = undefined)
throw
"File not found: '" + x + "'";
return Sk.builtinFiles["files"][x];
}

// Here
's everything you need to run a python program in skulpt
// grab
the
code
from your textarea
// get
a
reference
to
your
pre
element
for output
    // configure the output function
// call Sk.importMainWithBody()
function runit() {
var
prog = document.getElementById("yourcode").value;
var
mypre = document.getElementById("output");
mypre.innerHTML = '';
Sk.pre = "output";
Sk.configure({output: outf, read: builtinRead});
(Sk.TurtleGraphics | | (Sk.TurtleGraphics = {})).target = 'mycanvas';
var
myPromise = Sk.misceval.asyncToPromise(function()
{
return Sk.importMainWithBody("<stdin>", false, prog, true);
});
myPromise.then(function(mod)
{
console.log('success');
},
function(err)
{
console.log(err.toString());
});
}
< / script >

    < h3 > Economia < / h3 >
                        < form >
                        < textarea
id = "yourcode"
cols = "40"
rows = "10" >
import turtle

import turtle

print
"Break Even Point"
t = turtle.Turtle()
t.speed(10)
f = t.forward
r = t.rt
u = t.pu
d = t.pd
c = t.color
g = t.goto

# --------- assi
f(-150)
r(-90)
f(150)
u()
# ------------ torna all'origine
g(-150, 0)
# ---------- costi variabili
d()
r(60)
t.speed(3)
c("red")
f(150)
t.write("COSTI VARIABILI")
# ----------- RICAVI
t.speed(10)
u()
g(-150, 0)
r(-15)
d()
t.speed(3)
c("blue")
f(150)
t.write("RICAVI")
print("La retta dei ricavi ha una inclinazione maggiore.")
print("Significa che R > cv")

< / textarea > < br / >
    < button
type = "button"
onclick = "runit()" > Vedi < / button >
                               < / form >
                                   < pre
id = "output" > < / pre >
                    <!-- If
you
want
turtle
graphics
include
a
canvas -->
< div
id = "mycanvas" > < / div >

                      < / body >

                          < / html >