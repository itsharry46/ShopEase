function commonGetCSRFToken() {
  let cookies = document.cookie.split(";");
  for (let i = 0; i < cookies.length; i++) {
    let cookie = cookies[i].trim();
    if (cookie.startsWith("csrftoken=")) {
      return cookie.substring("csrftoken=".length, cookie.length);
    }
  }
  return null;
}

function commonDownloadFile(file_url) {
  const a = document.createElement("a");
  a.href = file_url;
  a.download = file_url.split("/").pop();
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}
