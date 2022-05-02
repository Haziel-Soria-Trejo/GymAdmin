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

    default:
      break;
  }
}
async function switch_data(data) {
  switch (state) {
    case "pay":
      await ajax(
        "setdata",
        (e) => {
          alert(e.message);
        },
        "POST",
        {
          subject: "setClientPay",
          name: data[0],
          id: data[1],
          total: data[2],
        }
      );
      break;
    case "register":
      await ajax("setdata", (e) => {}, "POST", {
        subject: "setClient",
        name: data[0],
        membership: data[1],
        fee: data[2],
        advice: data[4],
        paid_until: Date(),
      });
      break;
    case "pay-product":
      await ajax("setdata", (e) => {}, "POST", {
        subject: "setItemSell",
        name: data[0],
        id: data[1],
        total: data[2],
      });
      break;
    case "task":
      await ajax("setdata", (e) => {}, "POST", {
        subject: "setTask",
        name: data[0],
        to: data[1].split(',')[0],
        importance:data[2],
        duration:data[3],
        descr:data[4]
      });
      break;

    default:
      break;
  }
}
function getData() {
  let inputs = modalForm.getElementsByClassName("in");
  let values = Array.from(inputs).map((e) => e.value);
  switch_data(values);
}
$.addEventListener("click", (e) => {
  if (e.target === close) {
    modal.style.display = "none";
  }
  if (e.target.closest(".display-modal")) {
    modal.style.display = "flex";
    switch_id(e.target.closest(".display-modal").id);
  }
  if (e.target.id === "modal-form-sumbit") {
    getData();
  }
});
