function[n]=num(X)


a=size(X,1);
b=size(X,2);
n=zeros(a,1);
for i=1:a;
c=-1;
for j=1:b;
if X(i,j)==0;
break
end
c+=1;
end
n(i,1)=c;
end;

end;
 