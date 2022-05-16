function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
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
  
  
export async function ajax(loc, cbSuccess, method = "GET", body = undefined) {
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