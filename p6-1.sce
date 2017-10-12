clc()
//1 - a)
//    Sea Ax = b el sistema lineal a resolver, el metodo de jacobi
//    separa A = N + A* con D diagonal
//    Luego, por el corolario el metodo converge sii r(I-N^(-1)A) < 1
        A = [1 -1 -1;1 -1 2;0 2 4]
        D = diag([1 -1 4])        
        a = max(abs(spec(I-D^-1 * A)))
        disp(a)
//      luego para el primer caso converge
        A = [1 -1 0;-1 2 -1;0 -1 1.1]
        D = diag([1 2 1.1])
        a = max(abs(spec(I-D^-1 * A)))
        disp(a)
//      luego no converge para los 2 casos
//1 - b)
        I = eye(3,3)
        A = [1 -1 -1;1 -1 2;0 2 4]
        D = tril(A)
        a = max(abs(spec(I-D^-1 * A)))
        disp(a)
        A = [1 -1 0;-1 2 -1;0 -1 1.1]
        D = tril(A)
        a = max(abs(spec(I-D^-1 * A)))
        disp(a)
//        el metodo converge para los 2 sistemas

function x = jacobi(A,b,x0,delta)
    n = size(A)
    if  n(1)<>n(2) then  error('bad matrix'); end
    for i = 1:n(1)
            suma =  0
            for j = 1:n(1)
                if  j <> i then
                    suma = suma + A(i,j) * x0(j);
                end
            end
            x(i) = (b(i) - suma)/A(i,i)
        end
    while (norm(x-x0,2) > delta )
        x0 = x
        for i = 1:n(1)
            suma =  0
            for j = 1:n(1)
                if  j <> i then
                    suma = suma + A(i,j) * x0(j);
                end
            end
            x(i) = (b(i) - suma)/A(i,i)
        end
    end
endfunction

function x = gauss_s(A,b,x0,delta)
endfunction

A = [1 -1 -1;1 -1 2;0 2 4]
b = [0.375,0,0]'
x = jacobi(A,b,[0 0 0]',1e-12)
disp(x)

A = [1 -1 0;-1 2 -1;0 -1 1.1]
b = [0 1 0]'
x = jacobi(A,b,[0 0 0]',1e-12)
disp(x)
disp(A*x)
