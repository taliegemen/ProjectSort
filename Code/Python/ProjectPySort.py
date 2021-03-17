#!/usr/bin/env Python3
import PySimpleGUI as sg
import numpy as np
import time


def InsertionSort(Array):
    Delay = 0.001 * (200 - values['sliderSpeed'])
    for j in range(1, len(Array)):
        keyvalue = Array[j]
        i = j - 1
        while i > -1 and Array[i] > keyvalue:
            Array[i + 1] = Array[i]
            i = i - 1
        Array[i + 1] = keyvalue
        time.sleep(Delay)
    return Array


def halfarray(Array):
    half = len(Array) // 2
    return Array[:half], Array[half:]


def MergeSort(Array):
    Delay = 0.001 * (200 - values['sliderSpeed'])
    firsthalf, secondhalf = halfarray(Array)
    firsthalf = InsertionSort(firsthalf)
    secondhalf = InsertionSort(secondhalf)
    firsthalf = np.append(firsthalf, 99999)
    secondhalf = np.append(secondhalf, 99999)
    i = 0
    j = 0
    for operationcounter in range(0, len(Array)):
        if firsthalf[i] <= secondhalf[j]:
            Array[operationcounter] = firsthalf[i]
            i = i + 1
            time.sleep(Delay)
        else:
            Array[operationcounter] = secondhalf[j]
            j = j + 1
            time.sleep(Delay)
    return Array


def BubbleSort(Array):
    Delay = 0.001 * (200 - values['sliderSpeed'])
    for i in range(1, len(Array)):
        for j in range(len(Array) - 1, i - 1, -1):
            time.sleep(Delay)
            if Array[j] < Array[j - 1]:
                Changekey = Array[j]
                Array[j] = Array[j - 1]
                Array[j - 1] = Changekey
    return Array


def QuickSort(Array):
    Delay = 0.001 * (200 - values['sliderSpeed'])
    leftArray = []
    pivotList = []
    rightArray = []
    if len(Array) <= 1:  # Already Sorted if Length is 1
        return Array

    pivot = np.random.choice(Array, 1)
    for i in Array:
        if i < pivot:
            leftArray.append(i)
            time.sleep(Delay)
        elif i > pivot:
            rightArray.append(i)
            time.sleep(Delay)
        else:
            pivotList.append(i)
            time.sleep(Delay)
        leftArray = QuickSort(leftArray)
        rightArray = QuickSort(rightArray)
        return leftArray + pivotList + rightArray


def SiftDown(Array, startValue, end):
    rootValue = startValue
    while True:
        childValue = rootValue * 2 + 1
        if childValue > end:
            break
        if childValue + 1 <= end and Array[childValue] < Array[childValue + 1]:
            childValue += 1
        if Array[rootValue] < Array[childValue]:
            Array[rootValue], Array[childValue] = Array[childValue], Array[rootValue]
            rootValue = childValue
        else:
            break


def HeapSort(Array):
    Delay = 0.001 * (200 - values['sliderSpeed'])
    for startValue in range((len(Array) - 2) // 2, -1, -1):
        SiftDown(Array, startValue, len(Array) - 1)

    for end in range(len(Array) - 1, 0, -1):
        time.sleep(Delay)
        Array[end], Array[0] = Array[0], Array[end]
        SiftDown(Array, 0, end - 1)
    return Array


BAR_WIDTH = 50
BAR_SPACING = 75
EDGE_OFFSET = 3
GRAPH_SIZE = (500,500)
DATA_SIZE = (2000,100)

graph = sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE)

sg.ChangeLookAndFeel('GreenTan')          # ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['Help', 'About...'], ]

layout = [
        [sg.Menu(menu_def, tearoff=True)],
        [sg.Text('Project Sort!', size=(40, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [sg.Text('Ali Egemen Taşören 160403034')],
        [sg.Frame(layout=[
        [sg.Radio('Start', "RADIO1", default=True, size=(10,1)), sg.Radio('Stop', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags'), sg.Button('Insertion'), sg.Button('Bubble'), sg.Button('Merge'), sg.Button('Quick'), sg.Button('Heap'), sg.Button('Quit')],
                [
            sg.Slider(range=(1, 75), default_value=50, size=(10, 20), orientation='vertical',key='sliderMax',font=("Helvetica", 15)),
            sg.Text(' ' * 2),
            sg.Slider(range=(1, 25), default_value=25, size=(10, 20), orientation='vertical',key='sliderLength',font=("Helvetica", 15)),
            sg.Text(' ' * 2),
            sg.Slider(range=(1, 100), default_value=100, size=(10, 20), orientation='vertical', key='sliderSpeed', font=("Helvetica", 15)),
            sg.Text(' ' * 20),
            graph],
            [sg.Text('Array Max', font=("Helvetica", 12), size=(9, 1)),
             sg.Text('Array Length', font=("Helvetica", 12), size=(10, 1)),
             sg.Text('Speed', font=("Helvetica", 12), size=(9, 1))],
        [sg.Text('_'  * 110)],
    ]


window = sg.Window('Project Sort', default_element_size=(40, 1), grab_anywhere=False).Layout(layout)

event, values = window.Read()

# The Event Loop
while True:
    event, values = window.Read()
    if event == 'Quit':
        break
    if event == 'Insertion':
        arrayLen = values['sliderLength']
        arrayMax = values['sliderMax']
        Array = np.random.randint(1, arrayMax, arrayLen)
        for j in range(1, len(Array)):
            keyvalue = Array[j]
            i = j - 1
            while i > -1 and Array[i] > keyvalue:
                Array[i + 1] = Array[i]
                i = i - 1

            Array[i + 1] = keyvalue
        graph.Erase()
        for k in enumerate(Array):
            graph_value = Array[k]
            graph.DrawRectangle(top_left=(k * BAR_SPACING
                + EDGE_OFFSET, graph_value),
                                bottom_right=(k * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0), fill_color='light blue')
            graph.DrawText(text=graph_value, location=(k * BAR_SPACING
                + EDGE_OFFSET + 25, graph_value + 10))
    if event == 'Merge':
        arrayLen = values['sliderLength']
        arrayMax = values['sliderMax']
        Array = np.random.randint(1, arrayMax, arrayLen)
        Array = MergeSort(Array)
        graph.Erase()
        for k in enumerate(Array):
            graph_value = Array[k]
            graph.DrawRectangle(top_left=(k * BAR_SPACING + EDGE_OFFSET, graph_value),
                                bottom_right=(k * BAR_SPACING + EDGE_OFFSET
                                    + BAR_WIDTH, 0), fill_color='light blue')
            graph.DrawText(text=graph_value, location=(k * BAR_SPACING
                + EDGE_OFFSET + 25, graph_value + 10))
    if event == 'Quick':
        arrayLen = values['sliderLength']
        arrayMax = values['sliderMax']
        Array = np.random.randint(1, arrayMax, arrayLen)
        Array = QuickSort(Array)
        graph.Erase()
        for k in enumerate(Array):
            graph_value = Array[k]
            graph.DrawRectangle(top_left=(k * BAR_SPACING + EDGE_OFFSET, graph_value),
                                bottom_right=(k * BAR_SPACING
                                    + EDGE_OFFSET + BAR_WIDTH, 0), fill_color='light blue')
            graph.DrawText(text=graph_value, location=(k * BAR_SPACING
                + EDGE_OFFSET + 25, graph_value + 10))
    if event == 'Heap':
        arrayLen = values['sliderLength']
        arrayMax = values['sliderMax']
        Array = np.random.randint(1, arrayMax, arrayLen)
        Array = HeapSort(Array)
        graph.Erase()
        for k in enumerate(Array):
            graph_value = Array[k]
            graph.DrawRectangle(top_left=(k * BAR_SPACING + EDGE_OFFSET, graph_value),                bottom_right=(k * BAR_SPACING + EDGE_OFFSET
                + BAR_WIDTH, 0), fill_color='light blue')
            graph.DrawText(text=graph_value, location=(k * BAR_SPACING
                + EDGE_OFFSET + 25, graph_value + 10))
    if event == 'Bubble':
        arrayLen = values['sliderLength']
        arrayMax = values['sliderMax']
        Array = np.random.randint(1, arrayMax, arrayLen)
        Array = BubbleSort(Array)
        graph.Erase()
        for k in enumerate(Array):
            graph_value = Array[k]
            graph.DrawRectangle(top_left=(k * BAR_SPACING + EDGE_OFFSET, graph_value),
            bottom_right=(k * BAR_SPACING + EDGE_OFFSET
            + BAR_WIDTH, 0), fill_color='light blue')
            graph.DrawText(text=graph_value, location=(k * BAR_SPACING
            + EDGE_OFFSET + 25, graph_value + 10))




sg.Popup('Sayanora',
        'App will close now...',
        'Thanks for using. -Ali Egemen')
