document.addEventListener("DOMContentLoaded", function () {
  const downloadBtn = document.getElementById("downloadBtn");
  const format = document.getElementById("formatSelect");
  const formatSection = document.getElementById("format-section");
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
    const url = document.getElementById("videoUrlInput");
    downloadUrl(url.value);
  });

  function downloadUrl(url) {
    const resolution = document.getElementById("resolutionSelect").value;
    const bitrate = document.getElementById("bitrateSelect").value;

    downloadBtn.style.display = "none";
    formatSection.style.display = "none";
    resolutionSection.style.display = "none";
    bitrateSection.style.display = "none";

    const loader = document.getElementById("loader");
    loader.style.display = "block";

    const processing = document.getElementById("processing");
    processing.innerHTML = "processing....";

    const formData = new FormData();

    formData.append("url", url);
    formData.append("format", format.value);
    if ((format.value = "mp4")) {
      formData.append("resolution", resolution);
    } else {
      formData.append("bitrate", bitrate);
    }
    fetch("/yt_download", {
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
        const convertedURL = "/downloads/" + convertedFilename;

        downloadBtn.style.display = "inline";
        loader.style.display = "none";
        processing.innerHTML = "";

        // Create a link element to initiate the download
        const link = document.createElement("a");
        link.style.display = "none";
        link.href = convertedURL;
        link.download = convertedFilename;

        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);

        formatSection.style.display = "block";
        if (format.value == "mp3") {
          bitrateSection.style.display = "block";
        } else {
          resolutionSection.style.display = "block";
        }

        downloadFile();
      })
      .catch((error) => {
        console.error("Error: ", error);
      });

    function downloadFile() {
      const convertedFilename = downloadBtn.getAttribute("filename");
      const convertedURL = downloadBtn.getAttribute("url");
      console.log(convertedFilename)
      console.log(convertedURL);

      const a = document.createElement("a");
      a.style.display = "none";
      a.href = convertedURL;
      a.download = convertedFilename;

      document.body.appendChild(a);
      a.click();

      document.body.removeChild(a);
    }
  }
});
