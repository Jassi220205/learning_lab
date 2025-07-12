const input = document.getElementById("urlInput");
const addBtn = document.getElementById("addBtn");
const urlList = document.getElementById("urlList");

function loadUrls() {
  chrome.storage.sync.get(["requiredUrls"], (data) => {
    const urls = data.requiredUrls || [];
    urlList.innerHTML = "";
    urls.forEach((url, index) => {
      const li = document.createElement("li");
      li.textContent = url;
      const removeBtn = document.createElement("button");
      removeBtn.textContent = "Remove";
      removeBtn.style.marginLeft = "10px";
      removeBtn.onclick = () => removeUrl(index);
      li.appendChild(removeBtn);
      urlList.appendChild(li);
    });
  });
}

function addUrl() {
  const newUrl = input.value.trim();
  if (!newUrl) return;
  chrome.storage.sync.get(["requiredUrls"], (data) => {
    const urls = data.requiredUrls || [];
    urls.push(newUrl);
    chrome.storage.sync.set({ requiredUrls: urls }, () => {
      input.value = "";
      loadUrls();
    });
  });
}

function removeUrl(index) {
  chrome.storage.sync.get(["requiredUrls"], (data) => {
    const urls = data.requiredUrls || [];
    urls.splice(index, 1);
    chrome.storage.sync.set({ requiredUrls: urls }, loadUrls);
  });
}

addBtn.addEventListener("click", addUrl);
document.addEventListener("DOMContentLoaded", loadUrls);
