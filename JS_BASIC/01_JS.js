const elem1 = document.querySelector('#list-1')
const elem2 = document.querySelector('#list-2')
const contentElem = document.querySelector('#content')
const listElem = document.querySelector('#list-1')
// const targetElem = elem1.lastElementChild
// console.log(targetElem);

// const budzElem = elem1.children[1]
// console.log(budzElem);

// budzElem.append(targetElem)

//append, prepend, before, after

// const newNode = document.createElement('li')

// //노드 꾸미기
// newNode.textContent = '데스크탑'
// elem1.append(newNode)


//html 속성 다루기
//classList : add, remove, toggle
// elem1.classList.add('WhiteFont')
// elem1.classList.toggle('whiteFont')
// elem1.classList.toggle('whiteFont')

//이벤트 다루기
function myClick(e) {
  console.log('hello')
  console.log(e.target);

}
//노드 .addeventListener(event type==event trigger, handler == event handler)
// elem1.addEventListener('click', function(){
//   console.log('새로운 익명 함수')
// })
// elem1.removeEventListener('click', function(){
//   console.log('새로운 익명 함수')
// }) 
// 익명함수로 핸들러에 적으면 삭제 할 수 없다. 이벤트를 remove 할려면 함수를 선언형으로 선언하고 콜백에 등록해야한다.

contentElem.addEventListener('click', myClick)
listElem.addEventListener('click', function (e) {
  e.stopPropagation()
  myClick(e)
})

