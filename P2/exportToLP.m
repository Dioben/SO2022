function []= exportToLP(nodeCount,linkMatrix,critical,filename)

    fid = fopen(filename,'wt');
    fprintf(fid,'min ');
    for i=1:nodeCount
        for j=i+1:nodeCount
            fprintf(fid,'+ l%d_%d',i,j);
        end
    end
    
    
    fprintf(fid,'\nsubject to\n\\\\only %d can be critical\n',critical);
    for i=1:nodeCount %%enforce critical node count condition
        fprintf(fid,'+ n%d',i);
    end
    fprintf(fid,' = %d\n',critical);
    
    for i= 1:nodeCount-1 
        for j= i+1:nodeCount
            if linkMatrix(i,j)>0 %%map out links we know exist
                fprintf(fid,'\\\\this is a known pair\n+ l%d_%d + n%d + n%d >=1\n',i,j,i,j);
            else %%scope out neighbourhood for possible connections
                fprintf(fid,'\\\\no direct link between %d,%d\n',i,j);
                for k=find(linkMatrix(i,:)>0)
                    fprintf(fid,'+ l%d_%d - l%d_%d - l%d_%d - n%d>= -1\n', i,j,  min(i,k),max(i,k), min(k,j),max(k,j)  ,k );
                end
            end
        end
    end
    
    
    
    fprintf(fid,'binary\n');
    for i=1:nodeCount
        fprintf(fid,'n%d ',i);
    end
    fprintf(fid,'\nend');
    fclose(fid);

end