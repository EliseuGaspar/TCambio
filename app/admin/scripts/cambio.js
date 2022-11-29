let request = new XMLHttpRequest()
request.open('GET','http://localhost:1000/tcambio/BMA',false)
alert('BMA request')
console.log(JSON.parse(request.responseText))

