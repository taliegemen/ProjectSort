function array = merge(array,low,middle,high,app,~)
pause('on')
size1 = middle - low + 1;
size2 = high - middle;
left = zeros(1,size1+1);
right = zeros(1,size2+1);
for i=1:size1
    left(i) = array(low+i-1);
end
for j=1:size2
    right(j) = array(middle+j);
end
left(size1+1) = inf;
right(size2+1) = inf;
i = 1;
j = 1;
for k=low:high
    if app.isWorking == 1
        pause(app.projectSpeed)
        if left(i)<= right(j)
            array(k) = left(i);
            i = i + 1;
            bar(app.UIAxes, array)
            drawnow update
        else
            array(k) = right(j);
            j = j + 1;
            bar(app.UIAxes, array)
            drawnow update
        end
    else
        app.randomArray = array;
        break
    end
end
end