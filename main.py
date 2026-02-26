from pyscript import document, display

def showcase(a):
    document.getElementById("show").innerHTML = "" #clears the output
    players = ['Agena', 'Ala', 'Baylon','Baylon', 'Brodhagen', 'Cabatingan', 'Canete', 'Dimaculangan', 'Evangelista', 'Galang', 'Garabiles', 'Gonzales', 'Jamet', 'Ledesma', 'Nacino', 'Nardo', 'Oliveros', 'Olmedo', 'Ong', 'Rebadulla', 'Reyes', 'Sangreo', 'Villafuerte', 'Villegas', 'Yao', 'Bob']
    for player in players:
            display(player, target = "show") #showcases the players