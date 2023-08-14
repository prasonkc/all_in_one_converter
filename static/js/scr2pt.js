document.addEventListener("DOMContentLoaded", function () {
  const downloadBtn = document.getElementById("downloadBtn");
  const format = document.getElementById("formatSelect");
  const resolutionSection = document.getElementById("resolution-section");
  const bitrateSection = document.getElementById("bitrate-section");

  format.addEventListener("change", function () {
    if (format.value == "mp3") {
      resolutionSection.style.display = "none";
      bitrateSection.style.display = "block";
    } else {
      resolutionSection.style.display = "block";
      bitrateSection.style.display = "none";
    }
  });

  downloadBtn.addEventListener("click", function () {
    const url = document.getElementById("videoUrlInput").value;
    downloadUrl(url);
  });

  function downloadUrl(url) {
    const resolution = document.getElementById("resolutionSelect").value;
    const bitrate = document.getElementById("bitrateSelect").value;

    const formData = new FormData();

    formData.append("url", url);
    formData.append("format", format.value);
    if ((format.value = "mp4")) {
      formData.append("resolution", resolution);
    } else {
      formData.append("bitrate", bitrate);
    }
    fetch('/yt_download', {
        method: 'POST',
        body:formData,
        headers:
        {
            Accept: 'application/json',
            "X-Requested-With": "XMLHttpRequest",
        },
    })
    .then((response) => response.json())
    .then((data) => {

    })
    .catch((error) => {
        console.error("Error: ", error)
    })
  }
});
