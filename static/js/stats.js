import { DrawChart, getFilters } from "./stats-utils.js";

async function ajax(loc, cbSuccess) {
  await fetch(`${origin}/api/${loc}`)
    .then((res) => {
      return res.ok ? res.json() : Promise.reject;
    })
    .then((json) => {
      cbSuccess(json);
    })
    .catch((err) => {
      alert("Ha ocurrido un error en el servidor.");
      console.log(err);
    });
}
let chart = new DrawChart();
const submitFilter = document.getElementById("submit-filter");

document.addEventListener("DOMContentLoaded", (e) => {
  //const { activity,time,filter,dmax,dmin} = setData(); 
});

async function setData() {
  const { filters, chartTime, chartFilter } = getFilters();
  await ajax(`stats?q=${JSON.stringify(filters)}`, (e) => {
    const dmax = filters.timemax,
      dmin = filters.timemin;;
    chart.start(e.activity, chartTime, chartFilter, dmax, dmin)
    chart.createChart();
    //return [e.activity, chartTime, chartFilter, dmax, dmin]
  });
}

submitFilter.addEventListener("click", async (e) => {
  e.preventDefault();
  setData();
});
const excelBtn = document.getElementById('excel')
excelBtn.addEventListener('click',e=>{
  ajax('sheet',e=>{})
})