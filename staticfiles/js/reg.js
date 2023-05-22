document.addEventListener('DOMContentLoaded', function(){
  document.querySelector("#reg_sub").disabled = true;
  document.getElementById("pw_msg").style.display = "none";
  document.getElementById("user_msg").style.display = "none";
  document.querySelector('#username').oninput = name_check;
  document.querySelector("#pw1").oninput = pw_check;
  document.querySelector("#pw2").oninput = pw2_check;
  document.querySelector('#reg_sub').onclick = reg_sub;
}, false);

function reg_sub(){
  document.querySelector('#pw1').disabled = false;
}

function name_check(event) {
  var all_names = [{% for user in users %}'{{ user.username|escapejs }}',{% endfor %}];
  if(!all_names.includes(event.target.value) && event.target.value.length > 5){
    document.getElementById("user_msg").style.display = "none";
    window.uT = true;
  }
  else {
    document.getElementById("user_msg").style.display = "block";
    document.getElementById('user_len').style.color = "red";
    window.uT = false;
  }
}

function pw_check(event){
  var c1 = pw_lenght(event);
  var c2 = pw_lowCase(event);
  var c3 = pw_upCase(event);
  var c4 = pw_Num(event);
  var c5 = pw_chr(event);

  window.p1 = event.target.value;

  if(c1 && c2 && c3 && c4 && c5){
    document.getElementById("pw_msg").style.display = "none";
    window.pT = true;
  }
  else{
    document.getElementById("pw_msg").style.display = "block";
    window.pT = false;
  }

}

function pw2_check(event){
  document.querySelector('#pw1').disabled = true;
  if(p1 == event.target.value && pT && uT){
    document.querySelector("#reg_sub").disabled = false;
  }
  else{
    document.querySelector("#reg_sub").disabled = true
  }

}

function pw_lenght(event){
  if(event.target.value.length >= 8){
    document.getElementById("pw_len").style.color = "green";
    return true;
  }
  else{
    document.getElementById("pw_len").style.color = "red";
    return false;
  }
}

function pw_lowCase (event) {
  var lowerCaseLetters = /[a-z]/g;
  if(event.target.value.match(lowerCaseLetters)){
    document.getElementById("pw_lc").style.color = "green";
    return true;
  }
  else{
    document.getElementById("pw_lc").style.color = "red";
    return false;
  }
}

function pw_upCase(event) {
  var upperCaseLetters = /[A-Z]/g;
  if(event.target.value.match(upperCaseLetters)){
    document.getElementById("pw_uc").style.color = "green";
    return true;
  }
  else{
    document.getElementById("pw_uc").style.color = "red";
    return false;
  }
}

function pw_Num(event) {
  var numbers = /[0-9]/g;
  if(event.target.value.match(numbers)){
    document.getElementById("pw_n").style.color = "green";
    return true;
  }
  else{
    document.getElementById("pw_n").style.color = "red";
    return false;
  }
}

function pw_chr(event){
  var chara = /[!@#$%&*]/;
  if(event.target.value.match(chara)){
    document.getElementById("pw_sc").style.color = "green";
    return true;
  }
  else{
    document.getElementById("pw_sc").style.color = "red";
    return false;
  }
}
