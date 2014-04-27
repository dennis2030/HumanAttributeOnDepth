function process(colorDir, depthDir)

    addpath(genpath('~/research/depth_attribute/HOGgles/ihog-master/'));
    inputFiles = dir([colorDir '/*.jpg']);
    head_size = [0,0];
    torso_size = [0,0];
    leftArm_size = [0,0];
    rightArm_size = [0,0];

    head_fid = fopen('head.feat','w');
    torso_fid = fopen('torso.feat','w');
    leftArm_fid = fopen('leftArm.feat','w');
    rightArm_fid = fopen('rightArm.feat', 'w');

    for i=1:numel(inputFiles)
        tmp_list = regexp(inputFiles(i).name, '/', 'split');
        fname = tmp_list{numel(tmp_list)};
        tmp_list2 = regexp(fname, '\.', 'split');
        prefix = tmp_list2{1}

        depthPath = [depthDir '/' prefix '.txt']
        [cropped_head, cropped_torso, cropped_leftArm, cropped_rightArm] = extractBody(depthPath);
        
        if(size(cropped_head, 1) < 10)
            continue;
        end
        if(size(cropped_head, 2) < 10)
            continue;
        end

        tmp_head = imresize(cropped_head, [35, 55]);
        head(:,:,1) = tmp_head;
        head(:,:,2) = tmp_head;
        head(:,:,3) = tmp_head;

        if(size(cropped_torso, 1) < 10)
            continue;
        end
        if(size(cropped_torso, 2) < 10)
            continue;
        end

        tmp_torso = imresize(cropped_torso, [70, 145]);
        torso(:,:,1) = tmp_torso;
        torso(:,:,2) = tmp_torso;
        torso(:,:,3) = tmp_torso;
        
        if(size(cropped_leftArm, 1) < 10)
            continue;
        end
        if(size(cropped_leftArm, 2) < 10)
            continue;
        end

        tmp_leftArm = imresize(cropped_leftArm, [20, 60]);
        leftArm(:,:,1) = tmp_leftArm;
        leftArm(:,:,2) = tmp_leftArm;
        leftArm(:,:,3) = tmp_leftArm;

        if(size(cropped_rightArm,1) < 10)
            continue;
        end
        if(size(cropped_rightArm,2) < 10)
            continue;
        end
        tmp_rightArm = imresize(cropped_rightArm, [20, 60]);
        rightArm(:,:,1) = tmp_rightArm;
        rightArm(:,:,2) = tmp_rightArm;
        rightArm(:,:,3) = tmp_rightArm;

        head_feat = features(head, 8);
        fprintf(head_fid, '%s',prefix);
        for i=1:numel(head_feat)
            fprintf(head_fid, ' %f', head_feat(i));
        end 
        fprintf(head_fid, '\n');

        torso_feat = features(torso, 8);
        fprintf(torso_fid, '%s',prefix);
        for i=1:numel(torso_feat)
            fprintf(torso_fid, ' %f', torso_feat(i));
        end 
        fprintf(torso_fid, '\n');

        leftArm_feat = features(leftArm, 8);
        fprintf(leftArm_fid, '%s',prefix);
        for i=1:numel(leftArm_feat)
            fprintf(leftArm_fid, ' %f', leftArm_feat(i));
        end 
        fprintf(leftArm_fid, '\n');

        rightArm_feat = features(rightArm, 8);
        fprintf(rightArm_fid, '%s',prefix);
        for i=1:numel(rightArm_feat)
            fprintf(rightArm_fid, ' %f', rightArm_feat(i));
        end 
        fprintf(rightArm_fid, '\n');

    end
    fclose(torso_fid);
    fclose(leftArm_fid);
    fclose(rightArm_fid);
    fclose(head_fid);
end
