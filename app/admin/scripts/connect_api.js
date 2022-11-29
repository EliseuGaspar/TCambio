let ul = document.querySelector('.ul_master')
let data = document.querySelector('.data')

function Subscreve(dicionario){
    let dic = JSON.parse(dicionario);
    console.log(dic)
    let tamanho = parseInt(dic.Tamanho)
    data.innerHTML = dic['Data']
    for (let index = 0; index < tamanho; index++){
        ul.innerHTML += `\
        <ul>\
            <li>${dic[index].Moeda}</li>\
            <li>${dic[index].Compra}</li>\
            <li>${dic[index].Venda}</li>\
        </ul>\
        `
    }
    
}

function Cambios(bank){
	if (bank == 'BMA'){
		let request = new XMLHttpRequest()
		request.open('GET','http://127.0.0.1:1000/',true)
		
        console.log(request.responseText)
		return request.responseText
	} else if (bank == 'BNI'){
		let request = new XMLHttpRequest()
		request.open('GET','http://localhost:1000/tcambio/BNI')
		request.send()
		return request.responseText
	} else {
		let request = new XMLHttpRequest()
		request.open('GET','http://localhost:1000/tcambio/BAI')
		request.send()
		return request.responseText
	}
}

/*

[FREE] Russ Millions X Tion Wayne Type beat | UK Drill Type Beat 2022 | (Prod. Sosa x BS Beats)

*/