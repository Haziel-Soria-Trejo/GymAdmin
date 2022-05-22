import {ajax} from './ajax.js'

document.addEventListener('change',e=>{
    console.log(e.target.classList);
    if (e.target.classList.contains('is_active')){
        const id = e.target.id.slice(6)
        ajax('active-client',e=>{},'POST',{
            id
        })
    }
})