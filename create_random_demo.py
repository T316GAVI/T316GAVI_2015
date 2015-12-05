import string
import random as r

r.seed(90210)  # specify the random seed to get the same "random" results


def getrandomaddress():
    return "{} {} {}th Street".format(r.randint(1,1000), "East" if r.random() < 0.5 else "West" ,r.randint(4,160))

def getrandomphone():
    return "212-714-{}".format(r.randint(1000,10000))

def getrandomlicence():
    return 'LIC#{}'.format(r.randint(100000,999999))

def getrandombeer(beers, weights):
    totalweight = sum(weights)
    randvalue = r.randint(0,totalweight)

    i = 0
    while i < len(weights)-1 and randvalue > weights[i]:
        randvalue -= weights[i]
        i += 1

    return beers[i]

def getrandombar( fictionalbars, favbeers ):

    randombar = r.choice(list(fictionalbars.keys()))

    favoritebeersontap = fictionalbars[randombar]['BeersOnTap'].intersection(favbeers)
    if len(favoritebeersontap) > 0 or r.random() > 0.5:
        return randombar
    else:
        return r.choice(list(fictionalbars.keys()))




# Process the superheroes
infile = open('wiki_superheroes.txt','r')
heroes = [i.strip() for i in infile.readlines()]

letters = list(string.ascii_uppercase)
j = 0

superheroes = {}

for i in heroes:
    if len(i) > 0 and not i in letters[j:]:
        if '(' in i:
            i = i.split('(',1)[0].strip()

        superheroes[i] = {'Address': getrandomaddress(), 'Phone': getrandomphone()}

    if i == letters[j]:
        j += 1

infile.close()

# Process the bars
infile = open('wiki_fictional_bars.txt')
bars = [i.strip() for i in infile.readlines()]

fictionalbars = {}

for i in bars:
    if len(i) > 1:
        barname = i.split('—',1)[0].strip()
        barloc = i.split('—',1)[1].strip()
        fictionalbars[barname] = {'Address': barloc, 'License': getrandomlicence()}

infile.close()


# Process the beer
infile = open('beer_advocate_best_beers.txt')
beerlist = [i.strip() for i in infile.readlines()]

beers = []
breweries = []
beerweight = []

for i in range(0, len(beerlist), 3):
    try:
        beername = beerlist[i].split(' ',1)[1].strip()
        brewery = beerlist[i+1].strip()
        tmp = beerlist[i+2].split()
        weight = round(float(tmp[-4]) * int(tmp[-3].replace(',','')))

        beers.append(beername)
        breweries.append(brewery)
        beerweight.append(weight)
    except:
        pass

infile.close()

# Create Likes-Beer
for i in superheroes:
    beercount = r.randint(1,6)
    favoritebeers = set()
    while len(favoritebeers) < beercount:
        tmp = getrandombeer(beers, beerweight)
        favoritebeers.add(tmp)

    superheroes[i]['FavoriteBeers'] = favoritebeers


# Create Sells-Beer
for i in fictionalbars:
    beercount = r.randint(5,15)
    beersontap = set()
    while len(beersontap) < beercount:
        tmp = getrandombeer(beers, beerweight)
        beersontap.add( tmp )

    fictionalbars[i]['BeersOnTap'] = beersontap


# Create Frequents-Bar
for i in superheroes:
    barcount = r.randint(1,4)
    favoritebars = set()
    while len(favoritebars) < barcount:
        tmp = getrandombar( fictionalbars, superheroes[i]['FavoriteBeers'] )
        favoritebars.add(tmp)

    superheroes[i]['FavoriteBar'] = favoritebars



# Write the sql statements
outfile = open('beer_demo.sql','w')

#superheroes
for s in superheroes:
    outfile.write("insert into drinkers (name, addr, phone) values ('{}', '{}', '{}')\n".format(s.replace("'","''"), superheroes[s]['Address'], superheroes[s]['Phone']))

#bars
for b in fictionalbars:
    outfile.write("insert into bars (name, addr, licence) values ('{}', '{}', '{}')\n".format(b.replace("'","''"), fictionalbars[b]['Address'].replace("'","''"), fictionalbars[b]['License']))

#beers
for i in range(len(beers)):
    outfile.write("insert into beers (name, manf) values ('{}', '{}')\n".format(beers[i].replace("'","''"), breweries[i].replace("'","''")))

#frequents
for s in superheroes:
    for bar in superheroes[s]['FavoriteBar']:
        outfile.write("insert into frequents (drinker, bar) values ('{}', '{}')\n".format(s.replace("'","''"), bar.replace("'","''")))

#likes
for s in superheroes:
    for beer in superheroes[s]['FavoriteBeers']:
        outfile.write("insert into likes (drinker, beer) values ('{}', '{}')\n".format(s.replace("'","''"), beer.replace("'","''")))

#sells
for bar in fictionalbars:
    for beer in fictionalbars[bar]['BeersOnTap']:
        beerprice = round(100*(5+r.random()*8)) / 100.0
        outfile.write("insert into sells (bar, beer, price) values ('{}', '{}', {})\n".format(bar.replace("'","''"), beer.replace("'","''"), beerprice))

outfile.close()



