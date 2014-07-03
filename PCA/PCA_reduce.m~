% some observation about dim:
% torso dim=300 reaches about 0.95
% head dim=100 reaches about 0.95
% leftArm dim=50 reaches about 0.95
% rightArm dim=50 reaches about 0.94

function PCA_reduce(filename,dim)

tmp_list = regexp(filename,'\/','split');
fname = tmp_list{length(tmp_list)};
tmp_list2 = regexp(fname,'\.','split');
prefix = tmp_list2{1};
inputName = [prefix '.mat']


load (inputName);

sum(eigenvalue(1:dim))/sum(eigenvalue)

transMatrix = eigenVector(:,1:dim);
matrix = matrix * transMatrix;

dlmwrite([prefix '.pca'],matrix);

end
