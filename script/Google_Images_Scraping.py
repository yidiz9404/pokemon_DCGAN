# -*- coding: utf-8 -*-

#Searching and Downloading Google Images/Image Links

#Import Libraries

import time       #Importing the time library to check the time of code execution
import sys    #Importing the System Library

import urllib2 as urllib2   #urllib.request
import copy
import os



#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    i = 20
    j = i * 2
    while i > 0 and j > 0:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            if len(item) < 1000:
                items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
        if len(item) < 1000:
            print('successful link')
            i -= 1
        else:
            print('broken link')
        j -= 1
    return items



#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib2    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib2.Request(url, headers = headers)
            resp = urllib2.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2 as urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
########### Edit From Here ###########

#This list is used to search keywords. You can edit this list to search for google images of your choice. You can simply add and remove elements of the list.

# pokemon_list = [' pikachu', ' squirtle', ' charmander', ' goldeen', ' charmeleon', ' snorlax']
pokemon_list = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'VenusaurMega Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'CharizardMega Charizard X', 'CharizardMega Charizard Y', 'Squirtle', 'Wartortle', 'Blastoise', 'BlastoiseMega Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'BeedrillMega Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'PidgeotMega Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran-f', 'Nidorina', 'Nidoqueen', 'Nidoran-m', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'AlakazamMega Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'SlowbroMega Slowbro', 'Magnemite', 'Magneton', "Farfetch'd", 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'GengarMega Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'KangaskhanMega Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'PinsirMega Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'GyaradosMega Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'AerodactylMega Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'MewtwoMega Mewtwo X', 'MewtwoMega Mewtwo Y', 'Mew', 'Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw', 'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou', 'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Mareep', 'Flaaffy', 'Ampharos', 'AmpharosMega Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow', 'Slowking', 'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco', 'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'SteelixMega Steelix', 'Snubbull', 'Granbull', 'Qwilfish', 'Scizor', 'ScizorMega Scizor', 'Shuckle', 'Heracross', 'HeracrossMega Heracross', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom', 'HoundoomMega Houndoom', 'Kingdra', 'Phanpy', 'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid', 'Magby', 'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar', 'TyranitarMega Tyranitar', 'Lugia', 'Ho-oh', 'Celebi', 'Treecko', 'Grovyle', 'Sceptile', 'SceptileMega Sceptile', 'Torchic', 'Combusken', 'Blaziken', 'BlazikenMega Blaziken', 'Mudkip', 'Marshtomp', 'Swampert', 'SwampertMega Swampert', 'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir', 'GardevoirMega Gardevoir', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'SableyeMega Sableye', 'Mawile', 'MawileMega Mawile', 'Aron', 'Lairon', 'Aggron', 'AggronMega Aggron', 'Meditite', 'Medicham', 'MedichamMega Medicham', 'Electrike', 'Manectric', 'ManectricMega Manectric', 'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'SharpedoMega Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt', 'CameruptMega Camerupt', 'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu', 'Altaria', 'AltariaMega Altaria', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy', 'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Castform', 'Kecleon', 'Shuppet', 'Banette', 'BanetteMega Banette', 'Duskull', 'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'AbsolMega Absol', 'Wynaut', 'Snorunt', 'Glalie', 'GlalieMega Glalie', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence', 'SalamenceMega Salamence', 'Beldum', 'Metang', 'Metagross', 'MetagrossMega Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias', 'LatiasMega Latias', 'Latios', 'LatiosMega Latios', 'Kyogre', 'KyogrePrimal Kyogre', 'Groudon', 'GroudonPrimal Groudon', 'Rayquaza', 'RayquazaMega Rayquaza', 'Jirachi', 'DeoxysNormal Forme', 'DeoxysAttack Forme', 'DeoxysDefense Forme', 'DeoxysSpeed Forme', 'Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup', 'Empoleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew', 'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy', 'WormadamPlant Cloak', 'WormadamSandy Cloak', 'WormadamTrash Cloak', 'Mothim', 'Combee', 'Vespiquen', 'Pachirisu', 'Buizel', 'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom', 'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'LopunnyMega Lopunny', 'Mismagius', 'Honchkrow', 'Glameow', 'Purugly', 'Chingling', 'Stunky', 'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly', 'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb', 'Gible', 'Gabite', 'Garchomp', 'GarchompMega Garchomp', 'Munchlax', 'Riolu', 'Lucario', 'LucarioMega Lucario', 'Hippopotas', 'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak', 'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'AbomasnowMega Abomasnow', 'Weavile', 'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon', 'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'GalladeMega Gallade', 'Probopass', 'Dusknoir', 'Froslass', 'Rotom', 'RotomHeat Rotom', 'RotomWash Rotom', 'RotomFrost Rotom', 'RotomFan Rotom', 'RotomMow Rotom', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'GiratinaAltered Forme', 'GiratinaOrigin Forme', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'ShayminLand Forme', 'ShayminSky Forme', 'Arceus', 'Victini', 'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite', 'Emboar', 'Oshawott', 'Dewott', 'Samurott', 'Patrat', 'Watchog', 'Lillipup', 'Herdier', 'Stoutland', 'Purrloin', 'Liepard', 'Pansage', 'Simisage', 'Pansear', 'Simisear', 'Panpour', 'Simipour', 'Munna', 'Musharna', 'Pidove', 'Tranquill', 'Unfezant', 'Blitzle', 'Zebstrika', 'Roggenrola', 'Boldore', 'Gigalith', 'Woobat', 'Swoobat', 'Drilbur', 'Excadrill', 'Audino', 'AudinoMega Audino', 'Timburr', 'Gurdurr', 'Conkeldurr', 'Tympole', 'Palpitoad', 'Seismitoad', 'Throh', 'Sawk', 'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede', 'Whirlipede', 'Scolipede', 'Cottonee', 'Whimsicott', 'Petilil', 'Lilligant', 'Basculin', 'Sandile', 'Krokorok', 'Krookodile', 'Darumaka', 'DarmanitanStandard Mode', 'DarmanitanZen Mode', 'Maractus', 'Dwebble', 'Crustle', 'Scraggy', 'Scrafty', 'Sigilyph', 'Yamask', 'Cofagrigus', 'Tirtouga', 'Carracosta', 'Archen', 'Archeops', 'Trubbish', 'Garbodor', 'Zorua', 'Zoroark', 'Minccino', 'Cinccino', 'Gothita', 'Gothorita', 'Gothitelle', 'Solosis', 'Duosion', 'Reuniclus', 'Ducklett', 'Swanna', 'Vanillite', 'Vanillish', 'Vanilluxe', 'Deerling', 'Sawsbuck', 'Emolga', 'Karrablast', 'Escavalier', 'Foongus', 'Amoonguss', 'Frillish', 'Jellicent', 'Alomomola', 'Joltik', 'Galvantula', 'Ferroseed', 'Ferrothorn', 'Klink', 'Klang', 'Klinklang', 'Tynamo', 'Eelektrik', 'Eelektross', 'Elgyem', 'Beheeyem', 'Litwick', 'Lampent', 'Chandelure', 'Axew', 'Fraxure', 'Haxorus', 'Cubchoo', 'Beartic', 'Cryogonal', 'Shelmet', 'Accelgor', 'Stunfisk', 'Mienfoo', 'Mienshao', 'Druddigon', 'Golett', 'Golurk', 'Pawniard', 'Bisharp', 'Bouffalant', 'Rufflet', 'Braviary', 'Vullaby', 'Mandibuzz', 'Heatmor', 'Durant', 'Deino', 'Zweilous', 'Hydreigon', 'Larvesta', 'Volcarona', 'Cobalion', 'Terrakion', 'Virizion', 'TornadusIncarnate Forme', 'TornadusTherian Forme', 'ThundurusIncarnate Forme', 'ThundurusTherian Forme', 'Reshiram', 'Zekrom', 'LandorusIncarnate Forme', 'LandorusTherian Forme', 'Kyurem', 'KyuremBlack Kyurem', 'KyuremWhite Kyurem', 'KeldeoOrdinary Forme', 'KeldeoResolute Forme', 'MeloettaAria Forme', 'MeloettaPirouette Forme', 'Genesect', 'Chespin', 'Quilladin', 'Chesnaught', 'Fennekin', 'Braixen', 'Delphox', 'Froakie', 'Frogadier', 'Greninja', 'Bunnelby', 'Diggersby', 'Fletchling', 'Fletchinder', 'Talonflame', 'Scatterbug', 'Spewpa', 'Vivillon', 'Litleo', 'Pyroar', 'Flabébé', 'Floette', 'Florges', 'Skiddo', 'Gogoat', 'Pancham', 'Pangoro', 'Furfrou', 'Espurr', 'MeowsticMale', 'MeowsticFemale', 'Honedge', 'Doublade', 'AegislashBlade Forme', 'AegislashShield Forme', 'Spritzee', 'Aromatisse', 'Swirlix', 'Slurpuff', 'Inkay', 'Malamar', 'Binacle', 'Barbaracle', 'Skrelp', 'Dragalge', 'Clauncher', 'Clawitzer', 'Helioptile', 'Heliolisk', 'Tyrunt', 'Tyrantrum', 'Amaura', 'Aurorus', 'Sylveon', 'Hawlucha', 'Dedenne', 'Carbink', 'Goomy', 'Sliggoo', 'Goodra', 'Phantump', 'Trevenant', 'PumpkabooAverage Size', 'PumpkabooSmall Size', 'PumpkabooLarge Size', 'PumpkabooSuper Size', 'GourgeistAverage Size', 'GourgeistSmall Size', 'GourgeistLarge Size', 'GourgeistSuper Size', 'Bergmite', 'Avalugg', 'Noibat', 'Noivern', 'Xerneas', 'Yveltal', 'Zygarde50% Forme', 'Diancie', 'DiancieMega Diancie', 'HoopaHoopa Confined', 'HoopaHoopa Unbound', 'Volcanion']
actions = [' ', ' pokemon', ' pixel art', ' anime screenshot', ' icon']
for pokemon in pokemon_list:
    pokek = 0
    # pokemon = ' ' + pokemon
    for action in actions:
        search_keyword = [pokemon + action]
        t0 = time.time()   #start the timer
        
        #Download Image Links
        i = 0
        items = []
        while i<1:
            iteration = "Item no.: " + str(i+1) + " -->" + " Item name = " + str(search_keyword[i])
            print (iteration)
            print ("Evaluating...")
            search_keywords = search_keyword[i]
            search = search_keywords.replace(' ','%20')
                #pure_keyword = keywords[j].replace(' ','%20')
            url = 'https://www.google.com/search?q=' + search + \
                    '%20-gettyimages%20-istock%20-shutterstock%20-tattoo%20-drawing' + \
                    '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
            raw_html =  (download_page(url))
            time.sleep(0.1)
            items = items + (_images_get_all_items(raw_html))
            i = i + 1
        
        	#'https://www.google.com/search?q=hello%20kitty%20wins&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg&&tbs=islt:2mp,isz:ex,iszw:64,iszh:64'        
            #print ("Image Links = "+str(items))
        print ("Total Image Links = "+str(len(items)))
        print ("\n")
        
        
        #This allows you to write all the links into a test file. This text file will be created in the same directory as your code. You can comment out the below 3 lines to stop writing the output to the text file.
        info = open('output.txt', 'a')        #Open the text file called database.txt
        info.write(str(i) + ': ' + str(search_keyword[i-1]) + ": " + str(items) + "\n\n\n")         #Write the title of the page
        info.close()                            #Close the file
        
        t1 = time.time()    #stop the timer
        total_time = t1-t0   #Calculating the total time required to crawl, find and download all the links of 60,000 images
        print("Total time taken: "+str(total_time)+" Seconds")
        print ("Starting Download...")
        
        ## To save imges to the same directory
        # IN this saving process we are just skipping the URL if there is any error
        dir = 'data/' + pokemon
        if not os.path.exists(dir):
            os.makedirs(dir)
        k=0
        errorCount=0
        while(k<len(items)-5):
            from urllib2 import Request,urlopen
            from urllib2 import URLError, HTTPError
            pokek = pokek + 1
        
            try:
                req = Request(items[k], headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
                response = urlopen(req)
                
                output_file = open(dir+'/'+str(pokek+1)+".jpg",'wb')
                data = response.read()
                output_file.write(data)
                response.close();
        
                print("completed ====> "+str(k+1))
        
                k=k+1;
        
            except IOError:   #If there is any IOError
        
                errorCount+=1
                print("IOError on image "+str(k+1))
                k=k+1;
        
            except HTTPError as e:  #If there is any HTTPError
        
                errorCount+=1
                print("HTTPError"+str(k))
                k=k+1;
            except URLError as e:
        
                errorCount+=1
                print("URLError "+str(k))
                k=k+1;
            except:
                errorCount+=1
                print("random error "+str(k))
                k +=1
                continue
print("\n")
print("All are downloaded")
print("\n"+str(errorCount)+" ----> total Errors")

#----End of the main program ----#