import pygsheets

gc = pygsheets.authorize(service_file='authentications/email script-ceb8d0fcd170.json',no_cache=True)

# Open spreadsheet and then workseet
sh = gc.open('test')
wks = sh[0]
# Select worksheet by id, index, title.
#wks = gc.worksheet_by_title("test")
# Update a cell with value (just to let him know values is updated ;) )
findcode = wks.find("22032")
row= findcode[0].row
wks.update_cell('O'+ str(2), "Y")


alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26):
    c = wks.cell(alphabet[i]+str(row))
    c.color = (.05,.60,1,.1)
c1 = wks.cell('A15')

c1.color = (1,0,1,1)
c1.update()
c1.unlink()
##wks.update_cell('A15', Color= 'blue')
#sa
#wks.update_cell(str(cell_list[0]), "Hey yak")
