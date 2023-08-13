document.addEventListener("DOMContentLoaded", function () {
  let videoBlob;

  const uploadBox = document.querySelector(".upload-box");
  const videoInput = document.getElementById("videoInput");
  const convertBtn = document.getElementById("convertBtn");
  const downloadBtn = document.getElementById("downloadBtn");
  const dropboxText = document.getElementById("dropboxText");
  const attachment = document.getElementById("attachment");
  const preview = document.getElementById("preview");

  uploadBox.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadBox.style.border = "2px dashed #007bff";
  });

  uploadBox.addEventListener("dragleave", () => {
    e.preventDefault();
    uploadBox.style.border = "2px dashed #007bff";
  });

  uploadBox.addEventListener("drop", (e) => {
    e.preventDefault();
    uploadBox.style.border = "2px dashed #007bff";
    videoBlob = e.dataTransfer.files[0];
    updateAttachment(videoBlob.name);
    preview.style.display = "none";
  });

  uploadBox.addEventListener("click", () => {
    videoInput.click();
  });

  videoInput.addEventListener("change", () => {
    videoBlob = videoInput.files[0];
    console.log("Selected file:", videoBlob);
    convertBtn.style.display = "block";
    preview.style.display = "none";
    updateAttachment(videoBlob.name);
  });

  convertBtn.addEventListener("click", () => {
    convertVideo();
  });

  downloadBtn.addEventListener("click", () => {
    downloadConvertedVideo();
  });

  function updateAttachment(fileName) {
    attachment.textContent = `Attached File: ${fileName}`;
    dropboxText.style.display = "none";
    attachment.style.display = "block";
  }

  function convertedAnimationFrontend() {
    const convertBtn = document.getElementById("convertBtn");
    const uploadStatus = document.getElementById("uploadStatus");
    const loader = document.getElementById("loader");

    convertBtn.style.display = "none";
    downloadBtn.style.display = "block";
    uploadStatus.style.display = "none";
    attachment.innerHTML = `Converted file: ${videoBlob.name}`;
    attachment.style.display = "block";
    loader.style.display = "none";
  }

  function performRequest(selectedFile, selectedFormat, url) {
    const formData = new FormData();
    formData.append("video", selectedFile, selectedFile.name);
    formData.append("format", selectedFormat);

    console.log(formData);

    fetch(url, {
      method: "POST",
      body: formData,
      headers: {
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        const convertedFilename = data.filename;
        const convertedURL = "/converted/" + convertedFilename;

        console.log(convertedFilename);
        console.log(convertedURL);

        convertedAnimationFrontend();

        preview.src = convertedURL;
        preview.style.display = "block";
        preview.innerHTML = "Download Ready";

        downloadBtn.setAttribute("data-converted-file", convertedFilename);
        downloadBtn.setAttribute("data-converted-url", convertedURL);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  function convertVideo() {
    const videoInput = document.getElementById("videoInput");
    const selectedFile = videoInput.files[0];

    const currentUrl = window.location.href;

    if (selectedFile) {
      uploadStatus.style.display = "block";
      dropboxText.style.display = "none";
      loader.style.display = "block";
      attachment.style.display = "none";

      if (currentUrl.includes("/video_to_video_converter")) {
        const formatSelect = document.getElementById("formatSelect");
        const selectedFormat = formatSelect.value;

        url = "/video_to_video_converter";
        performRequest(selectedFile, selectedFormat, url);
      } else if (currentUrl.includes("/video_to_audio_converter")) {
        const formatSelect = document.getElementById("formatSelect");
        const selectedFormat = formatSelect.value;

        url = "/video_to_audio_converter";
        performRequest(selectedFile, selectedFormat, url);
      } else if (currentUrl.includes("/video_to_gif_converter")) {
        const selectedFormat = "gif";

        url = "/video_to_gif_converter";
        performRequest(selectedFile, selectedFormat, url);
      } else if (currentUrl.includes("/video_to_frames_converter")) {
        const formatSelect = document.getElementById("formatSelect");
        const selectedFormat = formatSelect.value;

        url = "/video_to_frames_converter";
        performRequest(selectedFile, selectedFormat, url);
      } else if (currentUrl.includes("/image_to_image_converter")) {
        const formatSelect = document.getElementById("formatSelect");
        const selectedFormat = formatSelect.value;

        url = "/image_to_image_converter";
        performRequest(selectedFile, selectedFormat, url);
      }
    }
  }

  function downloadConvertedVideo() {
    const downloadBtn = document.getElementById("downloadBtn");
    const convertedFilename = downloadBtn.getAttribute("data-converted-file");
    const convertedURL = downloadBtn.getAttribute("data-converted-url");
    const preview = document.getElementById("preview");
    const convertBtn = document.getElementById("convertBtn");

    const a = document.createElement("a");
    a.style.display = "none";
    a.href = convertedURL;
    a.download = convertedFilename;
    preview.innerHTML = "Download Complete";
    convertBtn.style.display = "block";
    downloadBtn.style.display = "none";
    attachment.style.display = "none";
    dropboxText.style.display = "block";

    document.body.appendChild(a);
    a.click();

    document.body.removeChild(a);
  }
});
