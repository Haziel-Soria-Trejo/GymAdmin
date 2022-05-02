$ = document
const likes = Array.from($.getElementsByClassName("like"));
const dislikes = Array.from($.getElementsByClassName("dislike"));
const disps = Array.from($.getElementsByClassName("disp"));

//Código recomendado por: https://docs.djangoproject.com/en/3.1/ref/csrf/
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

function deletion(cls) {
  cls.forEach((el, idx) => {
    el.addEventListener("click", (ev) => {
      if (el.className === "like" || 'dislike') {
        const id = el.parentElement.id.split('_')[1]
        fetch(`${location.origin}/api/v1`, {
          method: "POST",
          headers: {
            "X-CSRFToken": getCookie("csrftoken"),
          },
          body:JSON.stringify({btn:el.className,id:id})
        })
          .then((res) => disps[idx].remove())
          .catch((err) => alert(err));
      }
    });
  });
}

deletion(likes);
deletion(dislikes);
