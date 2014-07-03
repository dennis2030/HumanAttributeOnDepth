function PCA(filename)


tmp_list = regexp(filename,'\/','split');
fname = tmp_list{length(tmp_list)}
tmp_list2 = regexp(fname,'\.','split');
prefix = tmp_list2{1}

matrix = dlmread(filename,' ',0,1);


[eigenVector,score,eigenvalue,tsquare] = princomp(matrix); 

save([prefix '.mat'],'eigenVector','score','eigenvalue','tsquare','matrix');

end
