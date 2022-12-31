
var i = 1;
var emailNav;
var emailDeskMenu;

mainNavBar.addEventListener('click', (e) => {
    const eTarget = e.target
    // console.log(eTarget);
    
    const classEvent = e.target.getAttributeNode('class');
    // console.log(classEvent.value);
    if (i == 1) {
        console.log(i)
        emailDeskMenu = document.querySelector('.user-menu');
        emailNav = document.querySelector('.navbar-email');
        // console.log(emailNav);
        i+=1
    }
    if (classEvent) {
        if (eTarget == emailNav) {
            // const emailDeskMenu = document.querySelector('.user-menu');
            toggleEmailDeskMenu(emailDeskMenu)

        }
    }
});

async function toggleEmailDeskMenu(item){
    /*
    const isEmailClose = emailDeskMenu.classList.contains('inactive')

    if (!isEmailClose) {
        emailDeskMenu.classList.add('inactive')
    }  
    */
    
    item.classList.toggle('inactive');
}
