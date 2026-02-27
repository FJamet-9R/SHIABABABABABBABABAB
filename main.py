from pyscript import document, display

def showcase(a):
    document.getElementById("show").innerHTML = "" #clears the output
    players = ['Agena', 'Ala', 'Baylon','Baylon', 'Brodhagen', 'Cabatingan', 'Canete', 'Dimaculangan', 'Evangelista', 'Galang', 'Garabiles', 'Gonzales', 'Jamet', 'Ledesma', 'Nacino', 'Nardo', 'Oliveros', 'Olmedo', 'Ong', 'er*nmy alpha', 'Reyes', 'Sangreo', 'Villafuerte', 'Villegas', 'Yao', 'Bob', 'Stuart', 'Kevin', 'Jimenez']
    for player in players:

            display(player, target = "show") #showcases the players

