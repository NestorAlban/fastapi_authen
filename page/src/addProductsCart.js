
var i = 1;
var itemCont;
var itemImageCont;
var itemImage;
var itemData;
var itemDataName;
var itemDataPrice;
var cartCont;

mainPageBody.addEventListener('click', (e) => {
    cartCont = document.querySelector('.user-cart .cart-cont')

    const eTarget = e.target
    console.log(eTarget);
    
    const classEvent = e.target.getAttributeNode('class').value;
    console.log(classEvent);

    if (classEvent == 'add-products'){
        console.log('1')
        itemData = eTarget.parentElement;
        console.log(itemData);
        itemCont = itemData.parentElement;
        console.log(itemCont);
        itemImageCont = itemCont.children[0];
        console.log(itemImageCont);
        itemImage = itemImageCont.children[0];
        console.log(itemImage);
        console.log(itemImage.getAttributeNode('src').value); //Image
        itemDataName = itemData.children[0].children[0];
        itemDataPrice = itemData.children[0].children[1];
        console.log(itemDataName);
        console.log(itemDataPrice);

        createAddedCartItem();

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

async function createAddedCartItem(){
    const cartItem = document.createElement('div');
    cartItem.classList.add('cart-item');

    const cartItemImgCont = document.createElement('div');
    cartItemImgCont.classList.add('cart-item_img_cont');

    const cartItemImage = document.createElement('img');
    cartItemImage.classList.add('cart-item_img');
    cartItemImage.setAttribute('alt', itemDataName);
    cartItemImage.setAttribute(
        'src', 
        itemImage.getAttributeNode('src').value
    );

    const cartItemName = document.createElement('p');
    cartItemName.innerText = itemDataName.innerText;

    const cartItemPrice = document.createElement('p');
    cartItemPrice.innerText = itemDataPrice.innerText;

    const cartItemEliminate = document.createElement('img');
    cartItemEliminate.classList.add('cart-item_eliminate');
    cartItemEliminate.setAttribute('alt', 'eliminate_item');
    cartItemEliminate.setAttribute(
        'src', 
        './src/images/close_icon.svg'
    );

    cartItemImgCont.appendChild(cartItemImage)
    cartItem.appendChild(cartItemImgCont)
    cartItem.appendChild(cartItemName)
    cartItem.appendChild(cartItemPrice)
    cartItem.appendChild(cartItemEliminate)
    cartCont.appendChild(cartItem)
}
