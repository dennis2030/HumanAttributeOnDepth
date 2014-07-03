function process(colorDir, depthDir)

    inputFiles = dir([colorDir '/*.jpg']);
    head_size = [256,256];
    torso_size = [256,256];
    leftArm_size = [256,256];
    rightArm_size = [256,256];

    for i=1:numel(inputFiles)
        inputFiles(i).name
        tmp_list = regexp(inputFiles(i).name, '/', 'split');
        fname = tmp_list{numel(tmp_list)};
        tmp_list2 = regexp(fname, '\.', 'split');
        prefix = tmp_list2{1}
        
        targetDir = './parts';
        [cropped_head, cropped_torso, cropped_leftArm, cropped_rightArm] = extractBody([colorDir '/' inputFiles(i).name]);
        
        % ========================== %
        if(size(cropped_head, 1) < 10)
            continue;
        end
        if(size(cropped_head, 2) < 10)
            continue;
        end

        head = imresize(cropped_head, head_size);
        imwrite(head,[targetDir '/head/' prefix '.jpg']);

        % ========================== %
        if(size(cropped_torso, 1) < 10)
            continue;
        end
        if(size(cropped_torso, 2) < 10)
            continue;
        end

        torso = imresize(cropped_torso, torso_size);
        imwrite(torso,[targetDir '/torso/' prefix '.jpg']);
        % ========================== %
        if(size(cropped_leftArm, 1) < 10)
            continue;
        end
        if(size(cropped_leftArm, 2) < 10)
            continue;
        end

        leftArm = imresize(cropped_leftArm, leftArm_size);
        imwrite(leftArm,[targetDir '/leftArm/' prefix '.jpg']);

        % ========================== %
        if(size(cropped_rightArm,1) < 10)
            continue;
        end
        if(size(cropped_rightArm,2) < 10)
            continue;
        end
        rightArm = imresize(cropped_rightArm, rightArm_size);
        imwrite(rightArm,[targetDir '/rightArm/' prefix '.jpg']);

        % ========================== %

    end
end
