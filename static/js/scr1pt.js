document.addEventListener("DOMContentLoaded", function () {
  const uploadBox = document.querySelector(".upload-box");
  const videoInput = document.getElementById("videoInput");
  const convertBtn = document.getElementById("convertBtn");
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
    convertBtn.style.display = "block";
  });

  uploadBox.addEventListener("click", () => {
    videoInput.click();
  });

  videoInput.addEventListener("change", () => {
    convertedVideoBlob = videoInput.files[0];
    console.log("Selected file:", convertedVideoBlob);
    convertBtn.style.display = "block";
  });

  convertBtn.addEventListener("click", () => {
    convertVideo();
  });

  downloadBtn.addEventListener("click", () => {
    downloadConvertedVideo();
  });

  function convertVideo() {
    const videoInput = document.getElementById("videoInput");
    const selectedFile = videoInput.files[0];
    const formatSelect = document.getElementById("formatSelect");
    const selectedFormat = formatSelect.value;
    const convertBtn = document.getElementById("convertBtn");
    const uploadStatus = document.getElementById("uploadStatus");
    const dropboxText = document.getElementById("dropboxText");
    const preview = document.getElementById("preview")

    if (selectedFile) {
      uploadStatus.style.display = "block";
      dropboxText.style.display = "none";

      const formData = new FormData();
      formData.append("video", selectedFile, selectedFile.name); // Append video file correctly
      formData.append("format", selectedFormat);

      console.log(formData);

      fetch("/video_to_video_converter", {
        method: "POST",
        body: formData,
        headers: {
          Accept: "application/json",
          "X-Requested-With": "XMLHttpRequest",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          const videoFilename = data.video_filename;
          const videoURL = "/converted/" + videoFilename;

          convertBtn.style.display = "none";
          downloadBtn.style.display = "block";
          dropboxText.style.display = "block";
          uploadStatus.style.display = "none";
          
          preview.src = videoURL
          preview.style.display = "block";

          downloadBtn.setAttribute("data-video-file", videoFilename);
          downloadBtn.setAttribute("data-video-url", videoURL);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    }
  }

  function downloadConvertedVideo() {
    const downloadBtn = document.getElementById("downloadBtn");
    const videoFile = downloadBtn.getAttribute("data-video-file");
    const videoURL = downloadBtn.getAttribute("data-video-url");

    const a = document.createElement("a");
    a.style.display = "none";
    a.href = videoURL;
    a.download = videoFile;

    document.body.appendChild(a);
    a.click();

    document.body.removeChild(a);
  }
});
