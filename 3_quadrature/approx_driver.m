clear all
format long

N = 6;
exps = 1:N;
myeps = 10.^-exps;

myint = zeros(size(myeps));
for i=1:N
  myint(i) = approx_integral(myeps(i));
end

err = sqrt(myeps).*myint-pi/2;

figure(1);clf;
plot(myeps,abs(err),'LineWidth',2);
  xlabel('\epsilon'); ylabel('error');
set(gca, 'fontsize', 18);

figure(2);clf;
loglog(myeps,abs(err),'LineWidth',2);
  xlabel('\epsilon'); ylabel('error');
set(gca, 'fontsize', 18);

function I = approx_integral(myeps)

myfun = @(x) 1./(myeps+x.^2);
I = quad(myfun,0,1);

end