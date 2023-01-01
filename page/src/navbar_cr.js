
const mainNavBar = document.querySelector('#main-nav');
//Desk Menu
async function createNavBarDesk() {
    createButtonDesk()
    createDiv1Desk()
    createDiv2Desk()
    createDiv3Desk()
    createDiv4Desk()
    createAsideDesk()
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
    navBarRightLi2Div.classList.add('shopping_cart_amount');
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


//User Cart
async function createAsideDesk() {
    const navBarUsCart = document.createElement('aside');
    navBarUsCart.classList.add('user-cart');
    navBarUsCart.classList.add('inactive');
    navBarUsCart.setAttribute('id', 'user-cart');

    const navBarUsCartDiv0 = document.createElement('div');
    navBarUsCartDiv0.classList.add('cart-in');

    const navBarUsCartDiv0Img = document.createElement('img');
    navBarUsCartDiv0Img.setAttribute('alt', 'arrow');
    navBarUsCartDiv0Img.setAttribute('src', './src/images/arrow.svg');
    navBarUsCartDiv0Img.classList.add('return-arrow');

    const navBarUsCartDiv0P = document.createElement('p');
    navBarUsCartDiv0P.innerText = 'My order'
    navBarUsCartDiv0P.classList.add('user-order');

    const navBarUsCartDiv1 = document.createElement('div');
    navBarUsCartDiv1.classList.add('cart-cont');


    const navBarUsCartDiv1Div0 = document.createElement('div');
    navBarUsCartDiv1Div0.classList.add('cart-item');
    const navBarUsCartDiv1Div1 = document.createElement('div');
    navBarUsCartDiv1Div1.classList.add('cart-item');
    const navBarUsCartDiv1Div2 = document.createElement('div');
    navBarUsCartDiv1Div2.classList.add('cart-item');
    const navBarUsCartDiv1Div3 = document.createElement('div');
    navBarUsCartDiv1Div3.classList.add('cart-item');

    const navBarUsCartDiv1DivDiv = document.createElement('div');
    navBarUsCartDiv1DivDiv.classList.add('cart-item_img_cont');

    const navBarUsCartDiv1DivDivImg = document.createElement('img');
    navBarUsCartDiv1DivDivImg.setAttribute('alt', 'item');
    navBarUsCartDiv1DivDivImg.setAttribute('src', './src/images/ai.png');
    navBarUsCartDiv1DivDivImg.classList.add('cart-item_img');

    const navBarUsCartDiv1DivP1 = document.createElement('p');
    navBarUsCartDiv1DivP1.innerText = 'Byke'

    const navBarUsCartDiv1DivP2 = document.createElement('p');
    navBarUsCartDiv1DivP2.innerText = 'S/ 30'

    const navBarUsCartDiv1DivImg = document.createElement('img');
    navBarUsCartDiv1DivImg.setAttribute('alt', 'eliminate_item');
    navBarUsCartDiv1DivImg.setAttribute('src', './src/images/close_icon.svg');
    navBarUsCartDiv1DivImg.classList.add('cart-item_eliminate');

    const navBarUsCartDiv2 = document.createElement('div');
    navBarUsCartDiv2.classList.add('cart-total');

    const navBarUsCartDiv2P1 = document.createElement('p');
    navBarUsCartDiv2P1.innerText = 'Total'

    const navBarUsCartDiv2P2 = document.createElement('p');
    navBarUsCartDiv2P2.innerText = 'S/ 150'


    navBarUsCartDiv0.appendChild(navBarUsCartDiv0Img)
    navBarUsCartDiv0.appendChild(navBarUsCartDiv0P)
    navBarUsCartDiv2.appendChild(navBarUsCartDiv2P1)
    navBarUsCartDiv2.appendChild(navBarUsCartDiv2P2)
    navBarUsCartDiv1DivDiv.appendChild(navBarUsCartDiv1DivDivImg)
    navBarUsCartDiv1Div1.appendChild(navBarUsCartDiv1DivDiv)
    navBarUsCartDiv1Div1.appendChild(navBarUsCartDiv1DivP1)
    navBarUsCartDiv1Div1.appendChild(navBarUsCartDiv1DivP2)
    navBarUsCartDiv1Div1.appendChild(navBarUsCartDiv1DivImg)
    navBarUsCartDiv1Div2.appendChild(navBarUsCartDiv1DivDiv)
    navBarUsCartDiv1Div2.appendChild(navBarUsCartDiv1DivP1)
    navBarUsCartDiv1Div2.appendChild(navBarUsCartDiv1DivP2)
    navBarUsCartDiv1Div2.appendChild(navBarUsCartDiv1DivImg)
    navBarUsCartDiv1Div3.appendChild(navBarUsCartDiv1DivDiv)
    navBarUsCartDiv1Div3.appendChild(navBarUsCartDiv1DivP1)
    navBarUsCartDiv1Div3.appendChild(navBarUsCartDiv1DivP2)
    navBarUsCartDiv1Div3.appendChild(navBarUsCartDiv1DivImg)
    navBarUsCartDiv1Div0.appendChild(navBarUsCartDiv1DivDiv)
    navBarUsCartDiv1Div0.appendChild(navBarUsCartDiv1DivP1)
    navBarUsCartDiv1Div0.appendChild(navBarUsCartDiv1DivP2)
    navBarUsCartDiv1Div0.appendChild(navBarUsCartDiv1DivImg)

    navBarUsCartDiv1.appendChild(navBarUsCartDiv1Div0)
    navBarUsCartDiv1.appendChild(navBarUsCartDiv1Div1)
    navBarUsCartDiv1.appendChild(navBarUsCartDiv1Div2)
    navBarUsCartDiv1.appendChild(navBarUsCartDiv1Div3)

    navBarUsCart.appendChild(navBarUsCartDiv0)
    navBarUsCart.appendChild(navBarUsCartDiv1)
    navBarUsCart.appendChild(navBarUsCartDiv2)
    mainNavBar.appendChild(navBarUsCart)
}

