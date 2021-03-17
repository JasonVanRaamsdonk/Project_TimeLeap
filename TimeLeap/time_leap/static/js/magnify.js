window.onload = function() { // add window.onload here and set it euqal to a function
  // Get the modal
  var modal = document.getElementById('myModal');

  // Get the image and insert it inside the modal - use its "alt" text as a caption
  var img = document.getElementById('image_uploader');
  var modalImg = document.getElementById("image_expand");
  var captionText = document.getElementById("caption");
  img.onclick = function() {
    modal.style.display = "block";
    modalImg.src = this.src;
    console.log("- Image magnigication executed!")
    // captionText.innerHTML = this.alt;
  }

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    modal.style.display = "none";
    console.log("- Image magnigication ended!")
  }

  modal.onclick = function() {
      modal.style.display = "none";
      console.log("- Image magnigication ended!")
  }

} // close the function
