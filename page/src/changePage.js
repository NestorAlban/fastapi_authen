
var i = 1;
// var emailNav;
// var asideNav0;
// var asideNav1;
// var asideNav2;
// var generalNav0;
// var generalNav1;
// var generalNav2;
// var emailDeskMenu;
// var asideDeskMenu;
// var generalDeskMenu;
// var isEmailClose;
// var isAsideClose;
// var isGeneralClose;

mainPageBody.addEventListener('click', (e) => {
    const eTarget = e.target
    console.log(eTarget);
    
    const classEvent = e.target.getAttributeNode('class').value;
    console.log(classEvent);

    if (classEvent == 'item-container'){
        console.log('1')
    } else if (classEvent == 'item-image'){
        console.log('2')
    } else if (classEvent == 'product-image'){
        console.log('3')
    } else if (classEvent == 'item-data'){
        console.log('4')
    } else if (classEvent == 'item-image'){
        console.log('5')
    } 
    // if (i == 1) {
    //     console.log(i)
    //     emailDeskMenu = document.querySelector('.user-menu');
    //     emailNav = document.querySelector('.navbar-email');
        
    //     asideDeskMenu = document.querySelector('.user-cart');
    //     asideNav0 = document.querySelector('.navbar-shopping-cart');
    //     asideNav1 = document.querySelector('.shopping_cart');
    //     asideNav2 = document.querySelector('.shopping_cart_amount');

    //     generalDeskMenu = document.querySelector('.desk-menu');
    //     generalNav0 = document.querySelector('img.menu');
    //     generalNav1 = document.querySelector('span.header_desk_menu-text');
    //     generalNav2 = document.querySelector('.header_desk_menu');

    //     i+=1

    // }
    // if (classEvent) {
    //     if (eTarget == emailNav) {
    //         toggleEmailDeskMenu()
    //     }
    //     if (eTarget == asideNav0 || eTarget == asideNav1 || eTarget == asideNav2) {
    //         toggleAsideDeskMenu()
    //     }
    //     if ( eTarget == generalNav1 || eTarget == generalNav0 || eTarget == generalNav2) {
    //         toggleGeneralDeskMenu()
    //     }

    // }
});