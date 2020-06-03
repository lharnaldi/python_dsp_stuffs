<?php
/*
 * MyWeb
 *
 *   simple web page implementation on top of bootstrap 4
 *   configuration by modifying manually the public members of the class
 *   Uses:
 *     bootstrap4 (4.4.1)
 *     jquery3 (3.4.1)
 *     popper1 (1.16.0)
 *     aos2 (2.3.1)
 *     fontawesome5 (5.13.0)
 *
 *  This is WyWeb version 0.2 of May 11 2020
 *    Changes 0.2:
 *    * language picker using $_SESSION
 *    * adding hovering effects
 *    * adding text bubbles
 *    * separate call for CSS via $_GET
 */
  if ($_GET["css"]) {
    header('Content-Type: text/css');
?>
.english, .spanish {
  display: none;
}
.my-banner {
  padding:9em 0;
  transition: background-color 5s;
}
.my-bg {
  background-color: var(--maincolor);
}
.my-bg-img {
  position: relative;
  height:400px;
  background-color: var(--mainbannercolor);
  z-index:-99;
}
.my-bg-img img,video {
  z-index:-90;
  position:fixed; 
  margin: 0 auto;
  left: 0;
  right:0;
  max-width:100%;
}
.my-text {
  color: var(--maincolor);
}
.my-up-arrow {
  position:fixed;
  width:35px;
  height:35px;
  font-size:1.4rem;
  border-radius: 50px;
  bottom: 0px;
  right:0px;
  border: 1px solid;
}
.my-bg-hover {
  background-size: 100% 200%;
  background-image: linear-gradient(to bottom, white 50%, var(--maincolor) 50%);
  transition: all 1s;
}
.my-bg-hover i {
  color: var(--maincolor);
  transition: all 1s;
}
.my-bg-hover:hover i {
  color: white;
}
.my-bg-hover:hover {
  color: white;
  background-position: 0 100%;
}
.my-bg-hover-top:hover {
  background-position: 0 -100%;
}
.my-bubble {
  position: relative;
  background-color: #fff;
  box-shadow:  0 0.125rem 0.5rem rgba(0, 0, 0, .1), 0 0.0625rem 0.125rem rgba(0, 0, 0, .1);
}
.my-bubble::before {
  content: '';
  position: absolute;
  width: 0;
  height: 0;
  top: 100%;
  left: 50%;
  border: .75rem solid transparent;
  border-bottom: none;

  border-top-color: #fff;
  filter: drop-shadow(0 0.0625rem 0.0625rem rgba(0, 0, 0, .1));
}
<?php
    exit;
  }
  session_start();
  // Language handling
  if ($_POST["name"]) {
    $_SESSION["lang"]="ENG";
    if ($_POST["name"]=="ESP") $_SESSION["lang"]="ESP";
  }

  /*
   *
   * Main PHP class for formatting
   *
   */

class MyWeb {
  public $webmain="/";                  // Home of web site 
  public $webname="MyWebPage";          // Name of the web site
  public $darknavbar=1;                 // If nav bars are dark or light (dark by default)
  public $maincolor="#55905a";          // Main color theme (green by default)
  public $visualbannercolor="#F5F4F0";  // Background color for visual image banner
  public $topnavmenu="";                // Menus of top navbar
  public $langpicker=1;                 // Top navbar language picker (ENG/SPA)

  // 2 functions:
  // Header() to display header, open the body and display top navbar
  // Footer() to display the bottom navbar and close the body

  function Header() {
?>
<!DOCTYPE html>
<html lang="en">
<head>
<title><?php echo $this->webname ?></title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- bootstrap & jquery -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
  <!-- aos -->
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <!-- font awesome -->
  <script src="https://kit.fontawesome.com/ebedddc1c9.js" crossorigin="anonymous"></script>
  <!-- MyWeb -->
  <link href="<?php echo $this->webmain ?>/_MyWeb.php?css=1" rel="stylesheet"></link>
</head>
<body>
<style>
:root {
--maincolor: <?php echo $this->maincolor ?>;
--mainbannercolor: <?php echo $this->visualbannercolor ?>;
}
</style>

<script>
  // multi-lang
  function English() {
    $('.english').css("display","inline");
    $('.spanish').css("display","none");
    $.post('<?php echo $this->webmain ?>/_MyWeb.php', { name: 'ENG' });
  }
  function Spanish() {
    $('.english').css("display","none");
    $('.spanish').css("display","inline");
    $.post('<?php echo $this->webmain ?>/_MyWeb.php', { name: 'ESP' });
  }
  // AOS
  AOS.init();
  // Set proper language, remove banner bg and refresh AOS
  $(window).on('load', function() {
    // Load language depending on session value
<?php 
    if($this->langpicker) {
      if ($_SESSION["lang"]=="ESP") {
?>
    Spanish();
<?php } else { ?>
    English();
<?php 
      }
    }
 ?>
    AOS.refresh();
    $('#banner').removeClass('bg-dark');
  });
  // scrolling to #anchor, removing navbar size
  $(document).on('click', 'a[href^="#"]', function (event) {
    event.preventDefault();
    $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top-$('.navbar-collapse').height()
    }, 500);
  });
  // hide fixed image on scroll
  $(window).scroll(function() {
    if ($(this).scrollTop() > 500) {
      $('#bg-img').hide();
    } else {
      $('#bg-img').show();
    }
  });

</script>


  <nav class="navbar <?php if ($this->darknavbar) { ?>navbar-dark bg-dark <?php } else { ?>navbar-light bg-light <?php } ?>navbar-expand-sm sticky-top py-0 border-bottom  border-secondary" id=navbar>
<a class="navbar-brand" href="<?php echo $this->webmain ?>"><?php echo $this->webname ?></a>
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
  <ul class="navbar-nav ml-auto">
<?php
    echo $this->topnavmenu;
?>
  </ul>
  </div>
<?php
    if ($this->langpicker) {
?>
<ul class="navbar-nav ml-auto">
<li class="nav-item spanish"><a class="nav-link small" id="toeng" href="#"><u>English</u></a></li>
<li class="nav-item english"><a class="nav-link small" id="toesp" href="#"><u>Español</u></a></li>
</ul>
<script>
  $('#toeng').click(function(){ English(); return false; });
  $('#toesp').click(function(){ Spanish(); return false; });
</script>
<?php
    }
?>
  <button class="navbar-toggler small ml-2" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon small"></span>
  </button>
</nav>

<span id=top></span>
<?php
  }
  function Footer() {
?>
<div class="my-bg text-light text-center mr-2 mb-4 my-up-arrow">
<a class="text-light" href="#top"><i class='fas fa-angle-up'></i></a>
</div>
<nav class="navbar <?php if ($this->darknavbar) { ?>navbar-dark bg-dark <?php } else { ?>navbar-light bg-light <?php } ?> fixed-bottom mt-4 border-top border-secondary">
</nav>
        </body>
</html>
<?php
  }
}
?>

