let btn_converter = document.getElementById('btn_converter')
let select1 = document.getElementById('moeda1')
let select2 = document.getElementById('moeda2')
let valor_ = document.getElementById('valor')
let resultadobox = document.getElementById('resultado')
let btn_copy = document.querySelector('#bottom button')
let mensageBox = document.getElementById('menssage')
let mensageBox_text = document.querySelector('#menssage .msg')

btn_converter.addEventListener('click',()=>{
    if(select1.value == select2.value){
        resultadobox.innerHTML = `Não é possível converter ${select1.value} para ${select2.value}`
    } else {
        resultadobox.innerHTML = Converter(select1.value,select2.value,valor_.value)
    }
})

resultadobox.addEventListener('click',()=>{
    resultadobox.innerHTML = 'Sem nada ainda'
})

btn_copy.addEventListener('click',()=>{
    copyMenssage()
})

function copyMenssage(){
    let time = setTimeout(()=>{
        mensageBox_text.innerHTML = 'Copiado para a área de transferência.'
        mensageBox.classList.add('active')
        let time2 = setTimeout(()=>{
            mensageBox.classList.remove('active')
        },4000)
    },100)
}

function Converter(M1,M2,V){
    return 123
}