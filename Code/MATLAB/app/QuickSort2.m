function Array=QuickSort2(Array,p,r,app,event)
if p<r
    if app.isWorking == 1
    [q,Array]=partition2(Array,p,r,app,event);
    Array=QuickSort2(Array,p,q-1,app,event);
    Array=QuickSort2(Array,q+1,r,app,event);
    else
        return
    end
end
end
         










