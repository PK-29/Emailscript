import pygsheets


def Updatess(ticket):
    gc = pygsheets.authorize(service_file='Lyons Email-UpdateSheet Script-bdf97af036f4.json',no_cache=True)

    # Open spreadsheet and then workseet
    sh = gc.open('test')
    wks = sh[0]
    # Select worksheet by id, index, title.
    #wks = gc.worksheet_by_title("test")
    # Update a cell with value (just to let him know values is updated ;) )
    findcode = wks.find(ticket)
    row= findcode[0].row
    wks.update_cell('O'+ str(2), "Y")


    alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        c = wks.cell(alphabet[i]+str(row))
        c.color = (.05,.60,1,.50)
    c1 = wks.cell('A15')

    c1.color = (1,0,1,1)
    c1.update()
    c1.unlink()
    return "updating"
    ##wks.update_cell('A15', Color= 'blue')
    #sa
    #wks.update_cell(str(cell_list[0]), "Hey yak")
