let items=[
{name:"Sample User",type:"Laptop",status:"Active"},
{name:"Demo User",type:"Mobile",status:"Active"}
];
function render(d=items){
tbl.innerHTML="";
d.forEach((x,i)=>tbl.innerHTML+=`<tr><td>${x.name}</td><td>${x.type}</td><td>${x.status}</td><td><button class='remove' onclick='delItem(${i})'>Remove</button></td></tr>`);
}
render();
function addItem(){
if(!name.value.trim()){alert("Enter product name");return;}
items.push({name:name.value,type:type.value,status:"Active"});
name.value="";
render();
}
function delItem(i){items.splice(i,1);render();}
function searchItem(){
let q=search.value.toLowerCase();
render(items.filter(x=>x.name.toLowerCase().includes(q)||x.type.toLowerCase().includes(q)));
}