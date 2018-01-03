import pygsheets

gc = pygsheets.authorize(service_file='authentications/email script-ceb8d0fcd170.json',no_cache=True)

# Open spreadsheet and then workseet
sh = gc.open('test')
wks = sh.sheet1
# Select worksheet by id, index, title.
#wks = gc.worksheet_by_title("test")
# Update a cell with value (just to let him know values is updated ;) )
wks.update_cell('A1', "Hey yak")
yr=wks.find("yakak")
row= yr[0].row
c1 = wks.cell('A15')
c1.color = (0,0,1,1)
c1.update()
c1.unlink()
#wks.update_cell('A15', Color= 'blue')
#sa
#wks.update_cell(str(cell_list[0]), "Hey yak")
