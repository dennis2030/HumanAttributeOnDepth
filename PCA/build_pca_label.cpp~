#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "build_pca_label.h"
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;

void sort_label(){
    fstream label_set;
    fstream  feature_data;
    ofstream output;
    vector<string> image_name;
    vector<string> label;
    char* pch;
    char tmp[1000];
    char tmp2[5000];
    int name_index;
    label_set.open("label_set", fstream::in);
    feature_data.open("LFW_Gabor_eyes", fstream::in);
    output.open("label_all", fstream::out);

    while(label_set.getline(tmp,1000)){
        pch = strtok(tmp," ");
        image_name.push_back(pch);
        pch = strtok(NULL,"");
        label.push_back(pch);
    }

    while(feature_data.getline(tmp2,5000)){
        pch = strtok(tmp2," ");
        //check
        for(name_index=0;name_index<image_name.size();name_index++){
            //cout<<pch<<endl;
            if(strcmp(pch,image_name[name_index].c_str()) ==0 ){
                //cout<<name_index<<endl;
                output<<image_name[name_index]<<" "<<label[name_index]<<endl;
                break;
            }
        }
    }
    label_set.close();
    feature_data.close();
    output.close();
}

void fivefold(const char* filename){
    //feature data
    ifstream data_file;
    data_file.open(filename);
    char dir[5000];

    //five fold data
    char temp1[15];
    char fold_data[15][500];			//fold file name
    for(int a=0;a<5;a++){				//ada five fold		//can be changed
		for(int b = 0 ; b<3;b++)        //svm spilt data   //can be changed
		{
			sprintf(temp1,"_%d%d",a+1,b+1);
			strcpy(fold_data[a*3+b],"PCA_fold/");
			strcat(fold_data[a*3+b],filename);
			strcat(fold_data[a*3+b],temp1);
		}
    }

    ofstream ff_data[15];			//create fold file
    for(int b=0;b<15;b++){
		//cout<<fold_data[b]<<endl;
        ff_data[b].open(fold_data[b],ios::trunc);
    }

    //todo fivefold
    int count=1;
    int index = 0;
    while(data_file.getline(dir,5000)){
        index = count%15;
        ff_data[index]<<dir<<endl;
        count++;
      //  cout<<count<<" "<<index<<endl;
    }

    //close file
    for(int b=0;b<15;b++){
        ff_data[b].close();
    }
    data_file.close();

}

void cv_pca(const int ori_attr){
	Mat features;
	int fold = 5;
	string name = "PCA_fold/trainlabel";
	string tmp;
	int line_num;
	for(int z = 0 ; z < fold ; z++){	
		ifstream label;
		stringstream num;
		num << (z+1);
		label.open((name+(num.str())).c_str());
		//cout << name+(num.str()) << endl;
		line_num = linenumber((name+(num.str())).c_str());
		//cout << line_num << endl;
		Mat f(line_num, ori_attr, CV_32F);
		for(int i = 0 ; i < line_num ; i++){
			int k;
			label >> tmp;
			//cout << tmp << endl;
			for(int j = 0 ; j < ori_attr ; j++){
				label >> k;
				f.at<float>(i, j) = k;
			}
		}
		features.push_back(f);
		label.close();
		printf("Start PCA...");
		fflush(stdout);
		PCA pca(features, Mat(), CV_PCA_DATA_AS_ROW);
		printf("Done\n");
		
		Mat eigenval, eigenvec, mean;
		mean = pca.mean.clone();
		eigenval = pca.eigenvalues.clone();
		eigenvec = pca.eigenvectors.clone();
		FileStorage fs1("PCA_fold/mean_Matrix_resize" + num.str(), FileStorage::WRITE);
		fs1 << "mean_Matrix" << mean;
		fs1.release();
		FileStorage fs2("PCA_fold/eigenval_Matrix_resize" + num.str(), FileStorage::WRITE);
		fs2 << "eigenval_Matrix" << eigenval;
		fs2.release();
		FileStorage fs3("PCA_fold/eigenvec_Matrix_resize" + num.str() , FileStorage::WRITE);
		fs3 << "eigenvec_Matrix" << eigenvec;
		fs3.release();	
	}
}

void convert_pca(const int ori_attr, const int dim){
	string val_name = "PCA_fold/eigenval_Matrix_resize";
	string vec_name = "PCA_fold/eigenvec_Matrix_resize";
	string mean_name = "PCA_fold/mean_Matrix_resize";
	int fold = 5;
	for(int z = 0 ; z < fold ; z++){	
		ifstream label;
		ofstream output;
		string tmp;
		string out_name = "label_set";
		int line_num;
		stringstream num;
		num << (z+1);
		label.open("label_all");
		
		Mat eigenval, eigenvec, mean;
		cout<<"Load matrix from file..."<<endl;
        FileStorage fs1(mean_name + num.str(), FileStorage::READ);
		fs1["mean_Matrix"] >> mean;
        fs1.release();
        FileStorage fs2(val_name + num.str(), FileStorage::READ);
		fs2["eigenval_Matrix"] >> eigenval;
        fs2.release();
        FileStorage fs3(vec_name + num.str(), FileStorage::READ);
		fs3["eigenvec_Matrix"] >> eigenvec;		
		fs3.release();			
		cout<<"Read Matrix"<<endl;
		PCA pca;
		pca.mean=mean.clone();
		pca.eigenvalues=eigenval.clone();
		pca.eigenvectors=eigenvec.clone();
		
		line_num = linenumber("label_all");
		cout<<"Line: "<<line_num<<endl;
		Mat f(line_num, ori_attr, CV_32F);
		for(int i = 0 ; i < line_num ; i++){
			int k;
			label >> tmp;
			//cout << tmp << endl;
			for(int j = 0 ; j < ori_attr ; j++){
				label >> k;
				f.at<float>(i, j) = k;
			}
		}
		cout<<"Project..."<<endl;
		Mat result(line_num, ori_attr, CV_32F);
		pca.project(f, result);
		stringstream ss;
		ss<<dim;
		out_name = "../PCA_label/dim" + ss.str() + "/" + out_name + num.str();
		output.open( out_name.c_str() );
		for(int a=0;a<line_num;a++){
			for(int b=0;b<dim;b++){
				if(b != dim-1)
					output<<result.at<float>(a, b)<<" ";
				else
					output<<result.at<float>(a, b);
			}
			output<<endl;
		}
		output.close();
		label.close();
	}
}


int linenumber(const char* filename){
    char dir[5000];
    ifstream data_file;
    data_file.open(filename);
    char c;
    int linenum = 0;
    //count lines
    while(data_file.getline(dir,5000)){
        linenum++;
    }
    data_file.close();
    return linenum;
}
