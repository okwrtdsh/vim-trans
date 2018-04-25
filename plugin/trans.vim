if exists("g:loaded_vim_trans")
  finish
endif
let g:loaded_vim_trans = 1

let s:save_cpo = &cpo
set cpo&vim

command! -nargs=1 TransEn2Ja call trans#en2ja(<f-args>)
command! -nargs=1 TransJa2En call trans#ja2en(<f-args>)

let &cpo = s:save_cpo
unlet s:save_cpo
