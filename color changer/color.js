const Btn = document.getElementById('changeColorBtn');
const container = document.querySelector('.container');
const inputbox = document.getElementById('colorInput');

function color(){
    const color = inputbox.value;
    container.style.backgroundColor = color;
}

Btn.addEventListener('click', color);
