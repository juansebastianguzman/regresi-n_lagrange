%% Ventaja Mecanica de un Mecanismo de Manivela Biela y Corredera
% Desarrollado a partir de trabajo virtual
% 
% Mecanismos
% 
% Universidad Autonoma de Manizales - 2017

clc, clear, close all
%% Parametros

teta = 0:pi/18:pi;
xi = 1.01:.5:5.01;
r = 1;

%% Evaluacion de la ventaja mecanica (del inverso de)
% $$\frac{ds}{d\theta}=-r\sin\theta+\frac{r^2\sin\theta\cos\theta}{\xi^2r^2-r^2\sin^2\theta}$$

[Teta,Xi] = meshgrid(teta,xi);
dsdteta = abs(-r*sin(Teta) + r^2*sin(Teta).*cos(Teta)./(Xi.^2*r^2 - r^2*sin(Teta).^2).^(1/2));
%% Salidas graficas

figure('visible','on')
surf(Teta,Xi,dsdteta)
xlabel('\theta'), ylabel('\xi'),zlabel('ds/d\theta')