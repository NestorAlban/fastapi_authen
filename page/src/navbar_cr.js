
const mainNavBar = document.querySelector('#main-nav');
//Desk Menu
async function createNavBarDesk() {
    createButtonDesk()
    createDiv1Desk()
    createDiv2Desk()
    createDiv3Desk()
    createDiv4Desk()
}
//menu
async function createButtonDesk() {
    const headerDeskMenu = document.createElement('button');
    headerDeskMenu.classList.add('header_desk_menu');

    const headerDeskMenuSpan = document.createElement('span');

    const headerDeskMenuImg = document.createElement('img');
    headerDeskMenuImg.setAttribute('alt', 'menu');
    headerDeskMenuImg.setAttribute('src', './src/images/menu_1.svg');
    headerDeskMenuImg.classList.add('menu');

    const headerDeskMenuImgSpan = document.createElement('span');
    headerDeskMenuImgSpan.classList.add('header_desk_menu-text');
    headerDeskMenuImgSpan.innerText = 'Menu';

    headerDeskMenuSpan.appendChild(headerDeskMenuImg)
    headerDeskMenuSpan.appendChild(headerDeskMenuImgSpan)
    headerDeskMenu.appendChild(headerDeskMenuSpan)
    mainNavBar.appendChild(headerDeskMenu)
}
//Left
async function createDiv1Desk() {
    const navBarLeft = document.createElement('div');
    navBarLeft.classList.add('navbar-left');
    
    const navBarLeftImg = document.createElement('img');
    navBarLeftImg.setAttribute('alt', 'logo');
    navBarLeftImg.setAttribute('src', './src/images/dragon-vector-icon-illustration.svg');
    navBarLeftImg.classList.add('logo');

    navBarLeft.appendChild(navBarLeftImg)
    mainNavBar.appendChild(navBarLeft)

}
//Center
async function createDiv2Desk() {
    const navBarCenter = document.createElement('div');
    navBarCenter.classList.add('navbar-center');

    const navBarCenterForm = document.createElement('form');
    navBarCenterForm.setAttribute('id', 'searchForm')
    navBarCenterForm.classList.add('nav-searchForm');
    
    const navBarCenterInput = document.createElement('input');
    navBarCenterInput.setAttribute('type', 'text');
    navBarCenterInput.setAttribute('placeholder', 'Search');

    const navBarCenterButton = document.createElement('button');
    navBarCenterButton.setAttribute('type', 'submit');
    navBarCenterButton.innerText = '🔍';

    navBarCenterForm.appendChild(navBarCenterInput)
    navBarCenterForm.appendChild(navBarCenterButton)
    navBarCenter.appendChild(navBarCenterForm)
    mainNavBar.appendChild(navBarCenter)
}
//Right
async function createDiv3Desk() {
    const navBarRight = document.createElement('div');
    navBarRight.classList.add('navbar-right');

    const navBarRightUl = document.createElement('ul');
    
    const navBarRightLi1 = document.createElement('li');
    navBarRightLi1.classList.add('navbar-email');
    navBarRightLi1.innerText = 'dragon@example.com';

    const navBarRightLi2 = document.createElement('li');
    navBarRightLi2.classList.add('navbar-shopping-cart');

    const navBarRightLi2Img = document.createElement('img');
    navBarRightLi2Img.setAttribute('alt', 'shopping cart');
    navBarRightLi2Img.setAttribute('src', './src/images/carro.svg');
    navBarRightLi2Img.classList.add('shopping_cart');

    const navBarRightLi2Div = document.createElement('div');
    navBarRightLi2Div.innerText = 2;

    navBarRightLi2.appendChild(navBarRightLi2Img)
    navBarRightLi2.appendChild(navBarRightLi2Div)
    navBarRightUl.appendChild(navBarRightLi1)
    navBarRightUl.appendChild(navBarRightLi2)
    navBarRight.appendChild(navBarRightUl)
    mainNavBar.appendChild(navBarRight)
}
//User Data
async function createDiv4Desk() {
    const navBarUsData = document.createElement('div');
    navBarUsData.classList.add('user-menu');
    navBarUsData.classList.add('inactive');
    navBarUsData.setAttribute('id', 'user-data');

    const navBarUsDataDiv1 = document.createElement('div');
    navBarUsDataDiv1.classList.add('user-image-cont');


    const navBarUsDataDiv1Img = document.createElement('img');
    navBarUsDataDiv1Img.setAttribute('alt', 'usuario');
    navBarUsDataDiv1Img.setAttribute('src', './src/images/setsuna.png');
    navBarUsDataDiv1Img.classList.add('user-image');

    const navBarUsDataDiv2 = document.createElement('div');
    navBarUsDataDiv2.classList.add('user-data-cont');

    const navBarUsDataDiv2Ul1 = document.createElement('ul');

    const navBarUsDataDiv2Ul1Li1 = document.createElement('li');

    const navBarUsDataDiv2Ul1Li1A = document.createElement('a');
    navBarUsDataDiv2Ul1Li1A.setAttribute('href', '');
    navBarUsDataDiv2Ul1Li1A.innerText = 'My orders'

    const navBarUsDataDiv2Ul1Li2 = document.createElement('li');

    const navBarUsDataDiv2Ul1Li2A = document.createElement('a');
    navBarUsDataDiv2Ul1Li2A.setAttribute('href', '');
    navBarUsDataDiv2Ul1Li2A.innerText = 'Profile'

    const navBarUsDataDiv2Ul2 = document.createElement('ul');

    const navBarUsDataDiv2Ul2Li = document.createElement('li');

    const navBarUsDataDiv2Ul2LiA = document.createElement('a');
    navBarUsDataDiv2Ul2LiA.setAttribute('href', '');
    navBarUsDataDiv2Ul2LiA.innerText = 'Sign out'

    
    navBarUsDataDiv2Ul2Li.appendChild(navBarUsDataDiv2Ul2LiA)
    navBarUsDataDiv2Ul2.appendChild(navBarUsDataDiv2Ul2Li)
    navBarUsDataDiv2Ul1Li2.appendChild(navBarUsDataDiv2Ul1Li2A)
    navBarUsDataDiv2Ul1Li1.appendChild(navBarUsDataDiv2Ul1Li1A)
    navBarUsDataDiv2Ul1.appendChild(navBarUsDataDiv2Ul1Li1)
    navBarUsDataDiv2Ul1.appendChild(navBarUsDataDiv2Ul1Li2)
    navBarUsDataDiv2.appendChild(navBarUsDataDiv2Ul1)
    navBarUsDataDiv2.appendChild(navBarUsDataDiv2Ul2)
    navBarUsDataDiv1.appendChild(navBarUsDataDiv1Img)
    navBarUsData.appendChild(navBarUsDataDiv1)
    navBarUsData.appendChild(navBarUsDataDiv2)
    mainNavBar.appendChild(navBarUsData)
}


