var i = 0;
function myFunction() {
  console.log("it works");
  if(i%2==0) {
    document.body.style.backgroundImage = "url(static/bg2.png)";
    document.getElementById("lightdark").style.backgroundImage = "url(static/light.png)";
    document.getElementById("heading").style.color = "#424242";
    document.getElementById("heading4").style.color = "#424242";
    document.getElementById("heading42").style.color = "#424242";
    document.getElementById("submit1").style.border = "2px solid #424242";
    document.getElementById("submit2").style.border = "2px solid #424242";
    document.getElementById("submit1").style.color = "#424242";
    document.getElementById("submit2").style.color = "#424242";
    document.getElementById("input1").style.background = "#ffffff";
    document.getElementById("input2").style.background = "#ffffff";
    document.getElementById("input1").style.border = "2px solid #424242";
    document.getElementById("input2").style.border = "2px solid #424242";
    document.getElementById("input1").style.color = "#424242";
    document.getElementById("input2").style.color = "#424242";
  }
  else {
    document.body.style.backgroundImage = "url(static/bgdark.png)";
    document.getElementById("lightdark").style.backgroundImage = "url(static/dark.png)";
    document.getElementById("heading").style.color = "#ECECEC";
    document.getElementById("heading4").style.color = "#ECECEC";
    document.getElementById("heading42").style.color = "#ECECEC";
    document.getElementById("submit1").style.border = "2px solid #ECECEC";
    document.getElementById("submit2").style.border = "2px solid #ECECEC";
    document.getElementById("submit1").style.color = "#ECECEC";
    document.getElementById("submit2").style.color = "#ECECEC";
    document.getElementById("input1").style.background = "#2f3763";
    document.getElementById("input2").style.background = "#2f3763";
    document.getElementById("input1").style.border = "2px solid #ECECEC";
    document.getElementById("input2").style.border = "2px solid #ECECEC";
    document.getElementById("input1").style.color = "#ECECEC";
    document.getElementById("input2").style.color = "#ECECEC";
  }
  i++;
  console.log(i);
}

function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}
