function y = f(x)
    y = sin(x)-x**2/2
endfunction
function y = f1(x)
    y = %e**(-x)-x**4
endfunction
function y = f2(x)
    y = (x - 1)./log(x) - 1 
endfunction
function y = f3(x)
    y = x**2/4 - sin(x)
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

function y = secante(f,x0,x1,tol)
    y = x1 - (x1 - x0)/(f(x1) - f(x0)) * f(x1);
    e = abs(x1 - x0)
    while e > tol
        x0 = x1
        x1 = y
        y = x1 - (x1 - x0)/(f(x1) - f(x0)) * f(x1);
        e = abs(x1 - x0)
    end
endfunction
