function updateMeters() {
    const circles = document.querySelectorAll('.circle');
    circles.forEach(elem => {
        const dots = elem.getAttribute('data-dots');
        const marked = elem.getAttribute('data-percent');
        const percent = Math.floor(dots * marked / 100);
        const rotate = 360 / dots;
        let points = "";
        for (let i = 0; i < dots; i++) {
            points += `<div class="points" style="--i: ${i}; --rot: ${rotate}deg"></div>`;
        }
        elem.innerHTML = points;
        const pointsMarked = elem.querySelectorAll('.points');
        for (let i = 0; i < percent; i++) {
            pointsMarked[i].classList.add('marked')
        }
    })
}

String.prototype.toHSL = function(opts) {
    var h, s, l;
    opts = opts || {};
    opts.hue = opts.hue || [0, 360];
    opts.sat = opts.sat || [75, 100];
    opts.lit = opts.lit || [40, 60];

    var range = function(hash, min, max) {
        var diff = max - min;
        var x = ((hash % diff) + diff) % diff;
        return x + min;
    }

    var hash = 0;
    if (this.length === 0) return hash;
    for (var i = 0; i < this.length; i++) {
        hash = this.charCodeAt(i) + ((hash << 5) - hash);
        hash = hash & hash;
    }

    h = range(hash, opts.hue[0], opts.hue[1]);
    s = range(hash, opts.sat[0], opts.sat[1]);
    l = range(hash, opts.lit[0], opts.lit[1]);

    return `hsl(${h}, ${s}%, ${l}%)`;
}

/*
var list = document.querySelectorAll("#one li")
forEach(list, function(index, value) {
    list[index].style.color = list[index].textContent.toHSL({
        hue: [180, 360],
        sat: [75, 95],
        lit: [45, 55]
    })
})
var list = document.querySelectorAll("#two li")
forEach(list, function(index, value) {
    list[index].style.color = list[index].textContent.toHSL({
        hue: [180, 360],
        sat: [85, 100],
        lit: [60, 75]
    })
})*/
