function doFirst() {
  A = document.getElementById('A');
  A.addEventListener("dragstart", startDrag, false);
  B = document.getElementById('B');
  B.addEventListener("dragstart", startDrag, false);
  C = document.getElementById('C');
  C.addEventListener("dragstart", startDrag, false);
  leftbox = document.getElementById('leftbox');
  leftbox.addEventListener("dragenter", function(e){e.preventDefault();},false);
  leftbox.addEventListener("dragover", function(e){e.preventDefault();}, false);
  leftbox.addEventListener("drop", dropped, false);
}
function startDrag(e) {
  var code = '<column id="A">';
  e.dataTransfer.setData('Text', code);
}
function dropped(e) {
  e.preventDefault();
  leftbox.innerHTML = e.dataTransfer.getData('Text');
}
window.addEventListener("load", doFirst, false);
