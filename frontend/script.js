document.querySelectorAll("input").forEach(slider=>{

slider.oninput=function(){

document.getElementById(this.id+"_value").innerText=this.value

}

})

async function predict(){

let air=document.getElementById("air_temp").value
let process=document.getElementById("process_temp").value
let rpm=document.getElementById("rpm").value
let torque=document.getElementById("torque").value
let wear=document.getElementById("wear").value

let response=await fetch("https://factoryguard-ai-5slb.onrender.com",{

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

let data=await response.json()

document.getElementById("status").innerText=data.prediction

let meter=document.getElementById("meter-fill")

let health=document.getElementById("health-text")

if(data.prediction.includes("Failure")){

meter.style.width="90%"
health.innerText="Machine Health: Critical"

}else{

meter.style.width="30%"
health.innerText="Machine Health: Stable"

}

}

particlesJS.load('particles-js','https://cdn.jsdelivr.net/gh/VincentGarreau/particles.js/particles.json')
