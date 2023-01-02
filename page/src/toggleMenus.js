
var i = 1;
var emailNav;
var asideNav0;
var asideNav1;
var asideNav2;
var generalNav0;
var generalNav1;
var generalNav2;
var emailDeskMenu;
var asideDeskMenu;
var generalDeskMenu;
var isEmailClose;
var isAsideClose;
var isGeneralClose;

mainNavBar.addEventListener('click', (e) => {
    const eTarget = e.target
    console.log(eTarget);
    
    const classEvent = e.target.getAttributeNode('class');
    // const eChild0 = eTarget.children[0];
    // const eChild1 = eTarget.childNodes[1].getAttributeNode('class').value;
    // console.log('eChild0');
    // console.log(eChild0);
    if (i == 1) {
        console.log(i)
        emailDeskMenu = document.querySelector('.user-menu');
        emailNav = document.querySelector('.navbar-email');
        // isEmailClose = emailDeskMenu.classList.contains('inactive');
        
        asideDeskMenu = document.querySelector('.user-cart');
        asideNav0 = document.querySelector('.navbar-shopping-cart');
        asideNav1 = document.querySelector('.shopping_cart');
        asideNav2 = document.querySelector('.shopping_cart_amount');
        // isAsideClose = asideDeskMenu.classList.contains('inactive');

        generalDeskMenu = document.querySelector('.desk-menu');
        generalNav0 = document.querySelector('img.menu');
        generalNav1 = document.querySelector('span.header_desk_menu-text');
        generalNav2 = document.querySelector('.header_desk_menu');
        // console.log(generalNav0);
        i+=1
        // if (generalNav0 == newu) {
        //     console.log('yes')
        // } else {
        //     console.log('no')
        // }
    }
    // console.log(generalNav3);
    if (classEvent) {
        if (eTarget == emailNav) {
            toggleEmailDeskMenu()
        }
        if (eTarget == asideNav0 || eTarget == asideNav1 || eTarget == asideNav2) {
            toggleAsideDeskMenu()
        }
        if ( eTarget == generalNav1 || eTarget == generalNav0 || eTarget == generalNav2) {
            toggleGeneralDeskMenu()
        }

    }
});

async function toggleEmailDeskMenu(){
    var isAsideClose = asideDeskMenu.classList.contains('inactive');
    var isGeneralClose = generalDeskMenu.classList.contains('inactive');
    if (!isAsideClose) {
        asideDeskMenu.classList.add('inactive')
    }
    if (!isGeneralClose) {
        generalDeskMenu.classList.add('inactive')
    }
    
    emailDeskMenu.classList.toggle('inactive');
}

async function toggleAsideDeskMenu(){
    var isEmailClose = emailDeskMenu.classList.contains('inactive');
    var isGeneralClose = generalDeskMenu.classList.contains('inactive');
    if (!isEmailClose) {
        emailDeskMenu.classList.add('inactive')
    }
    if (!isGeneralClose) {
        generalDeskMenu.classList.add('inactive')
    }

    asideDeskMenu.classList.toggle('inactive');
}

async function toggleGeneralDeskMenu(){
    var isEmailClose = emailDeskMenu.classList.contains('inactive');
    var isAsideClose = asideDeskMenu.classList.contains('inactive');
    if (!isEmailClose) {
        emailDeskMenu.classList.add('inactive')
    }
    if (!isAsideClose) {
        asideDeskMenu.classList.add('inactive')
    }

    generalDeskMenu.classList.toggle('inactive');
}