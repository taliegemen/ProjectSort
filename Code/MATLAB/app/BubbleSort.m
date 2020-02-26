%% Function Define
function SortedArray = BubbleSort(app.arrayLen,app.randomArray,isWorking,speed)
%% Information
%Ali_Egemen_Tasoren
%Merge_Sort
%05/10/2018
%% Sort
pause('on')
if isWorking == 1
    for i = 1:(app.arrayLen - 1)
        for j = app.arrayLen:-1:(i+1)
            if app.randomArray(j) < app.randomArray((j-1)) && isWorking == 1
                pause(speed)
                Changekey           =   app.randomArray(j)    ;
                app.randomArray(j)      =   app.randomArray(j-1)  ;
                app.randomArray(j-1)    =   Changekey         ;
            end
        end  
    end
end

end