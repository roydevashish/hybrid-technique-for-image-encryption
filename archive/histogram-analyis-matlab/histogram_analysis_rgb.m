% Lazaros Moysis
% Youtube channel 
% https://www.youtube.com/@lazarosmoysis5095 
% RG: https://www.researchgate.net/profile/Lazaros-Moysis

% Realevant video
% https://www.youtube.com/watch?v=_mNyanDTDvw

% The SIPI database
% https://sipi.usc.edu/database/


% The following papers can be used as references for chaos based encryption
% https://dergipark.org.tr/en/pub/chaos/issue/54264/756229
% https://link.springer.com/chapter/10.1007/978-3-030-92166-8_7
% https://ieeexplore.ieee.org/abstract/document/9396395


% The following code displays the histograms of a plaintext image, its
% shuffled version, and its encrypted one. 
% The histogram's variance is also computed
% See the references above on
% information for chaos based encryption.

clear
plaintext=imread('original/done/baboon.png');

shuffled=imread('shuffled_rgb.png');

ciphertext=imread('encrypted/woman_darkhair.tif');


% Display Images
figure
subplot(1,3,1)
box on
imshow(plaintext)
title('Plaintext Image')
set(gca,'fontsize',10)
set(gca,'fontweight','bold')
subplot(1,3,2)
imshow(shuffled)
title('Shuffled Image')
set(gca,'fontsize',10)
set(gca,'fontweight','bold')
box on
subplot(1,3,3)
imshow(ciphertext)
title('Encrypted Image')
set(gca,'fontsize',10)
set(gca,'fontweight','bold')
box on

% Display their Histograms
% In the encryption process, we first combine all three channels and then perform
% shuffling and substitution. So the histograms of the shuffled channels
% are not the same to the original ones (in contrast to the grayscale case)


[R,G,B] = imsplit(plaintext);
[Rshuf,Gshuf,Bshuf] = imsplit(shuffled);
[Renc,Genc,Benc] = imsplit(ciphertext);

figure(2)
subplot(3,3,1)
hold all
histogram(R,256,FaceColor="r",EdgeColor="none")
set(gca,'fontsize',10)
set(gca,'fontweight','bold')
title('Plaintext Image (R)')
box on
subplot(3,3,2)
hold all
histogram(G,256,FaceColor="g",EdgeColor="none")
set(gca,'fontsize',10)
set(gca,'fontweight','bold')
title('Plaintext Image (G)')
box on
subplot(3,3,3)
hold all
histogram(B,256,FaceColor="b",EdgeColor="none")
set(gca,'fontsize',10)
set(gca,'fontweight','bold')
box on
title('Plaintext Image (B)')


subplot(3,3,4)
hold all
histogram(Rshuf,256,FaceColor="r",EdgeColor="none")
set(gca,'fontsize',10)
set(gca,'fontweight','bold')
title('Shuffled Image (R)')
box on
subplot(3,3,5)
hold all
histogram(Gshuf,256,FaceColor="g",EdgeColor="none")
set(gca,'fontsize',10)
set(gca,'fontweight','bold')
title('Shuffled Image (G)')
box on
subplot(3,3,6)
hold all
histogram(Bshuf,256,FaceColor="b",EdgeColor="none")
set(gca,'fontsize',10)
set(gca,'fontweight','bold')
box on
title('Shuffled Image (B)')


subplot(3,3,7)
hold all
histogram(Renc,256,FaceColor="r",EdgeColor="none")
set(gca,'fontsize',10)
set(gca,'fontweight','bold')
title('Encrypted Image (R)')
box on
subplot(3,3,8)
hold all
histogram(Genc,256,FaceColor="g",EdgeColor="none")
set(gca,'fontsize',10)
set(gca,'fontweight','bold')
title('Encrypted Image (G)')
box on
subplot(3,3,9)
hold all
histogram(Benc,256,FaceColor="b",EdgeColor="none")
set(gca,'fontsize',10)
set(gca,'fontweight','bold')
box on
title('Encrypted Image (B)')


% compute variance of histograms
counts = imhist(R);
disp('Variance: Plaintext R')
var(counts)

counts = imhist(G);
disp('Variance: Plaintext G')
var(counts)

counts = imhist(B);
disp('Variance: Plaintext B')
var(counts)


counts = imhist(Rshuf);
disp('Variance: Shuffled R')
var(counts)

counts = imhist(Gshuf);
disp('Variance: Shuffled G')
var(counts)

counts = imhist(Bshuf);
disp('Variance: Shuffled B')
var(counts)

counts = imhist(Renc);
disp('Variance: Encrypted R')
var(counts)

counts = imhist(Genc);
disp('Variance: Encrypted G')
var(counts)

counts = imhist(Benc);
disp('Variance: Encrypted B')
var(counts)