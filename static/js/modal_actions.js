const $ = document;
const modal = $.getElementsByClassName("modal")[0];
const close = $.getElementById("modal-close");
const modalForm = $.getElementById("modal-form");
const submitButtonText = (val)=>{
  return `
<div ">
<input type="button" value="${val}" id="modal-form-sumbit" 
  style="height:fit-content;width:fit-content;">
</div>
`
;}
let state = "";

function getCookie(name) {
  let cookieValue = null;
  if ($.cookie && $.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
async function ajax(loc, cbSuccess, method = "GET", body = undefined) {
  await fetch(`${location.origin}/api/${loc}`, {
    method:method,
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body:JSON.stringify( body)
  })
    .then((res) => (res.ok ? res.json() : Promise.reject))
    .then((json) => cbSuccess(json))
    .catch((err) => {
      alert("Se ha prducido un error en el servidor.");
      console.log(err);
    });
  }

async function quick_pay() {
  modalForm.innerHTML = `
    <p>Escriba el nombre <b>o</b> el ID del cliente. </p>
    <label for="in-name">Nombre:</label>
    <input type="text" id='in-name' class="in">

    <label for="in-id">ID:</label>
    <input type="number" id="in-id" class="in">
    
    <label for="in-fee">Total:</label>
    <input type="number" value="320" id='in-fee' class="in">
    
    
    ${submitButtonText('Pagar')}
    <p>
    <small>
    Anotar cuanto se pagó. Si excede o falta se registrará automaticamente.
    </small>
    </p>
    `;
}
function quick_register() {
  modalForm.innerHTML = `
    <label for="in-name">Nombre:</label>
    <input type="text" id='in-name' class="in">

    <label for="in-type">Tipo de cliente:</label>
    <select id="in-type" class="in">
        <option value="month">Mensual</option>
        <option value="week">Semanal</option>
        <option value="visit">Visita</option>
    </select>
    
    <label for="in-fee">Cuota:</label>
    <input type="number" value="320" id='in-fee'class="in" >
    
    <label for="in-fee-numb">Cuota de inscripción:</label>
    <input type="number" value="50" id="in-fee-ins" class="in">

    <label for="in-recoms">Recomendaciones:</label>
    <textarea name="" id="in-recoms" cols="30" rows="5" class="in"
     placeholder="Escriba sus recomendaciones para el nuevo usuario.">
    </textarea>

    ${submitButtonText('Registrar')}
    `;
}
function quick_pay_product() {
  modalForm.innerHTML = `
    <p>Ingrese el nombre <b>o</b> el ID del producto. </p>
    <label for="in-name">Nombre:</label>
    <input type="text" id='in-name' class="in">

    <label for="in-id">ID:</label>
    <input type="number" id="in-id" class="in">
    
    <label for="in-fee">Total:</label>
    <input type="number" value="" id='in-fee' class="in">

    ${submitButtonText('pagar')}
    `;
}
async function task_plus() {
  let users = "";
  await ajax("getstaff", (json) => {
    json.users.forEach((usr) => {
      users = users + `<option>${usr}</option>`;
    });
  });
  modalForm.innerHTML = `
  <label for="in-name">Nombre de la tarea:</label>
  <input type="text" id="in-name" class="in" />
  
  <label for="in-staff">Dirigida a :</label>
  <select name="" id="in-staff" class="in">
    ${users}
  </select>
  
  <label for="">Importancia</label>
  <input type="range" max="3" min="1" value="1" class="in">
  
  <label for="">Entrega</label>
  <input type="time"  class="in">
  
  <label for="in-descr">Breve descripción:</label>
  <textarea name="" id="" cols="30" rows="5" id="in-descr" class="in"> </textarea>
    ${submitButtonText('Añadir')}
    `;
}
function task_compl(){
  modalForm.innerHTML = `
  ${submitButtonText('¿Seguro que ya completaste tu deber? 🤔')}
  `
}

/* Usadas en la vista del inventario */
async function ModalAddItem(){
  let clusters = ''
  await ajax(`getcluster`,json=>{
    json.clusters.forEach(cl=>{
      clusters = clusters + `<option>${cl}</option>`
    })
  })
  modalForm.innerHTML = `
  <label>Nombre:</label>
  <input type="text" class="in"/>

  <label for="">Grupo:</label>
  <select name="" id="" class="in">
    ${clusters}
  </select>

  <label for="">Precio:</label>
  <input type="number" class="in" value="0"> 
  ${submitButtonText("Agregar")}
  `
}
function ModalAddGroup(){
  modalForm.innerHTML = `
  <label>Nombre </label>
  <input type="text" class="in" />
  ${submitButtonText("Agregar")}
  `
}
async function ModalUpdateItem(id){
  let clusters = ''
  await ajax(`getcluster`,json=>{
    json.clusters.forEach(cl=>{
      clusters = clusters + `<option>${cl}</option>`
    })
  })

  modalForm.innerHTML = `
  <input type="number" class="in" style="visibility:hidden" value="${id}"/>
  <hr />
  <label for="">Nombre:</label>
  <input type="text" class="in"/>

  <label for="">Grupo:</label>
  <select name="" id="" class="in">
    ${clusters}
  </select>

  <label for="">Precio:</label>
  <input type="number" class="in"/>

  ${submitButtonText("Modificar")}
  `
}
function ModalDelItem(id){
  modalForm.innerHTML = `
  <input type="number" value="${id}" class='in' style="visibility:hidden">
  ${submitButtonText("¿Está seguro de que desea eliminarlo?")}
  `
}
function ModalUpdateGroup(id){
  
  modalForm.innerHTML = `
    <input type="number" class="in" style="visibility:hidden" value="${id}"/>
    <hr />
    <label for="">Nombre:</label>
    <input type="text" name="" id="" class="in">

    ${submitButtonText("Modificar")}
  `
}
function ModalDelGroup(id){
  modalForm.innerHTML = `
    <input type="number" class="in" style="visibility:hidden" value="${id}"/>
    ${submitButtonText("¿Está seguro de que desea eliminarlo?")}
  `
}
