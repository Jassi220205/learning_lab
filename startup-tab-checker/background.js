chrome.runtime.onStartup.addListener(() => {
  chrome.storage.sync.get(["requiredUrls"], (data) => {
    const requiredUrls = data.requiredUrls || [];

    chrome.tabs.query({}, (tabs) => {
      const openUrls = tabs.map(tab => tab.url);
      requiredUrls.forEach(url => {
        if (!openUrls.some(openUrl => openUrl.includes(url))) {
          chrome.tabs.create({ url: url });
        }
      });
    });
  });
});
