(function () {
  "use strict";

  var storageKey = "cpen221-typeface";
  var choices = ["plex", "google-sans"];
  var selected = "plex";

  try {
    var saved = window.localStorage.getItem(storageKey);
    if (choices.indexOf(saved) !== -1) {
      selected = saved;
    }
  } catch (error) {
    // Storage may be unavailable in a private or restricted browsing context.
  }

  document.documentElement.setAttribute("data-typeface", selected);

  document.addEventListener("DOMContentLoaded", function () {
    var pickers = document.querySelectorAll("[data-typeface-picker]");

    function choose(value) {
      if (choices.indexOf(value) === -1) {
        return;
      }

      document.documentElement.setAttribute("data-typeface", value);
      for (var index = 0; index < pickers.length; index += 1) {
        pickers[index].value = value;
      }

      try {
        window.localStorage.setItem(storageKey, value);
      } catch (error) {
        // The selection still applies to this page when storage is unavailable.
      }
    }

    for (var index = 0; index < pickers.length; index += 1) {
      pickers[index].value = selected;
      pickers[index].addEventListener("change", function (event) {
        choose(event.target.value);
      });
    }
  });
}());
