r= [2.3 4.5 1.5 5.4 2.9 3.2];
s= [30 75 20 80 35 40];
c= [100 60];
n= length(r);
v= length(c);
fid = fopen('example.lpt','wt');
fprintf(fid,'max ');
for i=1:n
    fprintf(fid,'+ %f x%d ',r(i),i);
end
fprintf(fid,'\nsubject to\n');
for j=1:v
    for i=1:n
        fprintf(fid,'+ %f y%d_%d ',s(i),i,j);
    end
    fprintf(fid,'<= %f\n',c(j));
end
for i=1:n
    for j=1:v
        fprintf(fid,'+ y%d_%d ',i,j);
    end
    fprintf(fid,'- x%d = 0\n',i);
end
fprintf(fid,'binary\n');
for i=1:n
    fprintf(fid,'x%d ',i);
end
for i=1:n
    for j=1:v
        fprintf(fid,'y%d_%d ',i,j);
    end
end
fprintf(fid,'\nend');
fclose(fid);