if !has('python')
  finish
endif

if exists('g:loaded_Multiliner')
  finish
endif

let g:loaded_Multiliner = 1
let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

" Load the python code
exe 'pyfile ' . s:plugin_path . '/multiliner_init.py'

" Maps
nmap <leader>ml :py Multiliner_multiline()<CR>
nmap <leader>uml :py Multiliner_unmultiline()<CR>
