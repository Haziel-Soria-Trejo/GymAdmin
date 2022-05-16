 export class DrawChart {
    constructor() {
        this.chartElement = document.getElementById('myChart')
        this.chart = new Chart(this.chartElement,{})//vacio
    }
    start(...params){
        const [data, time, type, dmax, dmin] = params;
      this.data = data;
      this.time = time;
      this.type = type;
      //La fecha máxima será por default hoy.
      this.dmax = dmax === "" ? new Date().getTime() : new Date(dmax).getTime();
  
      //La fecha mínima será por default 30 días.
      this.dmin =
        dmin === ""
          ? new Date().getTime() - 30 * 24 * 3600 * 1000
          : new Date(dmin).getTime();

      this.setPeriods();
    }
    setPeriods() {
      const periods = {
        hr: 3600 * 1000,
        dy: 24 * 3600 * 1000,
        wk: 7 * 24 * 3600 * 1000,
        mt: 4 * 7 * 24 * 3600 * 1000, //4 semanas aprox= 1mes
      };
  
      //const ticksNumber = (this.dmax - this.dmin) / periods[this.time] - 1;
      const time = periods[this.time];
      const ticks = [];
      for (let i = this.dmin; i <= this.dmax; i = i + time) {
        ticks.push(new Date(i).toLocaleString());
      }
      this.ticks = ticks;
  
      this.configData(time);
    }
    configData(time) {
      const dtArray = this.data;
      let minDynamic = new Date(dtArray[0].date),
        maxDynamic = 0,
        amount = 0,
        dataRanges = [];
  
      dtArray.forEach((el, i) => {
        maxDynamic = new Date(el.date);
  
        if (maxDynamic - minDynamic > time) {
          const pastMax = new Date(dtArray[i - 1].date);
          dataRanges.push([minDynamic, pastMax, amount]);
  
          amount = el.amount;
          minDynamic = maxDynamic;
          /*Es una analogía a empezar 
           de cero el recorrido del array */
        } else {
          amount += el.amount;
        }
        if (i === dtArray.length - 1) {
          dataRanges.push([minDynamic, maxDynamic, amount]);
        }
      });
      console.log(dataRanges);
      this.labels = dataRanges.map((e) => {
        return `${e[0].toLocaleString()}<--->${e[1].toLocaleString()}`;
      });
      this.amounts = dataRanges.map((e) => {
        return e[2];
      });
    }
    createChart() {
      console.log(this.labels,this.amounts)
      this.chart.destroy()
      
      this.chart = new Chart(this.chartElement, {
        type: "bar",
        data: {
          labels: this.labels,
          datasets: [{
            label:"Barras",
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: this.amounts
          }]
        },
        options: {}
      });
    }
  }

export function getFilters() {
    const ids = ["staff", "type", "timemax", "timemin"];
    let filters = {};
  
    ids.forEach((val) => {
      filters[val] = document.getElementById(`filter-${val}`).value;
    });
  
    const chartTime = document.getElementById("filter-time").value;
    const chartFilter = document.getElementById("filter-chartType").value; //para los gráficos
  
    return { filters, chartFilter, chartTime }; //los valores predeterminados se harán en el backend.
  }