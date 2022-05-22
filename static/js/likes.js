import { ajax } from "./ajax.js";

const $ = document
const likes = Array.from($.getElementsByClassName("like"));
const dislikes = Array.from($.getElementsByClassName("dislike"));
const checks = Array.from($.getElementsByClassName("check"));
const disps = Array.from($.getElementsByClassName("disp"));

//Código recomendado por: https://docs.djangoproject.com/en/3.1/ref/csrf/
function deletion(cls) {
  cls.forEach((el, idx) => {
    el.addEventListener("click", async (ev) => {
      if (el.className === "like" || 'dislike' || 'check') {
        const id = el.parentElement.id.split('_')[1]
        /*fetch(`${location.origin}/api/v1`, {
          method: "POST",
          headers: {
            "X-CSRFToken": getCookie("csrftoken"),
          },
          body:JSON.stringify({btn:el.className,id:id})
        })
          .then((res) => disps[idx].remove())
          .catch((err) => alert(err));*/
         await ajax('v1',res=>disps[idx].remove(),'POST',{
          btn:el.className,id:id
        })
      }
    });
  });
}

deletion(likes);
deletion(dislikes);
deletion(checks)
