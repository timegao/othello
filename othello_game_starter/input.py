class Input:

    @staticmethod
    def input_score(name=''):
        '''Java InputDialogue Box to enter name'''
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, name)

    @staticmethod
    def read_write(name, score):
        '''Reads file and writes score'''
        with open("scores.txt", 'a+') as data:
            data.seek(0, 0)  # moves read back to front
            line0 = data.readline()  # read firstline
            data.seek(0, 0)  # moves read back to front
            save = data.read()  # creates save file
            old_score = int(line0.split(',')[1]) if line0 != "" else 0
        with open("scores.txt", 'w') as file:
            if score >= old_score:  # if same or higher score
                file.write(name + ',' + str(score) + "\n")
                file.write(save)  # append save file
            else:  # if lower score
                file.write(save)  # append save file
                file.write(name + ',' + str(score) + "\n")

    @staticmethod
    def end_prompt(score1, score2):
        '''Prompts user for name and calls read_write()'''
        s = ""
        if score1 > score2:
            s = "Player one won!\n" + "Enter your name:"
        elif score1 < score2:
            s = "Player one lost.\n" + "Enter your name:"
        else:
            s = "Tied game!\n" + "Enter your name:"
        name = Input.input_score(s)
        if name is not None:  # if player pressed cancel, nothing to record
            Input.read_write(name, score1)
        else:
            return
