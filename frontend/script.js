async function predict(){

let air = document.getElementById("air_temp").value
let process = document.getElementById("process_temp").value
let rpm = document.getElementById("rpm").value
let torque = document.getElementById("torque").value
let wear = document.getElementById("wear").value

let response = await fetch("/api/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

air_temp:air,
process_temp:process,
rpm:rpm,
torque:torque,
wear:wear

})

})

let data = await response.json()

document.getElementById("status").innerText = data.prediction

}
