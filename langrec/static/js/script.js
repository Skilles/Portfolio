// getting all required elements
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
const icon = searchWrapper.querySelector(".icon");
let hiddenLangList = document.getElementById("lang-input")
let langList = document.getElementById("languages")
let meters = document.querySelector(".meter-wrapper");

// if user press any key and release
inputBox.onkeyup = (e)=>{
    let userData = e.target.value; //user entered data
    let emptyArray = [];
    if (userData) {
        emptyArray = suggestions.filter((data)=>{
            //filtering array value and user characters to lowercase and return only those words which are start with user enetered chars
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data)=>{
            // passing return data inside li tag
            return data = `<li>${data}</li>`;
        });
        searchWrapper.classList.add("active"); //show autocomplete box
        showSuggestions(emptyArray);
        let allList = suggBox.querySelectorAll("li");
        for (let i = 0; i < allList.length; i++) {
            //adding onclick attribute in all li tag
            // allList[i].setAttribute("onclick", "select(this)");
            let langName = allList[i].innerText;
            allList[i].innerHTML += `<button type="button" class="btn-add btn btn-warning" onclick="select('` + langName + `')">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                  <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
                </svg>
                </button>`;
        }
    } else {
        searchWrapper.classList.remove("active"); //hide autocomplete box
    }
}

// select a language from the list and add it to the necessary elements
function select(lang_name){
    // console.log(lang_name)
    searchWrapper.classList.remove("active");
    const item = document.createElement("li");
    item.setAttribute("style", "color: " + lang_name.toHSL())
    item.innerHTML = lang_name;
    langList.appendChild(item);
    if (hiddenLangList.value === "") {
        hiddenLangList.value = lang_name;
    } else {
        hiddenLangList.value += "," + lang_name;
    }
    // console.log(hiddenLangList)
    inputBox.value = '';
}

function showSuggestions(list) {
    let listData;
    // if(!list.length){
    //     userValue = inputBox.value;
    //     listData = `<li>
    //                     ${userValue}
    //                 </li>`;
    // }else{
    //    listData = list.join("");
    // }
    listData = list.join('');
    suggBox.innerHTML = listData;
}

const meter = (name, value, color) => {
    let meter = document.createElement("div");
    meter.classList.add("box");
    let percent = value * 100;
    meter.innerHTML = `<div class="circle" data-dots="70" data-percent="${percent}" style="--bgColor: ${color}"></div>
            <div class="text">
                <h2>${percent}%</h2>
                <small>${name}</small>
            </div>`;
    return meter;
}

function showRecommendations(data) {
    if (data === "") {
        return;
    }
    while (meters.firstChild) {
        meters.removeChild(meters.firstChild);
    }
    let languages = JSON.parse(JSON.stringify(data));
    for (let i = 0; i < languages.length; i++) {
        let lang = languages[i];
        meters.appendChild(meter(lang.name, lang.value, lang.name.toHSL()));
    }
    meters.setAttribute("style", "opacity: 1");
    updateMeters();
}