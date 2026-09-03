let data=[{name:"Alex",type:"Economy",status:"Confirmed"},{name:"Priya",type:"Business",status:"Confirmed"}];
function render(d=data){tbl.innerHTML="";d.forEach((x,i)=>tbl.innerHTML+=`<tr><td>${x.name}</td><td>${x.type}</td><td>${x.status}</td><td><button class='cancel' onclick='del(${i})'>Cancel</button></td></tr>`)}
render();
function book(){if(!name.value.trim()){alert("Enter passenger name");return;}data.push({name:name.value,type:type.value,status:"Confirmed"});name.value="";render();}
function del(i){data.splice(i,1);render();}
function findBooking(){let q=search.value.toLowerCase();render(data.filter(x=>x.name.toLowerCase().includes(q)||x.type.toLowerCase().includes(q)));}