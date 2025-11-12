const Btn = document.getElementById("button");
const Weight = document.getElementById("weight").value;
const Height = document.getElementById("height").value;

Weight = parseFloat(Weight);
Height = parseFloat(Height);

function bmi() {
  let BMI = Weight /(Height * Height);
  if (BMI < 18.5) {
    alert("You are Underweight");
  } else if (18.5 < BMI < 24.9) {
    alert("You are Fit");
  } else if (25.0 < BMI < 29.9) {
    alert("You are Overweight");
  } else if (30.0 < BMI < 39.9) {
    alert("You are Obese");
  } else {
    alert("You are morbidly obese");
  }
}
Btn.addEventListener("click", bmi());
