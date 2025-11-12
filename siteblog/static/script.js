// Получаем элементы
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('nav-menu');
const navLinks = document.querySelectorAll('#nav-menu ul li a');

// Обработчик для гамбургер-меню
hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');
});

// Функция для установки активного пункта меню
function setActiveMenuItem() {
    const currentPath = window.location.pathname;

    navLinks.forEach(link => {
        link.classList.remove('active');
        const linkPath = link.getAttribute('href');
        const regex = new RegExp(`^${linkPath}(\/|$)`);

        if (regex.test(currentPath)) {
            link.classList.add('active');
        }
    });

    // Выделение "Главной" для корневой страницы
    if ((currentPath === '/' || currentPath.endsWith('index.html')) &&
        !document.querySelector('#nav-menu ul li a.active')) {
        navLinks.forEach(link => {
            if (link.textContent.trim() === 'Главная') {
                link.classList.add('active');
            }
        });
    }
}

// Функция для установки активной страницы пагинации
function setActivePage() {
    const urlParams = new URLSearchParams(window.location.search);
    const currentPage = urlParams.get('page') || '1';

    document.querySelectorAll('.page-button').forEach(button => {
        const buttonPage = button.getAttribute('href').split('page=')[1] || '1';

        if (buttonPage === currentPage) {
            button.classList.add('active');
        } else {
            button.classList.remove('active');
        }
    });
}

// Обработчики событий
document.addEventListener('DOMContentLoaded', () => {
    setActiveMenuItem();
    setActivePage();
});

window.addEventListener('popstate', () => {
    setActiveMenuItem();
    setActivePage();
});

// Закрытие меню при клике вне области
document.addEventListener('click', (e) => {
    if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
        navMenu.classList.remove('active');
    }
});

// Плавный скролл для внутренних ссылок (опционально)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});


// Yandex.Metrika counter
   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();
   for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
   k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

   ym(101483941, "init", {
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true,
        webvisor:true
   });
