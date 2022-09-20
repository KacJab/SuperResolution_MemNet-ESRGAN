folder2 = uigetdir;
% myfiles = dir(fullfile(myDir, '*.bmp')); 
% dirmat = uigetdir
% for k = 1:length(myfiles)
%     
%     im = imread(strcat(myDir,'\', myfiles(k).name));
%     filename = split(myfiles(k).name, '.');
%     path = strcat(dirmat,'\',filename(1), '.mat');
%     save(sprintf(path), sprintf('im')
%     filepaths = dir(fullfile(folder,'*.bmp'));
% end
scale = 4
filepaths = dir(fullfile(folder, '*.jpg')); 

% im = imread('C:\studia\semestr2\trueML\SRcomparisonML\algo_implementations\MemNet-master\data\SuperResolution\original_dataset_bmp\bKyYbyS.bmp')
for i = 1 : length(filepaths)        
    fullfile(folder,filepaths(i).name)
    im_gt = imread(fullfile(folder,filepaths(i).name));
    im_gt = modcrop(im_gt, scale);
    im_gt = double(im_gt);
    im_gt_ycbcr = rgb2ycbcr(im_gt / 255.0);
    im_gt_y = im_gt_ycbcr(:,:,1) * 255.0;
    im_l_ycbcr = imresize(im_gt_ycbcr, 1/scale, 'bicubic');
    im_b_ycbcr = imresize(im_l_ycbcr, scale, 'bicubic');
    im_l_y = im_l_ycbcr(:,:,1) * 255.0;
    im_l = ycbcr2rgb(im_l_ycbcr) * 255.0;
    im_b_y = im_b_ycbcr(:,:,1) * 255.0;
    im_b = ycbcr2rgb(im_b_ycbcr) * 255.0;
    filenamek = split(filepaths(i).name, '.');
    filename = folder2
    filename = strcat(filename,'\',filenamek(1),'.mat')
    filename = string(filename)
    save(filename, 'im_gt_y', 'im_b_y', 'im_gt', 'im_b', 'im_l_ycbcr', 'im_l_y', 'im_l');
end