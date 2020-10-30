
import tkinter as tk
import pickle

def on_keyrelease(event):
    
    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()
    
    # get data from test_list
    if value == '':
        data = test_list
    else:
        data = []
        for item in test_list:
            if value in item.lower():
                data.append(item)                

    # update data in listbox
    listbox_update(data)
    
    
def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')
    
    # sorting data 
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)


def on_select(event):
    # display element selected on list
    print('(event) previous:', event.widget.get('active'))
    print('(event)  current:', event.widget.get(event.widget.curselection()))
    print('---')


# --- main ---
pickle_in = open("tickers.pickle","rb")
example_dict = pickle.load(pickle_in)

test_list = example_dict

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()
entry.bind('<KeyRelease>', on_keyrelease)

listbox = tk.Listbox(root)
listbox.pack()
#listbox.bind('<Double-Button-1>', on_select)
listbox.bind('<<ListboxSelect>>', on_select)
listbox_update(test_list)

root.mainloop()