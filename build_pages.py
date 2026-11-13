from pathlib import Path

ROOT = Path(__file__).parent

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Mukta+Mahee:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{root}css/styles.css">
</head>
<body data-root="{root}" data-page="{page}">
<script src="{root}js/shell.js"></script>
"""

TAIL = """
<script src="{root}js/footer.js"></script>
<script src="{root}js/data.js"></script>
<script src="{root}js/main.js"></script>
</body>
</html>
"""

def write(rel, title, page, root, body, hero=None):
    hero_html = ""
    if hero:
        image, heading, lede = hero
        hero_html = f"""
<section class="page-hero" style="--hero: url('../{image}')">
  <div class="wrap">
    <h1>{heading}</h1>
    <p class="lede">{lede}</p>
  </div>
</section>
"""
    html = HEAD.format(title=title, root=root, page=page) + hero_html + body + TAIL.format(root=root)
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print(rel)

write("products.html", "Products - Cosasco", "products", "", """
<section class="page">
  <div class="wrap">
    <div class="filters" id="product-filters"></div>
    <div class="product-grid" id="product-grid"></div>
  </div>
</section>
<aside class="detail" id="product-detail" aria-label="Product details"></aside>
""", ("assets/facility.jpg", "All Products", "Dependable, accurate corrosion monitoring products and systems."))

write("services.html", "Services - Cosasco", "services", "", """
<section class="page">
  <div class="wrap prose">
    <p>Cosasco is the only company with the experience, reputation, and global reach able to support all your corrosion monitoring requirements. Whether you are establishing a new corrosion management program, maintaining existing assets, or looking for solutions, Cosasco is your trusted partner. Experienced in-house experts across the globe are ready to respond.</p>
  </div>
  <div class="quote-band solo" style="margin-top:36px">
    <div class="bar"></div>
    <blockquote>
      <p>“Cosasco is capable of providing the full package of both product supply and service with a history of quality and reliability. That is why we use Cosasco.”</p>
      <cite>— Cosasco Customer, Corrosion Engineer, Supermajor</cite>
    </blockquote>
  </div>
  <div class="wrap" style="padding-top:56px">
    <h2>The Cosasco Commitment</h2>
    <p style="max-width:760px">Since 1950, Cosasco has developed corrosion monitoring solutions that help customers decide how to care for critical infrastructure. Matching that commitment is a field team located around the world, trained on safety, and focused on the life of the equipment after commissioning.</p>
    <h2 style="margin-top:36px">Our Services Include</h2>
    <div class="app-grid">
      <article class="app-card"><h3>Corrosion Program Development</h3><p>Support for new programs and existing assets, drawing on more than 70 years of corrosion monitoring experience.</p></article>
      <article class="app-card"><h3>Design &amp; Documentation</h3><p>Probe placement and device selection worked out with EPCs, design engineers, and corrosion engineers.</p></article>
      <article class="app-card"><h3>Installation</h3><p>Factory-trained crews install and configure monitoring and chemical injection systems so the data is usable from day one.</p></article>
      <article class="app-card"><h3>Service &amp; Maintenance</h3><p>Routine service for the life of the installation, performed by technicians who stay with the site.</p></article>
    </div>
    <p style="margin-top:28px"><a class="btn solid" href="contact.html?topic=services">Talk with the services team</a></p>
  </div>
</section>
""", ("assets/hero-company.jpg", "Corrosion Monitoring Services", "Supply and service, from the first placement study through the life of the equipment."))

write("innovation.html", "Innovation - Cosasco", "innovation", "", """
<section class="page">
  <div class="wrap">
    <p class="lede" style="color:var(--ink);margin-bottom:28px">Our latest technologies, available today.</p>
    <div class="app-grid">
      <article class="app-card"><h3>Echo Point</h3><p>Certified for the most hazardous environments. Three transducer choices with up to 3x sensitivity, thru-coating measurements, or ultra-high temperature at 932°F (500°C).</p></article>
      <article class="app-card"><h3>Microcor</h3><p>High-sensitivity intrusive probe with the fastest response time in the industry.</p></article>
      <article class="app-card"><h3>Decommissioning Plug</h3><p>Lets service teams isolate and lock out unserviceable or unnecessary access points without a shutdown.</p></article>
      <article class="app-card"><h3>SafeGuard Service Valve</h3><p>Double isolation valve technology that acts as an airlock against hazardous materials, built to the highest safety standards Cosasco offers.</p></article>
    </div>
    <div class="prose" style="margin-top:48px">
      <h2>Innovation is core to who we are.</h2>
      <p>New ideas start with real-world problems. If you have a corrosion problem and wish there were a solution, tell us.</p>
      <h2>Because we’re closer to customers, we’re making what the industry needs most</h2>
      <p>Local teams are the advantage. They learn what is needed and how it should work when it is built.</p>
      <h2>We are focused on the future</h2>
      <p>Economic, safety, and environmental stakes keep rising. The work is aimed at the solutions that change those outcomes.</p>
    </div>
    <div class="value-grid" style="margin-top:20px">
      <article class="value-card"><h3>Design great user experiences</h3><p>Data that’s difficult to interpret is difficult to trust. Ease-of-use is part of making a confident decision.</p></article>
      <article class="value-card"><h3>Enable the quickest decision making</h3><p>Acting at the right time takes real-time access to the right data, including integration into the systems operators already run.</p></article>
      <article class="value-card"><h3>Deliver results you can trust</h3><p>The consequences of corrosion are significant. Accuracy and reliability are what make a measurement useful.</p></article>
      <article class="value-card"><h3>Find and solve the most complex problems</h3><p>Local experts are on the front lines of the challenges that matter. New devices start there.</p></article>
    </div>
  </div>
</section>
<section class="quote-band solo">
  <div class="bar"></div>
  <blockquote>
    <p>“There is a difference in terms of the user friendliness of the equipment… Cosasco has user friendly software.”</p>
    <cite>— Cosasco Customer, Corrosion Engineer, Supermajor</cite>
  </blockquote>
</section>
""", ("assets/hero-home.jpg", "Innovation", "Technologies shaped by the problems operators actually have."))

write("about.html", "About - Cosasco", "about", "", """
<section class="page">
  <div class="wrap">
    <p style="max-width:800px;font-size:20px">Cosasco has been exclusively dedicated to corrosion management for over 70 years. The history is a record of product and service solutions, and a commitment to keep advancing the field through innovation and expertise.</p>
    <div class="value-grid" style="margin-top:28px">
      <article class="value-card"><h3>Our Vision</h3><p>Protect people and the environment from the impacts of corrosion.</p></article>
      <article class="value-card"><h3>Our Mission</h3><p>Innovate corrosion management solutions to improve production and increase safety for people and our environment.</p></article>
    </div>
    <h2>The Cosasco Difference</h2>
    <ul class="checks">
      <li>The entire suite of precise, proven corrosion management products</li>
      <li>Comprehensive beginning-to-end support from a global team of experts</li>
      <li>A 70 year history as pioneers of innovation in corrosion management</li>
    </ul>
    <h2>Our Values</h2>
    <div class="value-grid">
      <article class="value-card"><h3>We Serve</h3><p>Customers, team members, communities, and the environment are at the center of every decision.</p></article>
      <article class="value-card"><h3>We Do the Right Thing</h3><p>Integrity comes first. Difficult decisions are handled with honesty and fairness.</p></article>
      <article class="value-card"><h3>We Value Each Other</h3><p>The team comes before the individual, with room for different perspectives.</p></article>
      <article class="value-card"><h3>We Strive for Excellence</h3><p>Obstacles get worked, solutions stay bold, and results come from continuous improvement.</p></article>
    </div>
    <p style="margin-top:28px"><a class="text-link" href="industry/upstream.html">Discover the value for your industry →</a></p>
  </div>
</section>
""", ("assets/hero-company.jpg", "About Us", "Exclusively dedicated to corrosion management for over 70 years."))

write("contact.html", "Contact - Cosasco", "contact", "", """
<section class="page">
  <div class="wrap">
    <div class="calc">
      <div>
        <p>Cosasco is exclusively dedicated to corrosion monitoring from beginning to end, providing the information you need to make the best possible decisions.</p>
        <p><strong>Office 7, Second Floor</strong><br>Silverleaf Business Centre<br>118 Duncan Street<br>Hatfield, Pretoria, 0083<br>Gauteng, South Africa</p>
        <p>Phone: <a href="tel:+27120004521">+27 12 000 4521</a><br>Mobile: <a href="tel:+27820007314">+27 82 000 7314</a></p>
        <p>Email: <a href="mailto:sales.rsa@cosasco.co.za">sales.rsa@cosasco.co.za</a></p>
      </div>
      <div>
        <div class="success" hidden>
          <h3>Thank you for contacting Cosasco.</h3>
          <p>Your note was not emailed or sent anywhere. Form delivery is switched off for now.</p>
        </div>
        <form class="js-form" onsubmit="return false;">
          <label class="field"><span>Name*</span><input name="name" required placeholder="Name*"></label>
          <label class="field" style="margin-top:12px"><span>Email*</span><input type="email" required placeholder="Email*"></label>
          <label class="field" style="margin-top:12px"><span>Company Name*</span><input required placeholder="Company Name*"></label>
          <label class="field" style="margin-top:12px"><span>Phone*</span><input type="tel" required placeholder="Phone*"></label>
          <label class="field" style="margin-top:12px"><span>Where are you located?*</span><select class="js-country" required></select></label>
          <label class="field" style="margin-top:12px"><span>How can we help?*</span><textarea name="help" required placeholder="How can we help?*"></textarea></label>
          <div class="form-actions"><button class="btn solid" type="submit" disabled>Submit</button></div>
        </form>
      </div>
    </div>
  </div>
</section>
""", ("assets/hero-home.jpg", "Contact Us", "Tell us what you need measured, and where."))

write("faq.html", "FAQ - Cosasco", "faq", "", """
<section class="page">
  <div class="wrap faq">
    <details open><summary>What type of credit cards do you accept for payment?</summary><p>Visa, Mastercard, and American Express. For other forms of payment, contact the Pretoria office at <a href="tel:+27120004521">+27 12 000 4521</a> or <a href="mailto:sales.rsa@cosasco.co.za">sales.rsa@cosasco.co.za</a>.</p></details>
    <details><summary>How can I place an order?</summary><p>Email <a href="mailto:sales.rsa@cosasco.co.za">sales.rsa@cosasco.co.za</a> or call <a href="tel:+27120004521">+27 12 000 4521</a> / <a href="tel:+27820007314">+27 82 000 7314</a>. You can also use the <a href="contact.html">contact form</a>.</p></details>
    <details><summary>How can I check on the status of my order?</summary><p>Contact the Pretoria office at <a href="tel:+27120004521">+27 12 000 4521</a> or <a href="mailto:sales.rsa@cosasco.co.za">sales.rsa@cosasco.co.za</a>.</p></details>
    <details><summary>To whom should I send my quote request?</summary><p>Send quote requests to <a href="mailto:sales.rsa@cosasco.co.za">sales.rsa@cosasco.co.za</a> or use the <a href="contact.html">contact page</a>.</p></details>
    <details><summary>I could not find a particular probe or instrument. Who can help?</summary><p>Contact the Pretoria office and the team can talk through product options that are not listed in the catalog.</p></details>
    <details><summary>Do I have to uninstall the previous version of software before I install the new version?</summary><p>Yes.</p></details>
    <details><summary>How can I set up an account?</summary><p>Contact the Pretoria office at <a href="mailto:sales.rsa@cosasco.co.za">sales.rsa@cosasco.co.za</a>.</p></details>
    <details><summary>How can I get a product manual?</summary><p>Manuals are requested from the <a href="library.html">technical library</a>.</p></details>
    <details><summary>What is the latest version of the Microcor Tools Software?</summary><p>The latest published version of Microcor Tools Software is 4.4.3.</p></details>
    <details><summary>What is the latest version of the CRM Software?</summary><p>The latest published version of the CRM Software is 6.06.005.</p></details>
    <details><summary>How can I get an RMA number?</summary><p>Contact the Pretoria office at <a href="mailto:sales.rsa@cosasco.co.za">sales.rsa@cosasco.co.za</a> or call <a href="tel:+27120004521">+27 12 000 4521</a>.</p></details>
    <details><summary>Is local support available?</summary><p>Yes. Reach the South Africa office in Pretoria via the <a href="contact.html">contact page</a>.</p></details>
    <details><summary>How can I get help configuring an instrument?</summary><p>Contact the Pretoria office at <a href="mailto:sales.rsa@cosasco.co.za">sales.rsa@cosasco.co.za</a> or call <a href="tel:+27120004521">+27 12 000 4521</a> / <a href="tel:+27820007314">+27 82 000 7314</a>.</p></details>
  </div>
</section>
""", ("assets/hero-company.jpg", "FAQ", "Answers to frequently asked questions"))

write("blog.html", "Blog - Cosasco", "blog", "", """
<section class="page">
  <div class="wrap">
    <div class="post-grid">
      <a class="post" href="blog-safeguard.html">
        <img src="assets/facility.jpg" alt="">
        <div>
          <h3>The SafeGuard Service Valve: Cosasco's Latest Innovation</h3>
          <p>SafeGuard features double isolation valve technology to meet the highest safety standards, acting as an airlock against hazardous materials.</p>
        </div>
      </a>
    </div>
  </div>
</section>
""", ("assets/water.jpg", "Blog", "Notes on products, safety, and monitoring practice."))

write("blog-safeguard.html", "SafeGuard Service Valve - Cosasco", "article", "", """
<section class="page">
  <div class="wrap prose">
    <p><a href="blog.html">Blog</a></p>
    <h2>The SafeGuard Service Valve</h2>
    <p>SafeGuard, Cosasco’s latest innovation, features double isolation valve technology to realize the highest safety standards in the world, acting as an airlock against hazardous materials.</p>
    <p>The valve is fire-rated and PED-certified. It is made in NACE-compliant 4130 or duplex stainless steel, and it is the lightest service valve Cosasco offers in this class.</p>
    <p><a class="btn solid" href="products.html#safeguard">View the product</a></p>
  </div>
</section>
""", ("assets/facility.jpg", "The SafeGuard Service Valve", "Cosasco's latest innovation in retrieval safety."))

write("library.html", "Technical Library - Cosasco", "library", "", """
<section class="page">
  <div class="wrap">
    <p>Product manuals and data sheets are issued by Cosasco for specific devices. Request the document you need and the Pretoria office can send the current file.</p>
    <div class="lib-grid" style="margin-top:22px">
      <article class="lib-card"><h3>Access Fittings</h3><p>Installation and maintenance literature for Models 50 through 58 and severe-service assemblies.</p><a class="text-link" href="contact.html?topic=access-fitting-manuals">Request documents →</a></article>
      <article class="lib-card"><h3>ER &amp; Microcor Probes</h3><p>Probe selection, wiring, and retrieval notes for electrical-resistance monitoring.</p><a class="text-link" href="contact.html?topic=er-probe-manuals">Request documents →</a></article>
      <article class="lib-card"><h3>LPR &amp; Water Systems</h3><p>Transmitter and portable instrument guides for aqueous corrosion rate measurement.</p><a class="text-link" href="contact.html?topic=lpr-manuals">Request documents →</a></article>
      <article class="lib-card"><h3>Ultrasonic</h3><p>Echo Point and non-intrusive thickness monitoring literature.</p><a class="text-link" href="contact.html?topic=ultrasonic-manuals">Request documents →</a></article>
      <article class="lib-card"><h3>Chemical Injection</h3><p>Injection and sampling tube assemblies, including retractable hardware.</p><a class="text-link" href="contact.html?topic=injection-manuals">Request documents →</a></article>
      <article class="lib-card"><h3>Software</h3><p>Offline tools, legacy versions, and activation steps.</p><a class="text-link" href="software-offline.html">Open software →</a></article>
    </div>
  </div>
</section>
""", ("assets/hero-company.jpg", "Technical Library", "Manuals, data sheets, and software notes."))

write("privacy.html", "Privacy Policy - Cosasco", "privacy", "", """
<section class="page">
  <div class="wrap prose">
    <p>This website stores consultation form notes in your browser only.</p>
    <h2>Consultation forms</h2>
    <p>The contact and consultation forms do not transmit what you type. After you submit, the page shows a confirmation and keeps the note on this device only.</p>
    <h2>Questions</h2>
    <p>Office 7, Second Floor, Silverleaf Business Centre, 118 Duncan Street, Hatfield, Pretoria, 0083, Gauteng, South Africa.</p>
    <p>Phone <a href="tel:+27120004521">+27 12 000 4521</a> · Mobile <a href="tel:+27820007314">+27 82 000 7314</a> · Email <a href="mailto:sales.rsa@cosasco.co.za">sales.rsa@cosasco.co.za</a>.</p>
  </div>
</section>
""", ("assets/hero-company.jpg", "Privacy Policy", "What this site keeps, and where it stays."))

write("partner.html", "Partner Payment - Cosasco", "partner", "", """
<section class="page">
  <div class="wrap prose">
    <p>Partner invoices are handled by the Pretoria office. This page does not take card payments.</p>
    <p>For payment questions, call <a href="tel:+27120004521">+27 12 000 4521</a> or <a href="tel:+27820007314">+27 82 000 7314</a>, email <a href="mailto:sales.rsa@cosasco.co.za">sales.rsa@cosasco.co.za</a>, or write through the contact form and include your account reference.</p>
    <p>Accepted cards, when card payment is offered, are Visa, Mastercard, and American Express.</p>
    <p><a class="btn solid" href="contact.html?topic=partner-payment">Contact accounts</a></p>
  </div>
</section>
""", ("assets/hero-company.jpg", "Partner Payment", "Reach the office that manages your account."))
write("software-offline.html", "Data Offline Software - Cosasco", "offline", "", """
<section class="page">
  <div class="wrap prose">
    <p>Data Offline Software is how Cosasco customers download and review corrosion data when a live connection to the transmitter is not available. Field crews use it for loggers and locations that are visited on a round, rather than polled continuously.</p>
    <p>Current installers are issued by Cosasco. Request access and the team will confirm which package matches your loggers.</p>
    <p><a class="btn solid" href="contact.html?topic=data-offline-software">Request software</a></p>
  </div>
</section>
""", ("assets/hero-company.jpg", "Data Offline Software", "Review corrosion data when the instrument is not online."))

write("software-key.html", "Data Key Activation - Cosasco", "key", "", """
<section class="page">
  <div class="wrap prose">
    <p>Licensed Cosasco software is activated with a data key tied to the installation. If a key needs to be issued or moved to another machine, Customer Service or Technical Support confirms the license before activating it.</p>
    <p>Have the software name, the version, and the site or purchase reference ready.</p>
    <p><a class="btn solid" href="contact.html?topic=data-key-activation">Request activation</a></p>
  </div>
</section>
""", ("assets/hero-company.jpg", "Data Key Activation", "Turn on a licensed Cosasco software install."))

write("software-calculator.html", "Device Length Calculator - Cosasco", "calc", "", """
<section class="page">
  <div class="wrap">
    <p>Estimate how far a probe needs to reach from the fitting seal face to the monitoring point. This sketch uses outside diameter, wall thickness, and fitting stand-off. It is not a certified Cosasco calculation.</p>
    <div class="calc" style="margin-top:22px">
      <form id="calc-form">
        <label class="field"><span>Pipe outside diameter (in)</span><input name="od" type="number" min="0" step="0.01" value="12"></label>
        <label class="field" style="margin-top:12px"><span>Wall thickness (in)</span><input name="wall" type="number" min="0" step="0.01" value="0.5"></label>
        <label class="field" style="margin-top:12px"><span>Fitting stand-off (in)</span><input name="stand" type="number" min="0" step="0.01" value="5.25"></label>
        <div class="form-actions"><button class="btn solid" type="submit">Calculate</button></div>
      </form>
      <div class="result-box" id="calc-result"><p>Estimated insertion length</p><strong>—</strong><p>Enter the three dimensions and calculate.</p></div>
    </div>
  </div>
</section>
""", ("assets/facility.jpg", "Device Length Calculator", "A planning estimate for probe insertion length."))

write("software-legacy.html", "Legacy Software - Cosasco", "legacy", "", """
<section class="page">
  <div class="wrap prose">
    <p>Older Cosasco instruments still read out through legacy packages. Published versions called out in the FAQ:</p>
    <ul>
      <li>Microcor Tools Software 4.4.3</li>
      <li>CRM Software 6.06.005</li>
    </ul>
    <p>Uninstall the previous version before installing a new one. Microcor Tools and Corrdata Plus have been documented as compatible with Windows Vista Business, Vista Ultimate, and XP Pro. For a current machine, ask Technical Support which build to use.</p>
    <p><a class="btn solid" href="contact.html?topic=legacy-software">Ask about a legacy installer</a></p>
  </div>
</section>
""", ("assets/hero-company.jpg", "Legacy Software", "Microcor Tools, CRM, and Corrdata packages."))

industries = [
    ("industry/upstream.html", "Upstream - Cosasco", "upstream", "assets/upstream.jpg", "Upstream",
     "We understand that upstream environments are often severe, remote, and rapidly changing.",
     """<p>Cosasco’s dependable corrosion management solutions provide upstream engineers with the information they need to make quick, accurate decisions in these high risk scenarios so that they can:</p>
     <ul class="checks">
       <li>Maximize uptime and production with reliable corrosion monitoring devices that won’t fail or require unnecessary shutdowns</li>
       <li>Protect people and assets in remote locations with accurate corrosion monitoring, proven in the world’s most severe environments</li>
       <li>React quickly to changes in the pipes with real-time data from the most stable, fastest responding probe technology in the industry</li>
       <li>Optimize production performance with customized engineering solutions designed specifically for your wells</li>
     </ul>
     <h2>Industry Applications</h2>
     <div class="app-grid">
       <article class="app-card"><h3>Offshore Production Facilities</h3><p>Customized solutions uniquely designed for complex, severe environments.</p></article>
       <article class="app-card"><h3>Downhole Monitoring</h3><p>Improved well performance and material selection for well tubing.</p></article>
       <article class="app-card"><h3>Chemical Optimization</h3><p>Real-time stream monitoring to optimize chemical injections.</p></article>
     </div>"""),
    ("industry/midstream.html", "Midstream - Cosasco", "midstream", "assets/midstream.jpg", "Midstream",
     "Corrosion is a leading cause of pipeline failure—and one of the most difficult to detect.",
     """<p>Cosasco’s efficient, reliable corrosion monitoring and management solutions allow you to balance regulatory requirements, asset performance, asset life and cost in order to:</p>
     <ul class="checks">
       <li>Extend the life of your assets by detecting internal and external corrosion before it causes pipeline damage or failure.</li>
       <li>Meet regulatory and integrity management requirements with real-time monitoring for pipeline, processing, and storage assets.</li>
       <li>Retrieve data easily from remote locations with flexible data transmission and service experts who travel to those sites.</li>
       <li>Monitor corrosion in locations with limited access using high-accuracy ultrasonic technology for non-intrusive monitoring.</li>
     </ul>
     <h2>Industry Applications</h2>
     <div class="app-grid">
       <article class="app-card"><h3>Pipeline Corrosion Monitoring</h3><p>Real-time data to protect pipelines from internal and external threats.</p></article>
       <article class="app-card"><h3>Regulatory Compliance and Best Practices</h3><p>Meet best-practice requirements for safety and regulatory compliance.</p></article>
       <article class="app-card"><h3>Pipeline Integrity and Risk Analysis</h3><p>Reliable monitoring to assess risk and confirm integrity.</p></article>
       <article class="app-card"><h3>Pipeline Defect Monitoring</h3><p>Precise data to watch defect changes over time and decide when to act.</p></article>
     </div>"""),
    ("industry/downstream.html", "Downstream - Cosasco", "downstream", "assets/downstream.jpg", "Downstream",
     "In high-risk downstream environments, containment is critical.",
     """<p>Optimal corrosion management increases profitability and helps avoid unscheduled repairs. Adding real-time corrosion monitoring to asset integrity programs lets engineers decide quickly so that they can:</p>
     <ul class="checks">
       <li>Maximize uptime and production with devices that provide real-time data for critical process decisions</li>
       <li>Protect people and assets with monitoring designed for high-risk environments</li>
       <li>React quickly to changes in the pipes with stable, fast-responding probe technology</li>
       <li>Optimize maintenance spend with automated monitoring that can be trusted</li>
     </ul>
     <h2>Industry Applications</h2>
     <div class="app-grid">
       <article class="app-card"><h3>Chemical Optimization</h3><p>Real-time stream monitoring to optimize chemical injections.</p></article>
       <article class="app-card"><h3>Crude Slate Monitoring</h3><p>Continuous process corrosion-rate monitoring so refinery assets can be protected from highly corrosive crudes.</p></article>
       <article class="app-card"><h3>Continuous Wall-Thickness Monitoring</h3><p>High-accuracy ultrasonic technology for mechanical integrity.</p></article>
       <article class="app-card"><h3>Corrosion &amp; Erosion Monitoring</h3><p>Real-time data to assess risk and prevent a release.</p></article>
     </div>"""),
    ("industry/gas-transmission.html", "Gas Transmission - Cosasco", "gas", "assets/gas.jpg", "Gas Transmission",
     "Internal corrosion is a leading cause of pipeline failure—and one of the most difficult to detect.",
     """<p>Cosasco’s monitoring solutions help balance regulatory requirements, asset performance, and maintenance cost in order to:</p>
     <ul class="checks">
       <li>Monitor asset performance by detecting internal and external material degradation and defects</li>
       <li>Meet regulatory and integrity management requirements, including PHMSA Mega-Rules, with real-time monitoring for pipeline, processing, and storage assets</li>
       <li>Retrieve data from remote locations with flexible transmission and field service</li>
       <li>Monitor locations with limited access using high-accuracy ultrasonic technology</li>
     </ul>
     <h2>Industry Applications</h2>
     <div class="app-grid">
       <article class="app-card"><h3>Pipeline Corrosion Monitoring</h3><p>Real-time data to protect pipelines from internal and external threats.</p></article>
       <article class="app-card"><h3>Regulatory Compliance and Best Practices</h3><p>Meet best-practice requirements for safety and regulatory compliance.</p></article>
       <article class="app-card"><h3>Pipeline Integrity and Risk Analysis</h3><p>Reliable monitoring to assess risk and confirm integrity.</p></article>
       <article class="app-card"><h3>Pipeline Defect Monitoring</h3><p>Precise data to watch defect changes over time and decide when to act.</p></article>
     </div>"""),
    ("industry/pulp-paper.html", "Pulp & Paper - Cosasco", "pulp", "assets/pulp.jpg", "Pulp &amp; Paper",
     "Papermaking releases corrosive contaminants into the air that damage electronics and machinery.",
     """<p>Cosasco measures the direct effect of airborne, internal, and external corrosion in real time. That lets pulp and paper manufacturers:</p>
     <ul class="checks">
       <li>Confirm air filtration systems are working</li>
       <li>Reduce equipment replacement costs through tighter control of atmospheric corrosion</li>
       <li>Cut unplanned maintenance by seeing the corrosion rate at critical assets</li>
       <li>Optimize production by measuring corrosion at each stage of the process</li>
     </ul>
     <h2>Industry Applications</h2>
     <div class="app-grid">
       <article class="app-card"><h3>Airborne Corrosion Monitoring</h3><p>Real-time air quality monitoring with hypersensitive ER technology, before damage shows up.</p></article>
       <article class="app-card"><h3>Continuous Wall-Thickness Monitoring</h3><p>High-accuracy ultrasonic technology for mechanical integrity.</p></article>
     </div>"""),
    ("industry/specialty-applications.html", "Specialty Applications - Cosasco", "specialty", "assets/specialty.jpg", "Specialty Applications",
     "Corrosion management for industrial applications that do not fit a single plant type.",
     """<p>If a standard system does not fit, Cosasco engineers a custom one in order to:</p>
     <ul class="checks">
       <li>Protect people and assets with monitoring designed for high-risk environments</li>
       <li>Maximize uptime with devices that do not force unnecessary shutdowns</li>
       <li>Remove uncertainty with accurate, real-time corrosion data</li>
       <li>Hold a controlled environment with hypersensitive sensors for airborne contaminants</li>
     </ul>
     <h2>Industry Applications</h2>
     <div class="app-grid">
       <article class="app-card"><h3>Wastewater Treatment</h3><p>Support regulatory requirements and strengthen the maintenance program.</p></article>
       <article class="app-card"><h3>Ultrapure Water</h3><p>Measure ultralow rouging rates in stainless steel systems.</p></article>
       <article class="app-card"><h3>Control Rooms &amp; Data Centers</h3><p>Protect sensitive electronics with real-time air quality monitoring that flags a corrosive environment before damage.</p></article>
     </div>"""),
]

for rel, title, page, image, heading, lede, body in industries:
    write(
        rel, title, page, "../",
        f'<section class="page"><div class="wrap prose">{body}<p style="margin-top:28px"><a class="btn solid" href="../contact.html">Talk with an industry specialist</a></p></div></section>',
        (image, heading, lede),
    )

print("done")
