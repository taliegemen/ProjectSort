function array = mergeSort(array,low,high,app,event)  
     if(low < high)
       middle = floor((low + high)/2);  
       if app.isWorking == 1
       array = mergeSort(array,low,middle,app,event); 
       else
          app.randomArray = array;
       end
       if app.isWorking == 1    
       array = mergeSort(array,middle + 1, high,app,event);
       else
          app.randomArray = array;
       end
       if app.isWorking == 1
           array = merge(array, low, middle, high,app,event);
       else
          app.randomArray = array; 
       end
       bar(app.UIAxes, array)
       drawnow update
     end          
   end  