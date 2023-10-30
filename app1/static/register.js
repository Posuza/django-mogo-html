console.log("this is javascript");

const form = document.getElementById('form')
const username = document.getElementById('username');
const email = document.getElementById('email');
const phone = document.getElementById('phone');
const bio = document.getElementById('bio');
const password = document.getElementById('password');
const passwor2 = document.getElementById('passwor2');

form.addEventListener('submit',e=>{
    e.preventDefault();
    validateInput();
});

const setError = (element,message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classlist.add('error');
    inputControl.classlist.remove('success')
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classlist.add('success');
    inputControl.classlist.remove('error')
}

const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const validateInput = () =>{
    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const phoneValue =  phone.value.trim();
    const bioValue = bio.value.trim();
    const passwordValue = password.value.trim();
    const password2Value =password2.value.trim();s

    if(usernameValue === ''){
        console.log("error")
        setError(username,'Username is required!')
    }else{
        setSuccess(username)
    }

    if(emailValue === '') {
        setError(email, 'Email is required');
    } else if (!isValidEmail(emailValue)) {
        setError(email, 'Provide a valid email address');
    } else {
        setSuccess(email);
    }

    if(phoneValue === '') {
        setError(phone, 'Phone number is required');
    } else if (phoneValue.length < 10 ) {
        setError(phone, 'Phone number must be at least 10 character.')
    } else {
        setSuccess(phone);
    }

    if(passwordValue === '') {
        setError(password, 'Password is required');
    } else if (passwordValue.length < 8 ) {
        setError(password, 'Password must be at least 8 character.')
    } else {
        setSuccess(password);
    }

    if(password2Value === '') {
        setError(password2, 'Please confirm your password');
    } else if (password2Value !== passwordValue) {
        setError(password2, "Passwords doesn't match");
    } else {
        setSuccess(password2);
    }

};
