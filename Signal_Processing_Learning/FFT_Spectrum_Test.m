fs = 100;
dt = 1 / fs;
f1 = 20;
f2 = 5;
f3 = 7;
amp1 = 4;
amp2 = 12;
amp3 = 2;

N = 5000;
t = 0:dt:N-dt;

signal = amp1*cos(2*pi*f1*t) + amp2*cos(2*pi*f2*t)+ amp3*cos(2*pi*f3*t) + 2;
fft_signal = fft(signal,N) / N;
fft_amp = abs(fft_signal);

df = fs / N;
faxis1 = linspace(-fs/2,fs/2,N);
faxis2 = linspace(0,fs,N);
figure();
plot(faxis1, fftshift(fft_amp));
figure();
plot(faxis2, fft_amp);
xticks([-100:2:100]);