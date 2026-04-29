%% Lab5_Q4.m
load HWD2_ElevationPlot.txt
elevation = HWD2_ElevationPlot(:,1);  % elevation angle
Pn_EZNEC = HWD2_ElevationPlot(:,2) - HWD2_ElevationPlot(1,2); % normalized power pattern for V-pol
%% convert elevation angle to theta
I = cosd(90-elevation);
Q = sind(90-elevation);
theta = atan2(Q,I);
%% sort theta and pattern values so they are in order
[theta1,k] = sort(theta);
Pn_EZNEC1 = Pn_EZNEC(k);
%% compute ideal pattern and generate plots
Pn_ideal = 10*log10(abs(sin(theta1).^3).*cos(pi/2*sin(theta)).^2);
plot(180/pi*theta1,Pn_EZNEC1,180/pi*theta1,Pn_ideal)
axis([-180 180 -60 0])
xlabel('\theta (deg)')
ylabel('P_n')
grid
legend('EZNEC','Ideal','best')
title('Elevation pattern of the two-stacked-element array')


