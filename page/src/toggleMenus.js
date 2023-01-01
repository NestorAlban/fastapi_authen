
var i = 1;
var emailNav;
var asideNav0;
var asideNav1;
var asideNav2;
var emailDeskMenu;
var asideDeskMenu;
var isEmailClose;
var isAsideClose;

mainNavBar.addEventListener('click', (e) => {
    const eTarget = e.target
    console.log(eTarget);
    
    const classEvent = e.target.getAttributeNode('class');
    // console.log(classEvent.value);
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
        // console.log(asideNav);
        i+=1
    }
    if (classEvent) {
        if (eTarget == emailNav) {
            // const emailDeskMenu = document.querySelector('.user-menu');
            toggleEmailDeskMenu()
        }
        if (eTarget == asideNav0 || eTarget == asideNav1 || eTarget == asideNav2) {
            // const emailDeskMenu = document.querySelector('.user-menu');
            toggleAsideDeskMenu()
        }
    }
});

async function toggleEmailDeskMenu(){
    var isAsideClose = asideDeskMenu.classList.contains('inactive');
    if (!isAsideClose) {
        asideDeskMenu.classList.add('inactive')
    }  
    
    emailDeskMenu.classList.toggle('inactive');
}

async function toggleAsideDeskMenu(){
    var isEmailClose = emailDeskMenu.classList.contains('inactive');
    if (!isEmailClose) {
        emailDeskMenu.classList.add('inactive')
    }

    asideDeskMenu.classList.toggle('inactive');
}
