const $ = document

let dates = $.querySelectorAll('.date')
/*Sé que pude simplemente escribir 'pm' o 'am'
dentro de 'date' pero queria intentar hacer esta conversión. :v*/
dates.forEach(el=>{
    let  date = el.innerHTML
    const period = date.slice(date.length-4,date.length)
    date = date.slice(0,date.length-4)
    date = new Date(date).toLocaleString()
    if (period === 'p.m.'){
        const date_split = date.split(' ')
        date = `${date_split[0]} ${
            parseInt(date_split[1].slice(0,2))+12}${
                date_split[1].slice(2)}`
    }


    el.innerHTML = date
})