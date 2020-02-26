function SortedArray = InsertionSort(RandomArray)
%Ali_Egemen_Tasoren
%Insertion_sort
%05/10/2018
%% Sorting
for j = 2:length(RandomArray)
    key_number  =   RandomArray(j);
    i           =   j-1           ;
    while (i>0) && (RandomArray(i)>key_number)
        RandomArray(i+1)    =   RandomArray(i)  ;
        i                   =   i-1             ;
    end
    RandomArray(i+1) = key_number;
end
SortedArray = RandomArray;
end

