

if (!localStorage.getItem('c')) {
     localStorage.setItem('c', 0);
    }


document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#counter').innerHTML = localStorage.getItem('c')
    document.querySelector('button').onclick = increment;
});

function increment() {
    let c = localStorage.getItem('c');
    c++;
    document.querySelector('#counter').innerHTML = c;
    localStorage.setItem('c', c);

    if (c % 10 === 0) {
        alert(`The counter value is ${c}`);
    }

    if (c === 5) {
        alert(`The counter equals 5`);
    }
}