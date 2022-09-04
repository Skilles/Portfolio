// getting all required elements
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
const icon = searchWrapper.querySelector(".icon");
const langList = document.getElementById("languages")
const meters = document.querySelector(".meter-wrapper");

let allLanguages = [];
let selectedLangs = [];

// if user press any key and release
inputBox.onkeyup = (e)=>{
    if (allLanguages.length === 0) {
        cacheAllLanguages();
    }
    let userData = e.target.value?.toLocaleLowerCase();
    let suggestionList = [];
    if (userData) {
        suggestionList = allLanguages
            .filter((language) => language.toLocaleLowerCase().startsWith(userData))
            .map((language) => suggestionListItem(language));
        showSearch();
        showSuggestions(suggestionList);
    } else {
        hideSearch();
    }
}

function cacheAllLanguages(endpoint) {
    $.ajax({
        type: 'GET',
        url: endpoint + '?json=true',
        success: function (data) {
            allLanguages = data;
        },
        error: function (data) {
            console.log("Error occured during GET: " + data.toString());
        }
    })
}

function submit(url) {
    if (selectedLangs.length === 0) {
        return;
    }
    $.ajax({
        type: 'POST',
        url: url,
        data:
            {
                languages: selectedLangs.join(','),
                count: $('#count-range').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
        success: function (data) {
            showRecommendations(data);
        },
        error: function (data) {
            console.log("Error occured during POST: " + data.toString());
        }
    })
}

function selectLanguage(language) {
    if (selectedLangs.includes(language)) {
        return;
    }
    hideSearch();
    langList.appendChild(selectedListItem(language));
    selectedLangs.push(language);
    inputBox.value = '';
}

const selectedListItem = (language) => {
    const item = document.createElement("li");
    item.setAttribute("style", "color: " + language.toHSL())
    item.innerHTML = language;
    return item;
}

const suggestionListItem = (language) => {
    const item = document.createElement("li");
    item.innerText = language;
    item.innerHTML +=
        `<button type="button" title="add" class="btn-add btn btn-warning" onclick="selectLanguage('` + language + `')">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
              <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
            </svg>
        </button>`;
    return item;
}

const meter = (name, percent, color) => {
    let meter = document.createElement("div");
    meter.classList.add("box");
    meter.innerHTML = `<div class="circle" data-dots="70" data-percent="${percent}" style="--bgColor: ${color}"></div>
            <div class="text">
                <h2>${percent}%</h2>
                <small>${name}</small>
            </div>`;
    return meter;
}

function hideSearch() {
    searchWrapper.classList.remove("active");
}

function showSearch() {
    searchWrapper.classList.add("active");
}

function showSuggestions(suggestions) {
    removeAllChildNodes(suggBox);
    for (const language of suggestions) {
        suggBox.appendChild(language);
    }
}

function showRecommendations(data) {
    if (data === undefined) {
        return;
    }
    removeAllChildNodes(meters);
    data.forEach((lang) => {
        meters.appendChild(meter(lang.name, Math.round(lang.value * 100), lang.name.toHSL()));
    });
    meters.setAttribute("style", "opacity: 1");
    selectedLangs = [];
    langList.innerHTML = '';
    updateMeters();
}

function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}

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
    let h, s, l;
    opts = opts || {};
    opts.hue = opts.hue || [0, 360];
    opts.sat = opts.sat || [75, 100];
    opts.lit = opts.lit || [40, 60];

    const range = function (hash, min, max) {
        const diff = max - min;
        const x = ((hash % diff) + diff) % diff;
        return x + min;
    };

    let hash = 0;
    if (this.length === 0) return hash;
    for (let i = 0; i < this.length; i++) {
        hash = this.charCodeAt(i) + ((hash << 5) - hash);
        hash = hash & hash;
    }

    h = range(hash, opts.hue[0], opts.hue[1]);
    s = range(hash, opts.sat[0], opts.sat[1]);
    l = range(hash, opts.lit[0], opts.lit[1]);

    return `hsl(${h}, ${s}%, ${l}%)`;
}