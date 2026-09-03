let books=[
{title:"Python Basics",author:"Guido"},
{title:"HTML & CSS",author:"John"}
];

function render(data=books){
let out="";
data.forEach((b,i)=>{
out+=`<tr><td>${b.title}</td><td>${b.author}</td><td><button class="remove" onclick="removeBook(${i})">Delete</button></td></tr>`;
});
document.getElementById("list").innerHTML=out;
}
render();

function addBook(){
let t=book.value.trim(),a=author.value.trim();
if(!t||!a){alert("Enter both fields");return;}
books.push({title:t,author:a});
book.value="";author.value="";
render();
}

function removeBook(i){
books.splice(i,1);
render();
}

function searchBooks(){
let q=search.value.toLowerCase();
render(books.filter(b=>b.title.toLowerCase().includes(q)||b.author.toLowerCase().includes(q)));
}
