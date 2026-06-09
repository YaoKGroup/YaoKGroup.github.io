(function () {
  function normalizeTitle(title) {
    return (title || "")
      .normalize("NFKD")
      .replace(/[\u2010-\u2015\u2212]/g, "-")
      .replace(/&/g, "and")
      .replace(/\(\s*news\s+and\s+views\s*\)/gi, " ")
      .replace(/[^a-zA-Z0-9]+/g, " ")
      .toLowerCase()
      .trim()
      .replace(/\s+/g, " ");
  }

  function updatedDate(data) {
    if (!data.updated_at) return "";
    var date = new Date(data.updated_at);
    if (Number.isNaN(date.getTime())) return "";
    return date.toISOString().slice(0, 10);
  }

  function makeBadge(record, dateText) {
    var badge = document.createElement(record && record.scholar_url ? "a" : "span");
    badge.className = "scholar-citation-badge";
    if (record && record.scholar_url) {
      badge.href = record.scholar_url;
      badge.target = "_blank";
      badge.rel = "noopener";
    }

    if (record && Number.isFinite(record.citations)) {
      var suffix = record.citations === 1 ? "citation" : "citations";
      badge.textContent = "Google Scholar: " + record.citations + " " + suffix;
      badge.title = dateText ? "Updated " + dateText : "Google Scholar citations";
    } else {
      badge.textContent = "Google Scholar: --";
      badge.title = dateText
        ? "No Google Scholar match in the " + dateText + " update"
        : "No Google Scholar match";
      badge.classList.add("is-missing");
    }
    return badge;
  }

  function addBadges(data) {
    var dateText = updatedDate(data);
    var records = data.site_citations_by_title || {};
    document.querySelectorAll(".pub-list li").forEach(function (item) {
      var title = item.querySelector(".pub-title");
      if (!title || item.querySelector(".scholar-citation-badge")) return;

      var record = records[normalizeTitle(title.textContent)];
      var badge = makeBadge(record, dateText);
      var imageBlock = item.querySelector(".pub-images");
      item.insertBefore(badge, imageBlock || null);
    });
  }

  var dataUrl = "/assets/data/scholar_citations.json";
  fetch(dataUrl + "?t=" + Date.now(), { cache: "no-store" })
    .then(function (response) {
      if (!response.ok) throw new Error("Citation data request failed.");
      return response.json();
    })
    .then(addBadges)
    .catch(function () {
      document.documentElement.classList.add("scholar-citations-unavailable");
    });
}());
