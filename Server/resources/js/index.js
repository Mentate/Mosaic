'use-strict'
let submit = $('#submit'),
    imageForm = $('#image-form'),
    cancelImages = $('#cancel-images'),
    imageUpload = $('#image-upload'),
    slideHolder = $('#slide-holder'),
    magDropdown = $('#magDropdown'),
    magLevelButton = $('#magLevelButton'),
    dropdownItem = $('.dropdown-item');

imageUpload.change(function() {
    cancelImages.click();

    if (this.files.length > 0) {
        if (this.files.length > 1) {
            $('.carousel-control-prev').removeClass('d-none');
            $('.carousel-control-next').removeClass('d-none');
        }

        cancelImages.prop("disabled", false);
        submit.prop("disabled", false);
        $('#image-label').text(this.files.length + ' images selected');

        $.each(this.files, function(idx, file) {
            let reader = new FileReader();

            reader.onload = function(e) {
                let carouselItem = $('<div class="carousel-item"></div>'),
                    image = $('<img class="d-block w-100"/>')
                        .attr({
                            src: e.target.result,
                            alt: 'Slide ' + slideHolder.children.length
                        }),
                    caption = $('<div class="carousel-caption d-none d-md-block"></div>'),
                    captionText = $('<span class="caption-text"></span>').text(e.target.fileName);
                        
                if (idx === 0) {
                    carouselItem.addClass('active');
                    $('#placeholder').parent().remove()
                }
                
                caption.append(captionText);
                carouselItem.append(image);
                carouselItem.append(caption);
                slideHolder.append(carouselItem);
            }

            reader.fileName = file.name;
            reader.readAsDataURL(file);
        });
    }
});

cancelImages.click(function() {
    let placeholder = $('<div class="carousel-item active"><img id="placeholder" class="d-block w-100" src="/resources/imgs/no-slides.jpg" alt="No Slides"></div>');

    cancelImages.prop("disabled", true);
    submit.prop("disabled", true);
    $('.carousel-control-prev').addClass('d-none');
    $('.carousel-control-next').addClass('d-none');
    $('#image-label').text('Choose images');

    while (slideHolder.children().length !== 0) {
        slideHolder.children()[0].remove();
    }

    placeholder.addClass('active');
    slideHolder.append(placeholder);
});

dropdownItem.on("click", function (e) {
    e.preventDefault();
    var magLevel = $(this).html();
    magLevelButton.text("Mag Level: " + magLevel);
    $("#magLevelInput").val(magLevel);
});


submit.click(function() {
    imageForm.submit();
});