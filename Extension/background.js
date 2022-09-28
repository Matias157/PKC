var notificationID = null;
var url = null;

chrome.webRequest.onErrorOccurred.addListener(
  function (details) {
    console.log(details);
    if (details.error == "net::ERR_CERT_AUTHORITY_INVALID") {
      url = details.url;
      if (url.includes("https://")) {
        url = url.split("https://");
        url = url[1];
      }
      if (url.includes("www.")) {
        url = url.split("www.");
        url = url[1];
      }
      if (url.includes("/")) {
        url = url.split("/");
        url = url[0];
      }
      chrome.notifications.create(
        "",
        {
          type: "basic",
          iconUrl: "assets/ext-icon.png",
          title: "Public Key Chain",
          message: "Would you like to search " + details.url + " on PKC?",
          buttons: [
            {
              title: "Yes",
              iconUrl: "assets/ext-icon.png",
            },
            {
              title: "No",
              iconUrl: "assets/ext-icon.png",
            },
          ],
          priority: 2,
        },
        function (id) {
          notificationID = id;
        }
      );
    }
  },
  { urls: ["<all_urls>"] }
);

chrome.notifications.onButtonClicked.addListener(function (notifId, btnIdx) {
  if (notifId === notificationID) {
    if (btnIdx === 0) {
      createPKC();
    }
  }
});

function createPKC() {
  postData("http://localhost:5000/create", { url: url }).then((data) => {
    console.log(data);
  });
}

async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
    body: JSON.stringify(data),
  });
  return response;
}
