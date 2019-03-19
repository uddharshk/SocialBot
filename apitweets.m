//X is user file
//Y is tweet file

a=size(X,1);
b=size(Y,1);
n=zeros(a,2);
j=1;p=1;
n(1,1)=Y(1,2);
for i=1:b;
  if p==1;
    n(j,1)=Y(i,2);
  end;
  if Y(i,2)==n(j,1);
    if Y(i,11)=='api';
      c+=1;
    end;
  else
    n(j,2)=c;
    c=0;
    p=1;
    j+=1;
  end;
end;
