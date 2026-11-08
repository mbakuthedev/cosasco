(function () {
  var r = document.body.getAttribute("data-root") || "";
  document.write(
    '<footer class="footer"><div class="wrap footer-grid">' +
      '<div>' +
        '<p>11841 Smith Avenue<br>Santa Fe Springs, CA 90670 USA</p>' +
        '<p>Toll Free +1-800-635-6898<br>Phone: +1-562-949-0123<br>Fax: +1-562-949-3065</p>' +
        '<p>Worldwide: Los Angeles / Houston / Aberdeen / Dubai / Kuala Lumpur</p>' +
        '<div class="footer-brand">' +
          '<a href="https://www.halma.com/" target="_blank" rel="noreferrer"><img src="' + r + 'assets/logo-halma.svg" alt="Halma"></a>' +
          '<a href="https://www.ampp.org/" target="_blank" rel="noreferrer"><img class="ampp" src="' + r + 'assets/ampp.png" alt="Member of AMPP"></a>' +
        '</div>' +
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
        '<a href="' + r + 'leadership.html">Leadership</a>' +
        '<a href="' + r + 'careers.html">Careers</a>' +
        '<a href="' + r + 'contact.html">Contact</a>' +
        '<a href="' + r + 'find-a-rep.html">Find a Rep</a>' +
      '</div>' +
      '<div><h4>Resources</h4>' +
        '<a href="' + r + 'products.html">Products</a>' +
        '<a href="' + r + 'services.html">Services</a>' +
        '<a href="' + r + 'innovation.html">Innovation</a>' +
        '<a href="' + r + 'library.html">Technical Library</a>' +
        '<a href="' + r + 'blog.html">Blog</a>' +
        '<a href="' + r + 'faq.html">FAQ</a>' +
        '<a href="' + r + 'quote.html">Online Quote</a>' +
      '</div>' +
    '</div><div class="wrap legal">Copyright © 2026 Cosasco / <a href="' + r + 'privacy.html">Privacy Policy</a></div></footer>'
  );
})();
