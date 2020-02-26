function sortedArray = CountSort(app, ~)
%% Counting Sort
% Ali Egemen Tasoren
% 30/10/2018
pause('on')
arrayBiggest = max(app.randomArray);
thirdArray = zeros(1,arrayBiggest);
for j = 1:app.arrayLen
    thirdArray(app.randomArray(j)) = thirdArray(app.randomArray(j)) + 1;
end
for i = 2:arrayBiggest
    thirdArray(i) = thirdArray(i) + thirdArray(i-1);
end
for j = app.arrayLen:-1:1
    if app.isWorking == 1
    pause(app.projectSpeed)
    sortedArray(thirdArray(app.randomArray(j))) = app.randomArray(j);
    bar(app.UIAxes, sortedArray)
    drawnow update
    thirdArray(app.randomArray(j)) = thirdArray(app.randomArray(j)) - 1;
    else
        sortedArray = app.randomArray;
        break
    end
end
bar(app.UIAxes, sortedArray)
drawnow update
end
