// function upload() {
//     var imgcanvas = document.getElementById('image_uploader');
//     var fileinput = document.getElementById('image_input');
//
//     var image = new SimpleImage(fileinput);
//     image.drawTo(imgcanvas);
// }

var colouriseButton = document.getElementById("colourise_button")
    fileinput = document.getElementById("image_input"),
    imgcanvas = document.getElementById("image_uploader"),
    downloadButton = document.getElementById("download_button"),
    canvasWrapper = document.getElementById("image_wrapper"),
    imageMagnifier = document.getElementById("image_expand");

// EVENT LISTENERS

fileinput.addEventListener("change", function() {
    if (fileinput.files.length == 0){
        console.log("no file selected!")
        disabledButton(this);
    } else {
        console.log("- Image uploaded!")
        enableButton(this);
    }
});

colouriseButton.addEventListener("click", function() {
  changeImage(fileinput);
  // document.getElementById("download_button").disabled = false
  console.log("- Colourising performed!")
});

downloadButton.addEventListener("click", function() {
    console.log("- Image downloaded!")
})

// downloadButton.addEventListener("click", () => {
//     let imagePath = imgcanvas.getAttribute('src');
//     let fileName = getFileName(imagePath);
//
//     FileSaver.saveAs(imagePath, fileName);
// });

// FUNCTIONS

function getFileName(str){
    return str.substring(str.lastIndexOf('/') + 1);
}

function enableButton() {
    document.getElementById("colourise_button").disabled = false;
}

function disabledButton() {
    document.getElementById("colourise_button").disabled = true;
}

function changeImage(input) {
  var reader;

  if (input.files && input.files[0]) {
    reader = new FileReader();

    reader.onload = function(e) {
      imgcanvas.setAttribute('src', e.target.result);
      canvasWrapper.setAttribute('href', e.target.result);
      // imageMagnifier.setAttribute('src', e.target.resutt);
    }

    reader.readAsDataURL(input.files[0]);
  }
}
