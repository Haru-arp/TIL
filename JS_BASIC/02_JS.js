const plusBtn = document.querySelector('#plusBtn')
const minusBtn = document.querySelector('#minusBtn')
const number = document.querySelector('#number')



plusBtn.addEventListener('click', function() {
  number.innerText ++
})

minusBtn.addEventListener('click', function() {
  number.innerText --
})