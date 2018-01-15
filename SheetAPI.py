import pygsheets


def Updatess(ticket):
    gc = pygsheets.authorize(service_file='authentications/Lyons Email-UpdateSheet Script-bdf97af036f4.json',no_cache=True)

    # Open spreadsheet and then workseet
    sh = gc.open('3D Printing Requests')
    wks = sh[0]
    # Select worksheet by id, index, title.
    #wks = gc.worksheet_by_title("test")
    # Update a cell with value (just to let him know values is updated ;) )
    try:
        findcode = wks.find(ticket)
        row = findcode[0].row


    except IndexError:
        return "Invalid Ticket " + ticket


    wks.update_cell('O'+ str(row), "Y")


    alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        c = wks.cell(alphabet[i]+str(row))
        c.color = (.05,.60,1,.50)
        c.update()
        c.unlink()


    return "updated"
    ##wks.update_cell('A15', Color= 'blue')
    #sa
    #wks.update_cell(str(cell_list[0]), "Hey yak")
if __name__ == "__main__":
    print Updatess("21798")