function convertToMat(inputDir)

    file_list = dir([inputDir '*_GT.txt']);
    for i=1:numel(file_list)
        fname = [inputDir file_list(i).name];
        tmp_list = regexp(fname,'\.','split');
        prefix = tmp_list{1};
        f = dlmread(fname);
        GT = zeros(size(f));
        size(f)
        for j=1:size(f,1)
            GT(j) = f(j);
        end

        save([prefix '.mat'],'GT');
    end

end
