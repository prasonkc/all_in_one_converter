let convertedVideoBlob = null;

const uploadBox = document.querySelector(".upload-box");
const videoInput = document.getElementById("videoInput");
const convertBtn = document.getElementById("convertBtn"); // Get the Convert button element
const downloadBtn = document.getElementById("downloadBtn");
const preview = document.getElementById("preview");

uploadBox.addEventListener("dragover", (e) => {
  e.preventDefault();
  uploadBox.style.border = "2px dashed #007bff";
});

uploadBox.addEventListener("dragleave", () => {
  uploadBox.style.border = "2px dashed #007bff";
});

uploadBox.addEventListener("drop", (e) => {
  e.preventDefault();
  uploadBox.style.border = "2px dashed #007bff";
  convertedVideoBlob = e.dataTransfer.files[0];
  convertBtn.style.display = "block"; // Show the Convert button
});

uploadBox.addEventListener("click", () => {
  videoInput.click();
});

videoInput.addEventListener("change", () => {
  convertedVideoBlob = videoInput.files[0];
  console.log("Selected file:", convertedVideoBlob);
  convertBtn.style.display = "block"; // Show the Convert button
});

function convertVideo() {
  const videoInput = document.getElementById("videoInput");
  const selectedFile = videoInput.files[0];
  const formatSelect = document.getElementById("formatSelect");
  const selectedFormat = formatSelect.value;
  const convertBtn = document.getElementById("convertBtn");
  const uploadStatus = document.getElementById("uploadStatus");
  const loadingAnimation = document.getElementById("loadingAnimation");

  if (selectedFile) {
    uploadStatus.style.display = "block";
    loadingAnimation.style.display = "block";

    const formData = new FormData();
    formData.append("video", selectedFile);
    formData.append("format", selectedFormat);

    console.log(formData);

    fetch("/video_to_video_converter", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((result) => {
        console.log(result);
        convertBtn.style.display = "none";
        downloadBtn.style.display = "block";
        preview.style.display = "block";
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
}

function downloadConvertedVideo() {
  if (convertedVideoBlob) {
    const a = document.createElement("a");
    a.href = URL.createObjectURL(convertedVideoBlob);
    a.download = "converted_video.mp4"; // Change the filename as needed
    a.click();
  }
}
