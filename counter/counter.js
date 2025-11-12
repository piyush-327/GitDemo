document.addEventListener("DOMContentLoaded", () => {
  const counter = document.getElementById("counter");
  const increase = document.getElementById("in");
  const decrease = document.getElementById("de");
  const reset = document.getElementById("re");
  let count = 0;

  function increased() {
    count++;
    counter.textContent = count;
  }
  function decreased() {
    count--;
    counter.textContent = count;
  }
  function reseted() {
    count = 0;
    counter.textContent = count;
  }

  increase.addEventListener("click", increased);
  decrease.addEventListener("click", decreased);
  reset.addEventListener("click", reseted);
});
