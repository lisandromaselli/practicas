function y = f(x)
    y = sin(x)-x**2/2
endfunction
function y = f1(x)
    y = %e**(-x)-x**4
endfunction
function y = f2(x)
    y = (x - 1)./log(x) - 1 
endfunction

function y = biseccion(f,a,b,e)
    if f(a)*f(b)>=0 then
        error('bad range')
    end
    y = (a + b)/2
    while b-y > e then
            if f(y)*f(b) <= 0 then
                a = y 
            else
                b = y
            end
        y = (a + b)/2
    end
endfunction
