function [Y]=rr(X) 
  Y=zeros(0,0);
  a=0;
  c=0;
  b=0;
  j=0;
  for i=1:size(X,1);
    if X(i,2)!=a && j!=0;
      Y=[Y;a,b,c];
      a=X(i,2);
      b=0;
      c=0;
      j=j+1;
    end
    if X(i,2)!=a && j==0;
      a=X(i,2);
      j+=1;
    end
      b+=1;
    if X(i,14)==1;
      c+=1;
    end
  end
end
