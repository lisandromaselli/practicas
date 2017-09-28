clc()
function y = f(x)
    y(1) = x(1)*%e**(x(2))+x(3)-10
    y(2) = x(1)*%e**(2*x(2))+2*x(3)-12
    y(3) = x(1)*%e**(3 * x(2))+3*x(3)-15
endfunction

function y = Newton(f,x,delta)
    J = numderivative(f,x)
    y = x - inv(J)*f(x)
    while norm(y - x,2) > delta
        x = y
        J = numderivative(f,x)
        y = x - inv(J) * f(x)
    end
endfunction

A = Newton(f,[6 0.1 2.7]',0.00000001)
disp(A)
deff('y = g(x)','y = A(1)*%e**(x*A(2))+A(3)*x - 500')
B = Newton(g,1,0.000001)
disp(B)
