(function () {
  var r = document.body.getAttribute("data-root") || "";
  var page = document.body.getAttribute("data-page") || "";
  var industryPages = ["upstream", "midstream", "downstream", "gas", "pulp", "specialty"];
  var companyPages = ["about"];
  var resourcePages = ["library", "blog", "article", "faq", "offline", "key", "calc", "legacy", "partner"];

  function on(name) { return page === name ? " is-active" : ""; }
  function group(list) { return list.indexOf(page) >= 0 ? " is-active" : ""; }

  document.write(
    '<div class="util"><div class="wrap util-inner">' +
      '<a class="util-link" href="' + r + 'contact.html">Contact</a>' +
    '</div></div>' +
    '<header class="site-header" id="site-header"><div class="wrap header-inner">' +
      '<a class="logo" href="' + r + 'index.html" aria-label="Cosasco home"><img src="' + r + 'assets/logo.svg" alt="Cosasco"></a>' +
      '<button class="menu-toggle" id="menu-toggle" aria-label="menu" aria-expanded="false"><span></span><span></span><span></span></button>' +
      '<nav class="nav" id="site-nav">' +
        '<div class="dropdown">' +
          '<button class="drop-toggle' + group(industryPages) + '" type="button">Industries <i class="chev"></i></button>' +
          '<div class="dropdown-panel">' +
            '<a href="' + r + 'industry/upstream.html">Upstream</a>' +
            '<a href="' + r + 'industry/midstream.html">Midstream</a>' +
            '<a href="' + r + 'industry/downstream.html">Downstream</a>' +
            '<a href="' + r + 'industry/gas-transmission.html">Gas Transmission</a>' +
            '<a href="' + r + 'industry/pulp-paper.html">Pulp &amp; Paper</a>' +
            '<a href="' + r + 'industry/specialty-applications.html">Specialty Applications</a>' +
          '</div></div>' +
        '<a class="nav-link' + on("products") + '" href="' + r + 'products.html">Products</a>' +
        '<a class="nav-link' + on("services") + '" href="' + r + 'services.html">Services</a>' +
        '<a class="nav-link' + on("innovation") + '" href="' + r + 'innovation.html">Innovation</a>' +
        '<div class="dropdown">' +
          '<button class="drop-toggle' + group(companyPages) + '" type="button">Company <i class="chev"></i></button>' +
          '<div class="dropdown-panel">' +
            '<a href="' + r + 'about.html">About Cosasco</a>' +
            '<a href="' + r + 'contact.html">Contact</a>' +
          '</div></div>' +
        '<div class="dropdown">' +
          '<button class="drop-toggle' + group(resourcePages) + '" type="button">Resources <i class="chev"></i></button>' +
          '<div class="dropdown-panel">' +
            '<a href="' + r + 'library.html">Technical Library</a>' +
            '<a href="' + r + 'blog.html">Blog</a>' +
            '<a href="' + r + 'software-offline.html">Software</a>' +
            '<a class="sub" href="' + r + 'software-offline.html">Data Offline Software</a>' +
            '<a class="sub" href="' + r + 'software-key.html">Data Key Activation</a>' +
            '<a class="sub" href="' + r + 'software-calculator.html">Device Length Calculator</a>' +
            '<a class="sub" href="' + r + 'software-legacy.html">Legacy Software</a>' +
            '<a href="' + r + 'faq.html">FAQ</a>' +
            '<a href="' + r + 'partner.html">Partner Payment</a>' +
          '</div></div>' +
      '</nav>' +
      '<button class="search-btn" id="search-open" aria-label="Search">' +
        '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>' +
      '</button>' +
    '</div></header>' +
    '<div class="search-modal" id="search-modal"><div class="search-panel" role="dialog" aria-label="Search">' +
      '<input id="search-input" type="search" placeholder="Search products, industries, and pages">' +
      '<div class="search-results" id="search-results"></div>' +
    '</div></div>'
  );
})();
