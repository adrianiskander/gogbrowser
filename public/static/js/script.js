'use strict';


function toggleElementDisplay(selector) {

  let elem = document.querySelector(selector);

  elem.classList.contains('d-none')
    ? elem.classList.remove('d-none')
    : elem.classList.add('d-none');
};
