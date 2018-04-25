let s:save_cpo = &cpo
set cpo&vim

py3file <sfile>:h:h/trans.py
python3 import vim

function! trans#en2ja(words)
  python3 en2ja(vim.eval('a:words'))
endfunction

function! trans#ja2en(words)
  python3 ja2en(vim.eval('a:words'))
endfunction

let &cpo = s:save_cpo
unlet s:save_cpo
