/**
 * Recocode.com
 */
(function($) {
    "use strict";
    var MOMB = {};
    $.fn.exists = function() {
        return this.length > 0;
    };

    /* ---------------------------------------------- /*
     * Pre load
    /* ---------------------------------------------- */
    MOMB.PreLoad = function() {
        document.getElementById("loading").style.display = "none";
    }

    /*--------------------
      * Menu toogle header
    ----------------------*/
    MOMB.MenuToggleClass = function() {
        $('.navbar-toggler').on('click', function() {
            var toggle = $('.navbar-toggler').is(':visible');
            if (toggle) {
                $('header').toggleClass('header-toggle');
            }
        })
    }

    /* ---------------------------------------------- /*
     * Header Fixed
    /* ---------------------------------------------- */
    MOMB.HeaderFixd = function() {
        var HscrollTop = $(window).scrollTop();
        var HHeight = $('.header-height').outerHeight()
        var HHeightTop = $('.header-top').outerHeight()

        if (HscrollTop >= 80) {
            $(".navbar-dark-enable").addClass("navbar-light");
            $(".navbar-dark-enable").addClass("navbar-dark-top");
            $(".navbar-dark-enable-top").removeClass("navbar-dark");
            $(".header-main").addClass("fixed-header");
            $('.header-main').css("top", -HHeightTop);
            $('.sticky-lg-top-header').css("top", HHeight);
        } else {
            $(".navbar-dark-enable-top").removeClass("navbar-light");
            $(".navbar-dark-enable-top").addClass("navbar-dark");
            $(".navbar-dark-enable").removeClass("navbar-dark-top");
            $(".header-main").removeClass("fixed-header");
            $('.header-main').css("top", 0);
        }
    }


    /* ---------------------------------------------- /*
     * Header height
    /* ---------------------------------------------- */
    MOMB.HeaderHeight = function() {
        var HHeight = $('.header-height').outerHeight()
        var HHeightTop = $('.header-top').outerHeight()
        $('.header-height-bar').css("min-height", HHeight);
    }

    /* ---------------------------------------------- /*
     * Mega Menu
    /* ---------------------------------------------- */

    MOMB.MegaMenu = function() {
        var mDropdown = $(".px-dropdown-toggle")
        mDropdown.on("click", function() {
            $(this).parent().toggleClass("open-menu-parent");
            $(this).next('.dropdown-menu').toggleClass("show");
            $(this).toggleClass("open");
        });
    }

    /*--------------------
    * Counter
    ----------------------*/
    MOMB.Counter = function() {
        //var counter = jQuery(".counter");
        var $counter = $('.counter');
        if ($counter.length > 0) {
            $counter.each(function() {
                var $elem = $(this);
                $elem.appear(function() {
                    $elem.find('.count').countTo({
                        speed: 2000,
                        refreshInterval: 10
                    });
                });
            });
        }
    }


    /*--------------------
    * Owl Corousel
    ----------------------*/
    MOMB.Owl = function() {
        var owlslider = $("div.owl-carousel");
        if (owlslider.length > 0) {
            owlslider.each(function() {
                var $this = $(this),
                    $items = ($this.data('items')) ? $this.data('items') : 1,
                    $loop = ($this.attr('data-loop')) ? $this.data('loop') : true,
                    $navdots = ($this.data('nav-dots')) ? $this.data('nav-dots') : false,
                    $navarrow = ($this.data('nav-arrow')) ? $this.data('nav-arrow') : false,
                    $autoplay = ($this.attr('data-autoplay')) ? $this.data('autoplay') : false,
                    $autospeed = ($this.attr('data-autospeed')) ? $this.data('autospeed') : 5000,
                    $smartspeed = ($this.attr('data-smartspeed')) ? $this.data('smartspeed') : 1000,
                    $autohgt = ($this.data('autoheight')) ? $this.data('autoheight') : false,
                    $CenterSlider = ($this.data('center')) ? $this.data('center') : false,
                    $stage = ($this.attr('data-stage')) ? $this.data('stage') : 0,
                    $space = ($this.attr('data-space')) ? $this.data('space') : 30;

                $(this).owlCarousel({
                    loop: $loop,
                    items: $items,
                    responsive: {
                        0: {
                            items: $this.data('xs-items') ? $this.data('xs-items') : 1
                        },
                        576: {
                            items: $this.data('sm-items') ? $this.data('sm-items') : 1
                        },
                        768: {
                            items: $this.data('md-items') ? $this.data('md-items') : 1
                        },
                        992: {
                            items: $this.data('lg-items') ? $this.data('lg-items') : 1
                        },
                        1200: {
                            items: $items
                        }
                    },
                    dots: $navdots,
                    autoplayTimeout: $autospeed,
                    smartSpeed: $smartspeed,
                    autoHeight: $autohgt,
                    center: $CenterSlider,
                    margin: $space,
                    stagePadding: $stage,
                    nav: $navarrow,
                    navText: ["<i class='bi bi-chevron-left'></i>", "<i class='bi bi-chevron-right'></i>"],
                    autoplay: $autoplay,
                    autoplayHoverPause: true
                });
            });
        }
    }

    /* ---------------------------------------------- /*
     * lightbox gallery
    /* ---------------------------------------------- */
    MOMB.Gallery = function() {
        var GalleryPopup = $('.lightbox-gallery');
        if (GalleryPopup.length > 0) {
            $('.lightbox-gallery').magnificPopup({
                delegate: '.gallery-link',
                type: 'image',
                tLoading: 'Loading image #%curr%...',
                mainClass: 'mfp-fade',
                fixedContentPos: true,
                closeBtnInside: false,
                gallery: {
                    enabled: true,
                    navigateByImgClick: true,
                    preload: [0, 1] // Will preload 0 - before current, and 1 after MOMB current image
                }
            });
        }
        var VideoPopup = $('.video-btn');
        if (VideoPopup.length > 0) {
            $('.video-btn').magnificPopup({
                disableOn: 700,
                type: 'iframe',
                mainClass: 'mfp-fade',
                removalDelay: 160,
                preloader: false,
                fixedContentPos: false
            });
        }
    }


    /*--------------------
        * Progress Bar 
    ----------------------*/
    MOMB.ProgressBar = function() {
        $(".skill-bar .skill-bar-in").each(function() {
            var bottom_object = $(this).offset().top + $(this).outerHeight();
            var bottom_window = $(window).scrollTop() + $(window).height();
            var progressWidth = $(this).attr('aria-valuenow') + '%';
            if (bottom_window > bottom_object) {
                $(this).css({
                    width: progressWidth
                });
            }
        });
    }
    

    /*--------------------
        * count down
    ----------------------*/

    MOMB.CountTimer = function() {
        var $count_timer = $('.count-down');
        var regionalVar = { days: 'Days', day: 'Day', years: 'Years', year: 'Year', hours: 'Hours', hour: 'Hour', minutes: 'Minutes', minute: 'Minute', seconds: 'Seconds', second: 'Second' };
        if ($count_timer.length > 0) {
            $('.count-down').countdown({ regional: regionalVar });
        }
    }

    /*--------------------
        * Nice Select
    ----------------------*/
    MOMB.nice_select = function() {
        var $NiceSelect = $('.px-nice-select');
        if ($NiceSelect.length > 0) {
            $NiceSelect.each(function() {
                $('select.px-nice-select').niceSelect();
            });
        }

    }

    /*--------------------
        * Custom file Upload
    ----------------------*/
    MOMB.custom_upload = function() {
        var $CustomUpload = $('.px-input-file');
        if ($CustomUpload.length > 0) {
            var inputs = document.querySelectorAll('.px-input-file');
            Array.prototype.forEach.call(inputs, function(input) {
                var label = input.nextElementSibling,
                    labelVal = label.innerHTML;

                input.addEventListener('change', function(e) {
                    var fileName = '';
                    if (this.files && this.files.length > 1) {
                        fileName = (this.getAttribute('data-multiple-caption') || '').replace('{count}', this.files.length);
                    } else {
                        fileName = e.target.value.split('\\').pop();
                    }

                    if (fileName) {
                        label.querySelector('span.px-input-selected-file').innerHTML = fileName;
                    } else {
                        label.innerHTML = labelVal;
                    }
                });
            });
        }
    }

    /*--------------------
        * Uploaded Preview
    ----------------------*/
    MOMB.px_avatar_Upload = function() {
        var $pximageUpload = $('.px-avatar-upload');
        if ($pximageUpload.length > 0) {
            function readURL(input) {
                if (input.files && input.files[0]) {
                    var reader = new FileReader();
                    reader.onload = function(e) {
                        $('#px_image_Preview').css('background-image', 'url('+e.target.result +')');
                        $('#px_image_Preview').hide();
                        $('#px_image_Preview').fadeIn(650);
                    }
                    reader.readAsDataURL(input.files[0]);
                }
            }
            $("#px_image_Upload").change(function() {
                readURL(this);
            });
        }
    }


    /*--------------------
        * One Page
    ----------------------*/
    MOMB.one_page = function() {
        //var HHeight = $('.navbar').outerHeight();
        var $one_page_nav = $('.one-page-nav');
        if ($one_page_nav.length > 0) {
            $one_page_nav.each(function() {
                $.scrollIt({
                    upKey: 38, // key code to navigate to the next section
                    downKey: 40, // key code to navigate to the previous section
                    easing: 'linear', // the easing function for animation
                    scrollTime: 600, // how long (in ms) the animation takes
                    activeClass: 'active', // class given to the active nav element
                    onPageChange: null, // function(pageIndex) that is called when page is changed
                    topOffset: -70 // offste (in px) for fixed top navigation
                });
            });
        }
    }


    // Window on Load
    $(window).on("load", function() {    
        MOMB.PreLoad();
    });
    // Document on Ready
    $(document).ready(function() {
        MOMB.HeaderFixd(),
        MOMB.Counter(),
        MOMB.MenuToggleClass(),
        MOMB.Gallery(),
        MOMB.HeaderHeight(),
        MOMB.ProgressBar(),
        MOMB.CountTimer(),
        MOMB.nice_select(),
        MOMB.MegaMenu(),
        MOMB.one_page(),
        MOMB.custom_upload(),
        MOMB.px_avatar_Upload(),
        MOMB.Owl();
    });

    // Document on Scrool
    $(window).scroll(function() {
        MOMB.ProgressBar(),
        MOMB.HeaderFixd();
    });

    // Window on Resize
    $(window).resize(function() {
        MOMB.HeaderHeight();
    });

})(jQuery);