
function homePage() {
    console.log('Home')
    // loadHTML("main-nav", "main-nav.html");

    newProductSection.classList.remove('inactive');
    bestSellerSection.classList.remove('inactive');
    sectDivContainer.classList.remove('inactive');
    newProductsArticleContainer.classList.remove('inactive');
    BestProductsArticleContainer.classList.remove('inactive');

    createNavBarDesk();
    
    getProductsPrev();
    getBestSellersPrev();
    
    // loadHTML("template1", "user-nav.html");
}

function categoriesPage() {
    console.log('Category')

    newProductSection.classList.remove('inactive');
    bestSellerSection.classList.remove('inactive');
    sectDivContainer.classList.remove('inactive');
    newProductsArticleContainer.classList.add('inactive');
    BestProductsArticleContainer.classList.add('inactive');
}

function trendsPage() {
    console.log('Trends')
}

function productDetailsPage() {
    console.log('Product')
}

function searchPage() {
    console.log('Search')
}

function navigator(){
    console.log({location});
    

    if (location.hash.startsWith('#trends')) {
        trendsPage();
    } else if (location.hash.startsWith('#search=')) {
        searchPage();
    } else if (location.hash.startsWith('#product=')) {
        productDetailsPage();
    } else if (location.hash.startsWith('#category=')) {
        categoriesPage();
    } else {
        homePage();
    }
}


window.addEventListener('DOMContentLoaded', navigator, false)
window.addEventListener('hashchange', navigator, false)
