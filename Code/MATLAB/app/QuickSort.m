function sortedArray = QuickSort(app, event, randomArray)
%Ali_Egemen_Tasoren
%Quick_Sort
%27/10/2018
%% Sorting Starts...
pause ('on')
if numel(randomArray) <= 1 %If the array has 1 element code will give error, so i had to do something...      
    sortedArray = randomArray;
    return
end
%% Take last element out of the array, as pivot.
pivotNumber         = randomArray(end)                                          ;
randomArray(end)    = []                                                        ; 
leftArray = randomArray( randomArray <= pivotNumber );
rightArray = randomArray( randomArray > pivotNumber );
pause(app.projectSpeed)
bar(app.UIAxes, [leftArray pivotNumber rightArray])
drawnow update
%% Our array will be leftArray + pivot + rightArray
sortedArray        = [QuickSort(app, event, leftArray) pivotNumber QuickSort(app, event, rightArray)]  ;
%% The End...
end
