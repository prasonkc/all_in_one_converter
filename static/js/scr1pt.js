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
    const loadingAnimation = document.getElementById("loadingAnimation");

    if (selectedFile) {
      uploadStatus.style.display = "block";
      loadingAnimation.style.display = "block";

      const formData = new FormData();
      formData.append("video", selectedFile, selectedFile.name); // Append video file correctly
      formData.append("format", selectedFormat);

      console.log(formData)

      fetch("/video_to_video_converter", {
        method: "POST",
        body: formData,
        headers: {
          Accept: "application/json",
          "X-Requested-With": "XMLHttpRequest",
        },
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
                if (convert_video_success) {
                const downloadLink = document.getElementById("downloadLink");
                const convertedFilename = response.converted_filename; // Assuming the response contains the converted filename
                const convertedVideoUrl = "../../converted/" + convertedFilename; // Update with your actual path

                downloadLink.href = convertedVideoUrl;
                document.getElementById("downloadDiv").style.display = "block";
            }

  }
});
