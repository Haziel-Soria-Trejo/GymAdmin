import {ajax} from './ajax.js'

function getPsw(){
    const password = document.getElementById('psw-id').value
    return password
}
let clickOnce = false
document.getElementById('settings-section').addEventListener('click',async e=>{
    if(clickOnce) return
    e.preventDefault()
    if(e.target.id === 'change-psw'){
        const psw1 = document.getElementById('psw1').value,
        psw2 = document.getElementById('psw2').value
        
        if (psw1 !== psw2 ){
            alert("Las contraseñas no coinciden")
            return
        }
        if(psw1 === ''){
            alert("No puede estar vacia")
            return
        }
        
        
    }
    if (e.target.classList.contains('changeStaff')){
        let onClick = false
        clickOnce = true
        await ajax('verify-psw',res=>{
            if(res.status === 'ok'){
                onClick = true
            }
            else{
                alert('No autorizado!')
            }
        //form.submit()
    },'POST',{
        password:getPsw()
    })
    if(onClick) {
        clickOnce = true
       e.target.click()
    }
    }
    
})