let btn_navbar = document.getElementById("btn_navbar")
let btn_search = document.getElementById("btn_search")
let btn_cadastro = document.getElementById("btn_cadastro")
let btn_cambio = document.getElementById("btn_cambio")
let btn_conversor = document.getElementById("btn_conversor")
let btn_backhome = document.querySelector(".logo h2")

let navbar = document.getElementById("navbar")
let search_body = document.getElementById("search")
let cadastro_body = document.getElementById("cadastro")
let cambio_body = document.getElementById("cambio")
let conversor_body = document.getElementById("conversor")
let select = document.getElementById('cambio_select')

let btn_backhome_


btn_navbar.addEventListener('click',()=>{
    if(navbar.classList != 'active'){
        navbar.classList.add('active')
    } else {
        navbar.classList.remove('active')
    }
})

btn_search.addEventListener('click',()=>{
    if(search_body.classList != 'active'){
        if(cadastro_body.classList == 'active'){
            cadastro_body.classList.remove('active')
            search_body.classList.add('active')
        } else {
            search_body.classList.add('active')
        }
    } else {
        search_body.classList.remove('active')
    }
})

btn_cadastro.addEventListener('click',()=>{
    if(cadastro_body.classList != 'active'){
        if(search_body.classList == 'active'){
            search_body.classList.remove('active')
            cadastro_body.classList.add('active')
        } else {
            cadastro_body.classList.add('active')
        }
    } else {
        cadastro_body.classList.remove('active')
    }
})

btn_cambio.addEventListener('click',()=>{
    cambio_body.classList.add('active')
    if(cambio_body.classList == 'active'){
        btn_backhome.classList.add('active')
        btn_backhome_ = document.querySelector(".logo h2.active")
        let resposta = Cambios('BMA')
        Subscreve(resposta)
    } else {
        null
    }
})

btn_conversor.addEventListener('click',()=>{
    conversor_body.classList.add('active')
    if(conversor_body.classList == 'active'){
        btn_backhome.classList.add('active')
        btn_backhome_ = document.querySelector(".logo h2.active")
    } else {
        null
    }
})

btn_backhome.addEventListener('click',()=>{
    if(conversor_body.classList == 'active'){
        conversor_body.classList.remove('active')
        btn_backhome.classList.remove('active')
    } else if (cambio_body.classList == 'active'){
        cambio_body.classList.remove('active')
        btn_backhome.classList.remove('active')
    }
})

select.addEventListener('change',()=>{
    document.querySelector('.banco').innerHTML = select.value
    alert('Chegou')
    let resposta = Cambios(select.value)
    Subscreve(resposta)
})