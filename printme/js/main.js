var date = new Date();
console.log(date);
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
    $('#messages').fadeOut('slow');
},3000);