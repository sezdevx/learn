" Hello World
" source %
" press Q
function! HelloWorld()
  let s:a = "Hello"
  let s:b = "World"
  echo s:a . " " . s:b | echo " | "
  echom s:a . " " . s:b . " permanently"
endfunction

command! Hello call HelloWorld()

nnoremap Q :Hello<cr>


