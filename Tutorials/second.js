let userScore = 0;
let computerScore = 0;

const logos = document.querySelectorAll(".logo");

const compChoice = () => {
    let choices = ["rock", "paper", "scissors"];
    const randomchoice = Math.floor(Math.random() * 3);
    return choices[randomchoice];
}

const playGame = (userChoice) => {
    console.log("user has choose", userChoice);
    const computerchoice = compChoice();
    console.log("computer has choose", computerchoice);

    if (userChoice === computerchoice) {
        console.log("It's a Draw");
        alert("It's a Draw");
    }
else if (userChoice === "rock" && computerchoice === "scissors" ||
    userChoice === "paper" && computerchoice === "rock" ||
    userChoice === "scissors" && computerchoice === "paper") {
    console.log("User Wins");
    alert("User Wins");
    userScore++;
} else {
    console.log("Computer Wins");
    alert("Computer Wins");
    computerScore++;
}
}
logos.forEach((logo) => {
    console.log(logo);
    logo.addEventListener("click",()=> {
        const userChoice = logo.getAttribute("id");
        console.log("choice was clicked", userChoice);
        playGame(userChoice);
        playGame(computerchoice);
    });
})

if(userScore === "5"|| computerScore === "5"){
    if(userScore === "5"){
        console.log("User is th ultimate winner");
        alert("User is the ultimate winner");
    }
    else{
        console.log("Computer is the ultimate winner");
        alert("Computer is the ultimate winner");
    }
}