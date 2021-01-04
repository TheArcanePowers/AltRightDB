<!DOCTYPE HTML>
<!--
	Credit
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Charlottesville Rally</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="../assets/css/main.css" />
		<noscript><link rel="stylesheet" href="../assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
						<a href="../index.html" class="logo"><strong>Alt-Right</strong> <span>Database</span></a>
						<nav>
							<a href="#menu">Menu</a>
						</nav>
					</header>

				<!-- Menu -->
					<nav id="menu">
						<ul class="links">
							<li><a href="../index.html">Home</a></li>
							<li><a href="../archive.html">Archive</a></li>
							<li><a href="../info.html">Info</a></li>
							<!--<li><a href="elements.html">Elements</a></li>
							-->
						</ul>
						<ul class="actions stacked">
							<li><a href="#" class="button fit">Submit Videos</a></li>
							<li><a href="#" class="button primary fit">Help Us</a></li>
						</ul>
					</nav>

				<!-- Main -->
					<div id="main" class="alt">

						<!-- One -->
							<section id="one">
								<div class="inner">
									<header class="major">
										<?php
										$strJsonFileContents = file_get_contents("charlottesville/info.json");
										$array = json_decode($strJsonFileContents, true);
										echo "<h1>" . $array[name] . "</h1>";
										?>
									</header>
									<?php
									// Get the contents of the JSON file 
									$strJsonFileContents = file_get_contents("charlottesville/info.json");
									// Convert to array 
									$array = json_decode($strJsonFileContents, true);
									//var_dump($array); // print array
									//echo $array
									echo "<p>" . $array[description] . "</p>";
									
									?>
										<div class="box alt">
											<div class="row gtr-50 gtr-uniform">
												<?php 
												$directory = "charlottesville/heads/";
												$images = glob($directory. "*.jpg");
												$counter = 0;
												$page = 1;
												foreach($images as $image)
												{
													$counter++;
													#echo $image . "\n";
													
													if ($page == 1 AND $counter <= 24 ){
														echo "<div class='col-2'><span class='image fit'><img src='$image' alt='' /></span></div>";
													} elseif ($page == 1 AND $counter >= 25) {
														$page++;
														$counter = 0;
														echo "<div class='col-2'><span class='image fit'><img src='$image' alt='' /></span></div>";
													} elseif ($page != 1 AND $counter >= 60){
														$page++;
														$counter = 0;
														echo "<div class='col-2'><span class='image fit'><img src='$image' alt='' /></span></div>";
													} else {
														echo "<div class='col-2'><span class='image fit'><img src='$image' alt='' /></span></div>";
													}
												}
												?>
												<!--
												<div class="col-2"><span class="image fit"><img src="images/charlottesville/#.jpg" alt="" /></span></div>
												<div class="col-2"><span class="image fit"><img src="images/pic09.jpg" alt="" /></span></div>
												<div class="col-2"><span class="image fit"><img src="images/pic10.jpg" alt="" /></span></div>
												<div class="col-2"><span class="image fit"><img src="images/pic10.jpg" alt="" /></span></div>
												<div class="col-2"><span class="image fit"><img src="images/pic08.jpg" alt="" /></span></div>
												<div class="col-2"><span class="image fit"><img src="images/pic09.jpg" alt="" /></span></div>
												<!-- Break 
												<div class="col-2"><span class="image fit"><img src="images/charlottesville/#.jpg" alt="" /></span></div>
												<div class="col-2"><span class="image fit"><img src="images/pic09.jpg" alt="" /></span></div>
												<div class="col-2"><span class="image fit"><img src="images/pic10.jpg" alt="" /></span></div>
												<div class="col-2"><span class="image fit"><img src="images/pic10.jpg" alt="" /></span></div>
												<div class="col-2"><span class="image fit"><img src="images/pic08.jpg" alt="" /></span></div>
												<div class="col-2"><span class="image fit"><img src="images/pic09.jpg" alt="" /></span></div>
												<!-- Break -->
											</div>
										</div>
										
										<ul class="pagination">
											<li><span class="button small disabled">Prev</span></li>
											<li><a href="#" class="page active">1</a></li>
											<li><a href="#" class="page">2</a></li>
											<li><a href="#" class="page">3</a></li>
											<li><span>&hellip;</span></li>
											<li><a href="#" class="page">8</a></li>
											<li><a href="#" class="page">9</a></li>
											<li><a href="#" class="page">10</a></li>
											<li><a href="#" class="button small">Next</a></li>
										</ul>		
								
								</div>
							</section>


					</div>

				<!-- Contact 
					<section id="contact">
						<div class="inner">
							<section>
								<form method="post" action="#">
									<div class="fields">
										<div class="field half">
											<label for="name">Name</label>
											<input type="text" name="name" id="name" />
										</div>
										<div class="field half">
											<label for="email">Email</label>
											<input type="text" name="email" id="email" />
										</div>
										<div class="field">
											<label for="message">Message</label>
											<textarea name="message" id="message" rows="6"></textarea>
										</div>
									</div>
									<ul class="actions">
										<li><input type="submit" value="Send Message" class="primary" /></li>
										<li><input type="reset" value="Clear" /></li>
									</ul>
								</form>
							</section>
							<section class="split">
								<section>
									<div class="contact-method">
										<span class="icon solid alt fa-envelope"></span>
										<h3>Email</h3>
										<a href="#">information@untitled.tld</a>
									</div>
								</section>
								<section>
									<div class="contact-method">
										<span class="icon solid alt fa-phone"></span>
										<h3>Phone</h3>
										<span>(000) 000-0000 x12387</span>
									</div>
								</section>
								<section>
									<div class="contact-method">
										<span class="icon solid alt fa-home"></span>
										<h3>Address</h3>
										<span>1234 Somewhere Road #5432<br />
										Nashville, TN 00000<br />
										United States of America</span>
									</div>
								</section>
							</section>
						</div>
					</section>-->

				<!-- Footer -->
					<footer id="footer">
						<div class="inner">
							<ul class="icons">
								<li><a href="#" class="icon brands alt fa-twitter"><span class="label">Twitter</span></a></li>
								<li><a href="#" class="icon brands alt fa-facebook-f"><span class="label">Facebook</span></a></li>
								<li><a href="#" class="icon brands alt fa-instagram"><span class="label">Instagram</span></a></li>
								<li><a href="#" class="icon brands alt fa-github"><span class="label">GitHub</span></a></li>
								<li><a href="#" class="icon brands alt fa-linkedin-in"><span class="label">LinkedIn</span></a></li>
							</ul>
							<ul class="copyright">
								<li>&copy; AltRightDB</li><li>Design by HTML5 UP</li>
							</ul>
						</div>
					</footer>

			</div>

		<!-- Scripts -->
			<script src="../assets/js/jquery.min.js"></script>
			<script src="../assets/js/jquery.scrolly.min.js"></script>
			<script src="../assets/js/jquery.scrollex.min.js"></script>
			<script src="../assets/js/browser.min.js"></script>
			<script src="../assets/js/breakpoints.min.js"></script>
			<script src="../assets/js/util.js"></script>
			<script src="../assets/js/main.js"></script>

	</body>
</html>