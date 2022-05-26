import { ajax } from "./ajax.js";

document.addEventListener("change", (e) => {
  console.log(e.target.classList);
  if (e.target.classList.contains("is_active")) {
    const id = e.target.id.slice(6);
    ajax("active-client", (e) => {}, "POST", {
      id,
    });
  }
});

//Fechas de pago
const dates = Array.from(document.getElementsByClassName("dateUntil")),
checks = Array.from(document.getElementsByClassName('is_active'))

dates.forEach((dt,idx) => {
  const now = new Date(),
  row = dt.closest('.client')

  if(!checks[idx].checked){
      return
  }

  let date = dt.innerText.split("/");

  date = new Date(date[2], date[1] - 1, date[0]);
console.log(row);
  if(date<=now){
    row.style = "background-color:#cc3300"
  }
  else{
    row.style = "background-color:#99cc33"
  }
});
