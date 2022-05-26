function switch_id(id) {
  switch (id) {
    case "quick_pay":
      state = "pay";
      quick_pay();
      break;
    case "quick_register":
      state = "register";
      quick_register();
      break;
    case "quick_pay-product":
      state = "pay-product";
      quick_pay_product();
      break;
    case "task-plus":
      state = "task";
      task_plus();
      break;
    case "item-add":
      state = "item-add";
      ModalAddItem();
      break;
    case "cluster-add":
      state = "group-add";
      ModalAddGroup();
      break;
    case "upgradeStaff":
      state = "upgradeStaff";
      upgradeStaff();
      break;
    case "add_disp":
      state = "add_disp";
      add_disp();
      break;
    default:
      break;
  }
}
const customAjax = async (body) => {
  ajax(
    "setdata",
    (e) => {
      e.message ? alert(e.message) : null;
    },
    "POST",
    body
  );
};
async function switch_data(data) {
  switch (state) {
    case "pay":
      await customAjax({
        subject: "setClientPay",
        name: data[0],
        id: data[1],
        total: data[2],
      });
      break;
    case "register":
      if(data[0]===''){
        alert('El nombre no puede ser nulo.')
        return
      }
      await customAjax({
        subject: "setClient",
        name: data[0],
        membership: data[1],
        fee: data[2],
        inscription :data[3],
        advice: data[4],
      });
      break;
    case "pay-product":
      await customAjax({
        subject: "setItemSell",
        name: data[0],
        id: data[1],
        total: data[2],
      });
      break;
    case "task":
      await customAjax({
        subject: "setTask",
        name: data[0],
        to: data[1].split(",")[0],
        importance: data[2],
        duration: data[3],
        descr: data[4],
      });
      break;
    case "deltask":
      await customAjax(
        await ajax("setdata", (e) => {}, "POST", {
          subject: "deleteTask",
          id: data,
        })
      );
      break;
    case "item-add":
      await customAjax({
        subject: "addItem",
        name: data[0],
        clusterName: data[1],
        price: data[2],
      });
      break;
    case "group-add":
      await customAjax({
        subject: "addGroup",
        name: data[0],
      });
      break;
    case "update-item":
      await customAjax({
        subject: "updateItem",
        action: "update",
        id: data[0],
        name: data[1] != "" ? data[1] : undefined,
        cluster: data[2] != "" ? data[2] : undefined,
        price: data[3] != "" ? data[3] : undefined,
      });
      break;
    case "del-item":
      await customAjax({
        subject: "updateItem",
        action: "delete",
        id: data,
      });
      break;
    case "update-group":
      await customAjax({
        subject: "updateGroup",
        action: "update",
        id: data[0],
        name: data[1],
      });
      break;
    case "del-group":
      await customAjax({
        subject: "updateGroup",
        action: "delete",
        id: data,
      });
      break;
    case "add_disp":
      await customAjax({
        subject: "addDisp",
        text: data[0],
        staff_to: data[1],
      });
    case "upgradeStaff":
      await customAjax({
        subject: "upgradeStaff",
        staff: data[0],
        rank: data[1],
      });
    default:
      break;
  }
}
function getData() {
  let inputs = modalForm.getElementsByClassName("in");
  let values = Array.from(inputs).map((e) => e.value);
  switch_data(values);
}
function submitModal() {
  if (state === "deltask") {
    switch_data(task_id);
    $.getElementById(`hd_${task_id}`).remove();
  } else if (state === "del-item") {
    switch_data(item_id);
    $.getElementById(`it_${item_id}`).remove();
  } else if (state === "del-group") {
    switch_data(cluster_id);
    $.getElementById(`cl_${cluster_id}`).remove();
  } else {
    getData();
  }
}
/*Las siguientes variables son los ID de la columna 
seleccionada en una tabla*/
let task_id = undefined;
let item_id = undefined;
let cluster_id = undefined;
$.addEventListener("click", (e) => {
  if (e.target === close) {
    modal.style.display = "none";
  }
  if (e.target.closest(".display-modal")) {
    submited = false
    modal.style.display = "flex";

    /* Los siguientes  if se usan en 
    casos donde se crean distontos botones con la misma funcionalidad
    pero que apuntan a distiontos objetos. */
    if (e.target.className.includes("is_compl")) {
      state = "deltask";
      task_id = e.target.id.slice(3);
      task_compl();
    } else {
      switch_id(e.target.closest(".display-modal").id);
    }
  }
  if (e.target.id === "modal-form-submit") {
    submitModal();
    modal.style.display = "none";
  }
});

modalForm.addEventListener("keypress", (e) => {
  if (e.key == "Enter" && $.activeElement!=$.getElementById('modal-form-submit')) {
    submitModal();
    modal.style.display = "none";
  }
});

function updateItem(id) {
  state = "update-item";
  ModalUpdateItem(parseInt(id));
}
function delItem(id) {
  state = "del-item";
  item_id = id;
  ModalDelItem(parseInt(id));
}
function updateGroup(id) {
  state = "update-group";
  ModalUpdateGroup(parseInt(id));
}
function delGroup(id) {
  state = "del-group";
  cluster_id = id;
  ModalDelGroup(parseInt(id));
}
