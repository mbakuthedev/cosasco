(function () {
  var r = document.body.getAttribute("data-root") || "";
  document.write(
    '<footer class="footer"><div class="wrap footer-grid">' +
      '<div>' +
        '<p>Office 7, Second Floor<br>Silverleaf Business Centre<br>118 Duncan Street<br>Hatfield, Pretoria, 0083<br>Gauteng, South Africa</p>' +
        '<p>Phone: <a href="tel:+27120004521">+27 12 000 4521</a><br>' +
        'Mobile: <a href="tel:+27820007314">+27 82 000 7314</a></p>' +
        '<p>Email: <a href="mailto:sales.rsa@cosasco.co.za">sales.rsa@cosasco.co.za</a></p>' +
      '</div>' +
      '<div><h4>Industries</h4>' +
        '<a href="' + r + 'industry/upstream.html">Upstream</a>' +
        '<a href="' + r + 'industry/midstream.html">Midstream</a>' +
        '<a href="' + r + 'industry/downstream.html">Downstream</a>' +
        '<a href="' + r + 'industry/gas-transmission.html">Gas Transmission</a>' +
        '<a href="' + r + 'industry/pulp-paper.html">Pulp &amp; Paper</a>' +
        '<a href="' + r + 'industry/specialty-applications.html">Specialty Applications</a>' +
      '</div>' +
      '<div><h4>Company</h4>' +
        '<a href="' + r + 'about.html">About Cosasco</a>' +
        '<a href="' + r + 'contact.html">Contact</a>' +
      '</div>' +
      '<div><h4>Resources</h4>' +
        '<a href="' + r + 'products.html">Products</a>' +
        '<a href="' + r + 'services.html">Services</a>' +
        '<a href="' + r + 'innovation.html">Innovation</a>' +
        '<a href="' + r + 'library.html">Technical Library</a>' +
        '<a href="' + r + 'blog.html">Blog</a>' +
        '<a href="' + r + 'faq.html">FAQ</a>' +
      '</div>' +
    '</div><div class="wrap legal">Copyright © 2026 Cosasco / <a href="' + r + 'privacy.html">Privacy Policy</a></div></footer>'
  );
})();
