//X is user file
//Y is tweet file

a=size(X,1);
b=size(Y,1);
n=zeros(a,2);
j=0;p=1;
for i=1:b;
  if p==1;
    n(j,2)=c;
    c=0;
    p=0;
    j+=1;
    n(j,1)=Y(i,1);
  end;
  if Y(i,11)=='api';
    c+=1;
  end;
end;


end;
