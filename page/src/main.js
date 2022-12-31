// import axios from "axios";
// const { default: axios } = require("axios");

const api_ax = axios.create({
    baseURL: MAIN_PATH,
    headers: {
        'Content-Type': 'application/json;'
    },
    // params: {
    //     'api-key': API_KEY
    // } //If have an API-KEY
});

/* 
const btn0 = document.querySelector('#btn0');
const btn1 = document.querySelector('#btn1');
const btn2 = document.querySelector('#btn2');
const btn3 = document.querySelector('#btn3');
const btn4 = document.querySelector('#btn4');
const btn5 = document.querySelector('#btn5');
const btn6 = document.querySelector('#btn6');
const btn7 = document.querySelector('#btn7');
const btn8 = document.querySelector('#btn8');
const btn9 = document.querySelector('#btn9');
const btn10 = document.querySelector('#btn10');
*/


const inp_ID = document.querySelector('#number_1');
const inp_Nombre = document.querySelector('#number_2');
const inp_Correo = document.querySelector('#number_3');
const inp_Contra = document.querySelector('#number_4');
const inp_RS = document.querySelector('#number_5');


const newProductsContainer = document.querySelector(".NewProducts-List .items_container");
const bestSellersContainer = document.querySelector(".BestSellers-List .items_container");

/*
btn0.addEventListener('click', createNewUserPrev);
btn1.addEventListener('click', getAllUsersPrev);
btn5.addEventListener('click', getUserIdPrev);
btn6.addEventListener('click', activateUserPrev);
btn7.addEventListener('click', deactivateUserPrev);
btn8.addEventListener('click', updateUserPrev);*/

// btnsubs.addEventListener('click', btn_subs);
// btnmulti.addEventListener('click', btn_multi);
// btndiv.addEventListener('click', btn_div);


async function getProductsPrev() {
    // const response = await fetch(`${MAIN_PATH}${PRODUCTS}${GET_PROD}`);
    const {data} = await api_ax(GET_PROD);
    const response1 = await fetch(`${MAIN_PATH}${GET_PROD}`);
    const data_res = await response1.json();

    const products = data_res

    products.forEach(product => {
        const productContainer = document.createElement('div');
        productContainer.classList.add('item-container');

        const productImageCont = document.createElement('div');
        productImageCont.classList.add('item-image');
        const productImage = document.createElement('img');
        productImage.classList.add('product-image');
        productImage.setAttribute('alt', product.name);
        productImage.setAttribute(
            'src', 
            './src/images/karin.png'
        );
        
        const productData = document.createElement('div');
        productData.classList.add('item-data');
        const productDataSub = document.createElement('div');
        const productNameSub = document.createElement('a');
        productNameSub.innerText = product.name;
        const productPriceSub = document.createElement('p');
        productPriceSub.innerText = `S/ ${product.amount}`;

        productDataSub.appendChild(productNameSub)
        productDataSub.appendChild(productPriceSub)
        productData.appendChild(productDataSub)
        productImageCont.appendChild(productImage)
        productContainer.appendChild(productImageCont)
        productContainer.appendChild(productData)
        newProductsContainer.appendChild(productContainer)


        
    })

    console.log({data})
} 

async function getBestSellersPrev() {
    // const response = await fetch(`${MAIN_PATH}${PRODUCTS}${GET_PROD}`);
    const bestSellerPath = 'best%20seller';
    const pathBestSell = PRODUCT_GEN+PRODUCT_TAG+bestSellerPath;
    const {data} = await api_ax(pathBestSell);
    const response1 = await fetch(`${MAIN_PATH}${GET_PROD}`);
    const data_res = await response1.json();

    const products = data.product

    products.forEach(product => {
        const productContainer = document.createElement('div');
        productContainer.classList.add('item-container');

        const productImageCont = document.createElement('div');
        productImageCont.classList.add('item-image');
        const productImage = document.createElement('img');
        productImage.classList.add('product-image');
        productImage.setAttribute('alt', product.name);
        productImage.setAttribute(
            'src', 
            './src/images/karin.png'
        );
        
        const productData = document.createElement('div');
        productData.classList.add('item-data');
        const productDataSub = document.createElement('div');
        const productNameSub = document.createElement('a');
        productNameSub.innerText = product.name;
        const productPriceSub = document.createElement('p');
        productPriceSub.innerText = `S/ ${product.amount}`;

        productDataSub.appendChild(productNameSub)
        productDataSub.appendChild(productPriceSub)
        productData.appendChild(productDataSub)
        productImageCont.appendChild(productImage)
        productContainer.appendChild(productImageCont)
        productContainer.appendChild(productData)
        bestSellersContainer.appendChild(productContainer)
    })
    
    
} 

async function getAllUsersPrev() {
    // const response = await fetch(`${MAIN_PATH}${PRODUCTS}${GET_PROD}`);
    const response1 = await fetch(`${MAIN_PATH}${GET_USERS}`);
    const data = await response1.json();

    const users = data

    console.log({users})
} 

async function createNewUserPrev() {
    // const response = await fetch(`${MAIN_PATH}${PRODUCTS}${GET_PROD}`);
    const userNombre = inp_Nombre.value;
    const userCorreo = inp_Correo.value;
    const userContra = inp_Contra.value;
    const res = await fetch(
        `${MAIN_PATH}${CREATE_USER}`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // 'X-API-KEY': KEY_A,
            },
            body: JSON.stringify({
                "name": `${userNombre}`,
                "email": `${userCorreo}`,
                "password": `${userContra}`
            }),
        }
    )
    const data = await res.json();

    const users = data

    console.log({users})
} 

async function getUserIdPrev() {
    // const response = await fetch(`${MAIN_PATH}${PRODUCTS}${GET_PROD}`);

    // if (userId == Number(userId)){
    //     const res = await fetch(`${MAIN_PATH}${GET_USER_C}${userId}`)
    // }
    const userId = inp_ID.value;
    const res = await fetch(
        `${MAIN_PATH}${GET_USER_C}${userId}`,
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                // 'X-API-KEY': KEY_A,
            },
        }
    )
    const data = await res.json();

    const users = data

    console.log({users})
} 

async function updateUserPrev() {
    // const response = await fetch(`${MAIN_PATH}${PRODUCTS}${GET_PROD}`);
    const userId = inp_ID.value;
    const userNombre = inp_Nombre.value;
    const userCorreo = inp_Correo.value;
    const res = await fetch(
        `${MAIN_PATH}${USER_GEN}${userId}/${UPDATE_USER}`,
        {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                // 'X-API-KEY': KEY_A,
            },
            body: JSON.stringify({
                "id": `${userId}`,
                "name": `${userNombre}`,
                "email": `${userCorreo}`
            }),
        }
    )
    const data = await res.json();

    const users = data

    console.log({users})
} 

async function activateUserPrev() {
    // const response = await fetch(`${MAIN_PATH}${PRODUCTS}${GET_PROD}`);
    const userId = inp_ID.value;
    const res = await fetch(
        `${MAIN_PATH}${USER_GEN}activate?id=${userId}`,
        {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                // 'X-API-KEY': KEY_A,
            },
            body: JSON.stringify({
                "id": `${userId}`,
            }),
        }
    )
    const data = await res.json();

    const users = data

    console.log({users})
} 

async function deactivateUserPrev() {
    // const response = await fetch(`${MAIN_PATH}${PRODUCTS}${GET_PROD}`);
    const userId = inp_ID.value;
    const res = await fetch(
        `${MAIN_PATH}${USER_GEN}deactivate/${userId}`,
        {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                // 'X-API-KEY': KEY_A,
            },
            body: JSON.stringify({
                "id": `${userId}`,
            }),
        }
    )
    const data = await res.json();

    const users = data

    console.log({users})
} 
