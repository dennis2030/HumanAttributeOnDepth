function faceFilter(inputPath)

    load 'face-release1.0-basic/face_p146_small.mat';
    im = imread(inputPath);
    bs = detect(im, model, model.thresh);
    bs = clipboxes(im, bs);
    bs = nms_face(bs,0.3);
    dettime = toc;
    numel(bs)
    bs
    figure, showboxes(im, bs), title('all detections');
end
