// static/js/slider.js 파일에 작성
document.addEventListener('DOMContentLoaded', function() {
    const sliderTrack = document.querySelector('.slider-track');
    const slides = Array.from(document.querySelectorAll('.slide'));
    const nextButton = document.querySelector('.next-button');
    const prevButton = document.querySelector('.prev-button');
    const dots = Array.from(document.querySelectorAll('.dot'));

    let currentSlideIndex = 0;
    const totalSlides = slides.length;

    function showSlide(index) {
        // 인덱스가 범위를 벗어나지 않도록 조정 (무한 루프 구현 시 필요)
        if (index >= totalSlides) {
            currentSlideIndex = 0;
        } else if (index < 0) {
            currentSlideIndex = totalSlides - 1;
        } else {
             currentSlideIndex = index;
        }


        // 슬라이더 트랙을 이동
        const offset = -currentSlideIndex * 100; // 100%씩 이동
        sliderTrack.style.transform = `translateX(${offset}%)`;

        // 점(dot) 활성화 상태 업데이트
        dots.forEach((dot, i) => {
            if (i === currentSlideIndex) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    }

    // 다음 버튼 클릭 이벤트
    nextButton.addEventListener('click', () => {
        showSlide(currentSlideIndex + 1);
    });

    // 이전 버튼 클릭 이벤트
    prevButton.addEventListener('click', () => {
        showSlide(currentSlideIndex - 1);
    });

    // 점(dot) 클릭 이벤트
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            showSlide(index);
        });
    });

    // (선택 사항) 자동 슬라이드 기능
    // let autoSlideTimer = setInterval(() => {
    //     showSlide(currentSlideIndex + 1);
    // }, 5000); // 5초마다 자동 전환

    // (선택 사항) 마우스 오버 시 자동 슬라이드 중지 등 추가 로직
});