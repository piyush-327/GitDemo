let boxes=document.querySelectorAll('.box');
let reset=document.querySelector('#reset');

let turnO='X';

const winPatterns=[
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
];

boxes.forEach((box)=>{
    box.addEventListener('click',()=>{
        console.log('box was clicked');
            if (turnO === 'X') {
                box.innerText = "X";
                turnO = 'O';    
            } else {
                box.innerText = "O";
                turnO = 'X';
            }
            box.disabled = true;

            checkWinner();
        })
})
const checkWinner = () => {
    for( let pattern of winPatterns){
        let pos1 = boxes[pattern[0]].innerText;
        let pos2 = boxes[pattern[1]].innerText;
        let pos3 = boxes[pattern[2]].innerText;

        if(pos1 !=="" && pos2 !=="" && pos3 !==""){
            if (pos1 === pos2 && pos2 === pos3){
                console.log(`Winner is ${pos1}`);
                alert(`Winner is ${pos1}`);
            }
    }
}
}