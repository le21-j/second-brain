%% Lab5_Q5.m
load Cardioid_AzimuthPlot.txt
azimuth = Cardioid_AzimuthPlot(:,1);  % azimuth angle
Pn_EZNEC = Cardioid_AzimuthPlot(:,2) - Cardioid_AzimuthPlot(1,2); % normalized power pattern for V-pol
%% compute ideal pattern and generate plots
Pn_ideal = 10*log10(cos(pi/4*(cosd(azimuth)-1)).^2);
plot(azimuth,Pn_EZNEC,azimuth,Pn_ideal)
axis([0 360 -60 0])
xlabel('\phi (deg)')
ylabel('P_n')
grid
legend('EZNEC','Ideal','best')
title('Azimuth Pattern for Cardioid Array')



