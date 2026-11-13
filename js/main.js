(function () {
  var root = document.body.getAttribute("data-root") || "";

  var header = document.getElementById("site-header");
  function onScroll() {
    if (header) header.classList.toggle("is-solid", window.scrollY > 12);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  var toggle = document.getElementById("menu-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  document.querySelectorAll(".drop-toggle").forEach(function (btn) {
    btn.addEventListener("click", function (event) {
      if (window.innerWidth > 980) return;
      event.preventDefault();
      btn.parentElement.classList.toggle("open");
    });
  });

  var modal = document.getElementById("search-modal");
  var searchOpen = document.getElementById("search-open");
  var searchInput = document.getElementById("search-input");
  var searchResults = document.getElementById("search-results");
  function closeSearch() { if (modal) modal.classList.remove("open"); }
  if (searchOpen && modal) {
    searchOpen.addEventListener("click", function () {
      modal.classList.add("open");
      searchInput.value = "";
      renderSearch("");
      searchInput.focus();
    });
    modal.addEventListener("click", function (event) {
      if (event.target === modal) closeSearch();
    });
    searchInput.addEventListener("input", function () { renderSearch(searchInput.value); });
  }
  function renderSearch(query) {
    if (!searchResults) return;
    var q = query.trim().toLowerCase();
    var pages = window.PAGES || [];
    var products = window.PRODUCTS || [];
    var hits = [];
    pages.forEach(function (page) {
      if (!q || (page.title + " " + page.text).toLowerCase().indexOf(q) >= 0) {
        hits.push({ title: page.title, text: page.text, href: root + page.href });
      }
    });
    products.forEach(function (product) {
      if (!q || (product.name + " " + product.blurb + " " + product.cat).toLowerCase().indexOf(q) >= 0) {
        hits.push({ title: product.name, text: product.cat, href: root + "products.html#" + product.id });
      }
    });
    searchResults.innerHTML = hits.slice(0, 12).map(function (hit) {
      return '<a href="' + hit.href + '"><strong>' + hit.title + '</strong><span>' + hit.text + '</span></a>';
    }).join("") || '<p class="empty">No matches.</p>';
  }
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      closeSearch();
      var detail = document.getElementById("product-detail");
      if (detail) detail.classList.remove("open");
    }
  });

  document.querySelectorAll(".js-country").forEach(function (select) {
    var current = select.getAttribute("data-placeholder") || "Where are you located?*";
    select.innerHTML = '<option value="">' + current + '</option>' +
      (window.COUNTRIES || []).map(function (country) {
        return '<option>' + country + '</option>';
      }).join("");
  });

  document.querySelectorAll("form.js-form").forEach(function (form) {
    var button = form.querySelector("button[type=submit]");
    function refresh() {
      var ok = true;
      form.querySelectorAll("[required]").forEach(function (field) {
        if (!field.value.trim()) ok = false;
      });
      if (button) button.disabled = !ok;
    }
    form.addEventListener("input", refresh);
    refresh();
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var success = form.parentElement.querySelector(".success");
      form.hidden = true;
      if (success) success.hidden = false;
    });
  });

  var params = new URLSearchParams(window.location.search);
  var topic = params.get("topic");
  var help = document.querySelector("[name=help]");
  if (topic && help && !help.value) {
    help.value = "I'd like to talk about " + topic.replace(/-/g, " ") + ".";
    help.dispatchEvent(new Event("input", { bubbles: true }));
  }

  var grid = document.getElementById("product-grid");
  var filterBar = document.getElementById("product-filters");
  var detail = document.getElementById("product-detail");
  if (grid && window.PRODUCTS) {
    var cats = ["All"].concat(window.PRODUCTS.reduce(function (list, product) {
      if (list.indexOf(product.cat) < 0) list.push(product.cat);
      return list;
    }, []));
    var active = "All";
    function drawProducts() {
      grid.innerHTML = window.PRODUCTS.filter(function (product) {
        return active === "All" || product.cat === active;
      }).map(function (product) {
        return '<article class="product-card" id="' + product.id + '">' +
          '<div class="cat-label">' + product.cat + '</div>' +
          '<h3>' + product.name + '</h3>' +
          '<p>' + product.blurb + '</p>' +
          '<div class="row">' +
            '<button class="btn" type="button" data-open="' + product.id + '">Details</button>' +
            '<a class="btn solid" href="' + root + 'contact.html?topic=' + encodeURIComponent(product.name) + '">Enquire</a>' +
          '</div></article>';
      }).join("");
    }
    if (filterBar) {
      filterBar.innerHTML = cats.map(function (cat) {
        return '<button class="chip' + (cat === "All" ? " is-on" : "") + '" type="button" data-cat="' + cat + '">' + cat + '</button>';
      }).join("");
      filterBar.addEventListener("click", function (event) {
        var chip = event.target.closest("[data-cat]");
        if (!chip) return;
        active = chip.getAttribute("data-cat");
        filterBar.querySelectorAll(".chip").forEach(function (el) { el.classList.toggle("is-on", el === chip); });
        drawProducts();
      });
    }
    drawProducts();
    grid.addEventListener("click", function (event) {
      var open = event.target.closest("[data-open]");
      if (open) openDetail(open.getAttribute("data-open"));
    });
    if (location.hash) {
      var hashed = location.hash.slice(1);
      if (window.PRODUCTS.some(function (product) { return product.id === hashed; })) openDetail(hashed);
    }
  }

  function openDetail(id) {
    var product = window.PRODUCTS.filter(function (item) { return item.id === id; })[0];
    if (!product || !detail) return;
    detail.innerHTML =
      '<button class="close-x" type="button" data-close aria-label="Close">×</button>' +
      '<div class="cat-label">' + product.cat + '</div>' +
      '<h2>' + product.name + '</h2>' +
      '<p>' + product.blurb + '</p>' +
      '<p>The Pretoria team can confirm materials, pressure class, and mounting style for this device.</p>' +
      '<a class="btn solid" href="' + root + 'contact.html?topic=' + encodeURIComponent(product.name) + '">Enquire</a>';
    detail.classList.add("open");
    history.replaceState(null, "", "#" + product.id);
  }
  if (detail) {
    detail.addEventListener("click", function (event) {
      if (event.target.closest("[data-close]")) detail.classList.remove("open");
    });
  }

  var calc = document.getElementById("calc-form");
  if (calc) {
    calc.addEventListener("submit", function (event) {
      event.preventDefault();
      var od = parseFloat(calc.od.value);
      var wall = parseFloat(calc.wall.value);
      var stand = parseFloat(calc.stand.value);
      var out = document.getElementById("calc-result");
      if (![od, wall, stand].every(function (n) { return n > 0; }) || wall >= od / 2) {
        out.innerHTML = "<p>Enter an outside diameter, a wall thickness smaller than the inside radius, and a fitting stand-off.</p>";
        return;
      }
      var length = od / 2 - wall + stand;
      out.innerHTML = '<p>Estimated insertion length</p><strong>' + length.toFixed(2) + ' in</strong><p>This is a planning sketch only. Confirm device length with the Pretoria office before ordering.</p>';
    });
  }
})();
