function [c,Array] = partition2(Array,p,q,app,event)
    x=Array(p);
    i=p;
    for j=p+1:q
        
        if Array(j)<=x
            i=i+1;
            key=Array(i);
            Array(i)=Array(j);
            Array(j)=key;
            bar(app.UIAxes, Array)
            drawnow update
            pause(app.projectSpeed)
        end
    end
    key=Array(p);
    Array(p)=Array(i);
    Array(i)=key ;
    c=i;
end

