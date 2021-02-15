/*  ---------------------------------------------------
    Template Name: HVAC
    Description: HVAC Car Dealer HTML Template
    Author: Colorlib
    Author URI: https://www.colorlib.com
    Version: 1.0
    Created: Colorlib
---------------------------------------------------------  */

'use strict';

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");

        /*------------------
            Car filter
        --------------------*/
        $('.filter__controls li').on('click', function () {
            $('.filter__controls li').removeClass('active');
            $(this).addClass('active');
        });
        if ($('.car-filter').length > 0) {
            var containerEl = document.querySelector('.car-filter');
            var mixer = mixitup(containerEl);
        }
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    //Canvas Menu
    $(".canvas__open").on('click', function () {
        $(".offcanvas-menu-wrapper").addClass("active");
        $(".offcanvas-menu-overlay").addClass("active");
    });

    $(".offcanvas-menu-overlay").on('click', function () {
        $(".offcanvas-menu-wrapper").removeClass("active");
        $(".offcanvas-menu-overlay").removeClass("active");
    });

    //Search Switch
    $('.search-switch').on('click', function () {
        $('.search-model').fadeIn(400);
    });

    $('.search-close-switch').on('click', function () {
        $('.search-model').fadeOut(400, function () {
            $('#search-input').val('');
        });
    });

    /*------------------
        Navigation
    --------------------*/
    $(".header__menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*--------------------------
        Testimonial Slider
    ----------------------------*/
    $(".car__item__pic__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: true,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: false
    });

    /*--------------------------
        Testimonial Slider
    ----------------------------*/
    var testimonialSlider = $(".testimonial__slider");
    testimonialSlider.owlCarousel({
        loop: true,
        margin: 0,
        items: 2,
        dots: true,
        nav: true,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: false,
        responsive: {
            768: {
                items: 2
            },
            0: {
                items: 1
            }
        }
    });

    /*-----------------------------
        Car thumb Slider
    -------------------------------*/
    $(".car__thumb__slider").owlCarousel({
        loop: true,
        margin: 25,
        items: 5,
        dots: false,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        mouseDrag: false,
        responsive: {

            768: {
                items: 5
            },
            320: {
                items: 3
            },
            0: {
                items: 2
            }
        }
    });

    /*-----------------------
        Range Slider
    ------------------------ */
    var rangeSlider = $(".price-range");
    rangeSlider.slider({
        range: true,
        min: 1,
        max: 4000,
        values: [800, 3200],
        slide: function (event, ui) {
            $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1] + ".100");
        }
    });
    $("#amount").val("$" + $(".price-range").slider("values", 0) + " - $" + $(".price-range").slider("values", 1) + ".100");

    var carSlider = $(".car-price-range");
    carSlider.slider({
        range: true,
        min: 1,
        max: 4000,
        values: [900, 3000],
        slide: function (event, ui) {
            $("#caramount").val("$" + ui.values[0] + " - $" + ui.values[1] + ".100");
        }
    });
    $("#caramount").val("$" + $(".car-price-range").slider("values", 0) + " - $" + $(".car-price-range").slider("values", 1) + ".100");

    var filterSlider = $(".filter-price-range");
    filterSlider.slider({
        range: true,
        min: 0,
        max: 4000000,
        values: [0, 4000000],
        slide: function (event, ui) {
            $("#filterAmount").val("[ " + ui.values[0] + "원" + ' - ' + ui.values[1] + "원" + " ]");
        }
    });
    $("#filterAmount").val("[ " + $(".filter-price-range").slider("values", 0) + "원" + " - " + $(".filter-price-range").slider("values", 1) + "원" + " ]");

    /*--------------------------
        Select
    ----------------------------*/
    $("select").niceSelect();

    /*------------------
        Magnific
    --------------------*/
    $('.video-popup').magnificPopup({
        type: 'iframe'
    });

    /*------------------
        Single Product
    --------------------*/
    $('.car-thumbs-track .ct').on('click', function () {
        $('.car-thumbs-track .ct').removeClass('active');
        var imgurl = $(this).data('imgbigurl');
        var bigImg = $('.car-big-img').attr('src');
        if (imgurl != bigImg) {
            $('.car-big-img').attr({
                src: imgurl
            });
        }
    });

    /*------------------
        Counter Up
    --------------------*/
    $('.counter-num').each(function () {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 4000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });



})(jQuery);

//Note jquery and jqueryUI are included

function collision($div1, $div2) {
    var x1 = $div1.offset().left;
    var w1 = 40;
    var r1 = x1 + w1;
    var x2 = $div2.offset().left;
    var w2 = 40;
    var r2 = x2 + w2;

    if (r1 < x2 || x1 > r2) return false;
    return true;

}

function showProducts(minPrice, maxPrice) {
    $("#products li").hide().filter(function () {
        var price = parseInt($(this).data("price"), 10);
        return price >= minPrice && price <= maxPrice;
    }).show();
}

// $(function() {
//     var options = {
//         range: true,
//         min: 0,
//         max: 500,
//         values: [50, 300],
//         slide: function(event, ui) {
//             var min = ui.values[0],
//                 max = ui.values[1];

//             $("#amount").val("$" + min + " - $" + max);
//             showProducts(min, max);
//         }
//     }, min, max;

//     $("#slider-range").slider(options);

//     min = $("#slider-range").slider("values", 0);
//     max = $("#slider-range").slider("values", 1);

//     $("#amount").val("$" + min + " - $" + max);

//     showProducts(min, max);
// });

$(function () {
    let INITIAL_RANGE_VALUES = [document.getElementById('price_min').value, document.getElementById('price_max').value]
    var MIN_RANGE = 0;
    var MAX_RANGE = 500;

    $('.js-price-range').slider({
        range: true,
        min: MIN_RANGE,
        max: MAX_RANGE,
        values: INITIAL_RANGE_VALUES,

        slide: function (event, ui) {
            $('.js-price_min').val(ui.values[0]);
            $('.js-price_max').val(ui.values[1]);

            setHandleValues(ui.values);
        }

    });


    function getRangeValues(numberValue) {
        return $('.js-price-range').slider('values', numberValue);
    }

    function setValueToInputs() {
        $('.js-price_min').attr('value', getRangeValues(0));
        $('.js-price_max').attr('value', getRangeValues(1));
    }

    function setHandleValues(values) {
        $('.ui-slider-handle:nth-child(2) .ui-slider-handle-value').text(values[0] + '만원');
        $('.ui-slider-handle:nth-child(3) .ui-slider-handle-value').text(values[1] + '만원');
    }

    setValueToInputs();

    $('.js-price_min').change(function () {
        var minValue = $('.js-price_min').val();
        var maxValue = $('.js-price_max').val();
        if (Number(minValue) <= Number(maxValue)) {
            if (Number(minValue) < MIN_RANGE) {
                minValue = MIN_RANGE;
                $('.js-price_min').val(minValue);
            }
            $('.js-price-range').slider('values', 0, minValue);
            $('.ui-slider-handle:nth-child(2) .ui-slider-handle-value').text(minValue + '만원');
        } else {
            $('.js-price-range').slider('values', 0, maxValue);
            $('.ui-slider-handle:nth-child(2) .ui-slider-handle-value').text(maxValue + '만원');
            $('.js-price_min').val(maxValue);
        }
    });

    $('.js-price_max').change(function () {
        var minValue = $('.js-price_min').val();
        var maxValue = $('.js-price_max').val();
        if (Number(maxValue) >= Number(minValue)) {
            if (Number(maxValue) > MAX_RANGE) {
                maxValue = MAX_RANGE;
                $('.js-price_max').val(maxValue);
            }
            $('.js-price-range').slider('values', 1, maxValue);
            $('.ui-slider-handle:nth-child(3) .ui-slider-handle-value').text(maxValue + '만원');
        } else {
            $('.js-price-range').slider('values', 1, minValue);
            $('.ui-slider-handle:nth-child(3) .ui-slider-handle-value').text(minValue + '만원');
            $('.js-price_max').val(minValue);
        }
    });

    setTimeout(function () {
        var handleValue = $('<span class="ui-slider-handle-value"></span>');
        var handleValueMin = handleValue.text($('.js-price-range').slider('values', 0) + '만원');
        $('.js-price-range .ui-slider-handle:nth-child(2)').append(handleValueMin);
    });

    setTimeout(function () {
        var handleValue = $('<span class="ui-slider-handle-value"></span>');
        var handleValueMax = handleValue.text($('.js-price-range').slider('values', 1) + '만원');
        $('.js-price-range .ui-slider-handle:nth-child(3)').append(handleValueMax);
    });

    $('.js-clear-all').on('click', function () {
        $('.js-price-range').slider('values', INITIAL_RANGE_VALUES);
        setValueToInputs();
        setHandleValues(INITIAL_RANGE_VALUES);
    });

});