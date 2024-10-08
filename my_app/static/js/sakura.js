var stop, staticx, img = new Image;

function Sakura(x, y, s, r, fn) {
    this.x = x, this.y = y, this.s = s, this.r = r, this.fn = fn
}

function getRandom(option) {
    var ret, random;
    switch (option) {
        case "x":
            ret = Math.random() * window.innerWidth;
            break;
        case "y":
            ret = Math.random() * window.innerHeight;
            break;
        case "s":
            ret = Math.random();
            break;
        case "r":
            ret = 6 * Math.random();
            break;
        case "fnx":
            random = 1 * Math.random() - .5, ret = function(x, y) {
                return x + .5 * random - 1.7
            };
            break;
        case "fny":
            random = 1.5 + .7 * Math.random(), ret = function(x, y) {
                return y + random
            };
            break;
        case "fnr":
            random = .03 * Math.random(), ret = function(r) {
                return r + random
            }
    }
    return ret
}

function startSakura() {
    requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.msRequestAnimationFrame || window.oRequestAnimationFrame;
    var canvas = document.createElement("canvas"),
        cxt;
    staticx = !0, canvas.height = window.innerHeight, canvas.width = window.innerWidth, canvas.setAttribute("style", "position: fixed;left: 0;top: 0;pointer-events: none;"), canvas.setAttribute("id", "canvas_sakura"), document.getElementsByTagName("body")[0].appendChild(canvas), cxt = canvas.getContext("2d");
    for (var sakuraList = new SakuraList, i = 0; i < 15; i++) {
        var sakura, randomX, randomY, randomS, randomR, randomFnx, randomFny;
        randomX = getRandom("x"), randomY = getRandom("y"), randomR = getRandom("r"), randomS = getRandom("s"), randomFnx = getRandom("fnx"), randomFny = getRandom("fny"), randomFnR = getRandom("fnr"), (sakura = new Sakura(randomX, randomY, randomS, randomR, {
            x: randomFnx,
            y: randomFny,
            r: randomFnR
        })).draw(cxt), sakuraList.push(sakura)
    }
    stop = requestAnimationFrame((function() {
        cxt.clearRect(0, 0, canvas.width, canvas.height), sakuraList.update(), sakuraList.draw(cxt), stop = requestAnimationFrame(arguments.callee)
    }))
}

function stopp() {
    if (staticx) {
        var child = document.getElementById("canvas_sakura");
        child.parentNode.removeChild(child), window.cancelAnimationFrame(stop), staticx = !1
    } else startSakura()
}
img.src = "../static/ico/sakura.png", Sakura.prototype.draw = function(cxt) {
    cxt.save();
    var xc = 40 * this.s / 4;
    cxt.translate(this.x, this.y), cxt.rotate(this.r), cxt.drawImage(img, 0, 0, 40 * this.s, 40 * this.s), cxt.restore()
}, Sakura.prototype.update = function() {
    this.x = this.fn.x(this.x, this.y), this.y = this.fn.y(this.y, this.y), this.r = this.fn.r(this.r), (this.x > window.innerWidth || this.x < 0 || this.y > window.innerHeight || this.y < 0) && (this.r = getRandom("fnr"), Math.random() > .4 ? (this.x = getRandom("x"), this.y = 0, this.s = getRandom("s"), this.r = getRandom("r")) : (this.x = window.innerWidth, this.y = getRandom("y"), this.s = getRandom("s"), this.r = getRandom("r")))
}, SakuraList = function() {
    this.list = []
}, SakuraList.prototype.push = function(sakura) {
    this.list.push(sakura)
}, SakuraList.prototype.update = function() {
    for (var i = 0, len = this.list.length; i < len; i++) this.list[i].update()
}, SakuraList.prototype.draw = function(cxt) {
    for (var i = 0, len = this.list.length; i < len; i++) this.list[i].draw(cxt)
}, SakuraList.prototype.get = function(i) {
    return this.list[i]
}, SakuraList.prototype.size = function() {
    return this.list.length
}, window.onresize = function() {
    var canvasSnow = document.getElementById("canvas_snow")
}, img.onload = function() {
    startSakura()
};