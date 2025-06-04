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
plaintext=imread('original/barbara.bmp');

shuffled=imread('shuffled.png');

ciphertext=imread('encrypted/barbara.bmp');


% Display Images
figure
subplot(1,3,1)
box on
imshow(plaintext)
title('Plaintext Image')
set(gca,'fontsize',12)
set(gca,'fontweight','bold')
subplot(1,3,2)
imshow(shuffled)
title('Shuffled Image')
set(gca,'fontsize',12)
set(gca,'fontweight','bold')
box on
subplot(1,3,3)
imshow(ciphertext)
title('Encrypted Image')
set(gca,'fontsize',12)
set(gca,'fontweight','bold')
box on

% Display their Histograms
% You will observe that the histogram of the plaintext and shuffled images
% are the same. Does this makes sense? Of course! like shuffling a deck of
% cards, its histogram does not change.

figure(2)
subplot(1,3,1)
hold all
imhist(plaintext)
set(gca,'fontsize',12)
set(gca,'fontweight','bold')
title('Plaintext Image')
box on
subplot(1,3,2)
hold all
imhist(shuffled)
set(gca,'fontsize',12)
set(gca,'fontweight','bold')
title('Shuffled Image')
box on
subplot(1,3,3)
hold all
imhist(ciphertext)
set(gca,'fontsize',12)
set(gca,'fontweight','bold')
box on
title('Encrypted Image')



% compute variance of histograms
counts = imhist(plaintext);
plaintext_var=var(counts)

counts = imhist(shuffled);
plaintext_var=var(counts)

counts = imhist(ciphertext);
ciphertext_var=var(counts)
