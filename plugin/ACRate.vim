if exists('g:loaded_acrate')
  finish
endif

let g:loaded_acrate = 1

scriptencoding utf-8

let s:save_cpo = &cpo
set cpo&vim


let s:core = yarp#py3('ACRate')

function g:ACRate#Setting()
  call s:core.notify('GetRate')
endfunction

autocmd VimEnter * call ACRate#Setting()

let &cpo = s:save_cpo
unlet s:save_cpo
