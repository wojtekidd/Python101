function bindOnClickToButton() {
    document.querySelector("button").onclick = increment;
}

document.addEventListener("DOMContentLoaded", bindOnClickToButton);

let c = 0;

function increment() {
    c++;
    document.querySelector("h1").innerHTML = c;

    if (c % 10 === 0) {
        alert(`The counter value is ${c}`);
    }

    if (c == 5) {
        alert(`The counter equals 5`);
    }
}