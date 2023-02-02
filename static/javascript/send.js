const form = document.querySelector('#login-form');
const hideShow = document.querySelector('.hide-show');

// Perform action for from
form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const username = document.getElementById('username').value.trim();
  const password = document.getElementById('password').value.trim();

  const data = { username, password };

  const response = await fetch('http://127.0.0.1:9000/login', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  });

  const result = await response;

  // Check if the server responed with 200 status
  if (response.status === 200) {
    window.location = response.url;
  }
  // If not 200 there must be an error at one of credentials
  else {
    const formFirstChild = form.firstElementChild
    const result = await response.json();
    if (formFirstChild.classList.contains('alert')) {
      formFirstChild.innerText = result.message;
      formFirstChild.classList.add('wrong-credentials-again');
      setTimeout(() => {
        formFirstChild.classList.remove('wrong-credentials-again')
      }, 400);
    }
    else {
      const body = document.getElementsByTagName('body');
      const div = document.createElement('div');
      div.classList.add('alert');
      div.classList.add('alert-danger');
      div.classList.add('fw-semibold');
      div.innerText = result.message;
      form.prepend(div);
    }
  }

});

// Toggle for hide or show password
hideShow.addEventListener('click', hideShowPassword);

function hideShowPassword() {
  const passwordInput = document.getElementById('password');
  if (passwordInput.type === 'password') {
    passwordInput.setAttribute('type', 'text');
    hideShow.classList.add('show');
  }
  else {
    passwordInput.setAttribute('type', 'password');
    hideShow.classList.remove('show');
  }
};
