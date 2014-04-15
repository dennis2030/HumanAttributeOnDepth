function im = getDepthImage(rawDepth)


% pre-processing, convert raw depth to range 0~1
rawDepthFilter = rawDepth >= 500;
minD = min(rawDepth(rawDepthFilter))

rawDepthFilter = rawDepth <= minD + 750;
maxD = max(max(rawDepth(rawDepthFilter)))

im = rawDepth - minD;
im = im ./ (maxD-minD);
imFilter = im <= 0;
im(imFilter) = 0;

%fnameList = regexp(inputPath, '\/','split');
%fname = fnameList{numel(fnameList)};
%tmpList = regexp(fname,'\.','split');
%prefix = tmpList{1}

end
