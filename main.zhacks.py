from collections import defaultdict
from flask import Flask
from flask import request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/submit')
def get_list():
  qualities = request.args.get('answers')
  qualities = qualities.split(',')
  corresponders = make_dict(qualities)
  final_game = pick_game(corresponders)
  final_dict = {'gamename': final_game, 
    'gameplot': plot[games.index(final_game)], 
    'gamerating': rate[games.index(final_game)],
    'gamepicture': pictures[games.index(final_game)]}
  return final_dict


def make_dict(lst):
  game_scores = defaultdict(int)
  for game in games:
    for item in lst:
      if item in desc[games.index(game)]:
        game_scores[game] += 1
  return game_scores

def pick_game(dicti):
  user_games = list(dicti.keys())
  user_scores = list(dicti.values())
  user_choice = user_games[user_scores.index(max(user_scores))]
  return user_choice



games = ["Halo", 
  "Doki-Doki Literature Club", 
  "Apex Legends", 
  "Dead Space 1", 
  "Resident Evil", 
  "Minecraft", 
  "League of Legends", 
  "Overwatch",
  "MapleStory",
  "Life is Strange",
  "Omori",
  "Genshin Impact",
  "Five Nights at Freddie's",
  "Age of Empires",
  "Subnautica",
  "Fall Guys",
  "Grand Theft Auto 5",
  "Ib",
  "Final Fantasy XV",
  "Warframe",
  "Diablo",
  "Destiny 2"]
desc = ["3D action sci-fi medium multiplayer fighting pvp realistic", 
  "2D RPG horror medium solo puzzle story artistic", 
  "3D action sci-fi short online fighting pvp realistic", 
  "3D action horror long solo fighting story realistic", 
  "3D RPG horror medium solo puzzle story realistic",
  "3D indie fantasy long multiplayer puzzle casual artistic", 
  "3D action fantasy short online fighting pvp artistic",
  "3D action sci-fi online fighting pvp artistic",
  "2D RPG fantasy online casual artistic",
  "3D indie mystery medium solo puzzle story artistic",
  "2D indie horror long solo turn-based story artistic",
  "3D adventure fantasy multiplayer fighting story artistic",
  "3D indie horror short solo puzzle story realistic",
  "2D adventure fantasy online turn-based pvp realistic",
  "3D adventure sci-fi long solo puzzle casual realistic",
  "3D action sci-fi short multiplayer fighting pvp artistic",
  "3D action mystery online fighting pvp realistic",
  "2D RPG horror medium solo puzzle story artistic",
  "3D RPG fantasy long solo fighting story artistic",
  "3D action fantasy medium online fighting story realistic",
  "3D RPG fantasy long solo fighting story realistic",
  "3D adventure sci-fi long multiplayer fighting pvp realistic"]
plot = ["Genres:\n Action, PvP, shooter game\n<br>About:\n 'Set in the distant past, this sci-fi game pairs story, worldbuilding, and intense fighting mechanics will send you fighting against the Flood -- a powerful alien parasite -- through the Milky Way Galaxy.'",
  "Genres:\n Anime, Psychological Horror, Visual Novel game\n<br>About:\n 'You play as the main character, who reluctantly joins the Literature Club in search of a romantic interest. With every poem you write and every choice you make, you’ll charm your crush and begin to unfold the horrors of school romance. Do you have what it takes to crack the code of dating sims and get the perfect ending?'",
  "Genres:\n Action, PvP, shooter game\n<br>About:\n 'Master an ever-growing roster of legendary characters with powerful abilities and experience strategic squad play and innovative gameplay in the next evolution of Hero Shooter and Battle Royale.'",
  "Genres:\n Action, horror, story game\n<br>About:\n 'You are Isaac Clarke, an engineer on the spacecraft USG Ishimura. You're not a warrior. You're not a soldier. You are, however, the last line of defense for the remaining living crew.'",
  "Genres:\n Horror, RPG, story game\n<br>About:\n 'In 1998 a special forces team is sent to investigate some bizarre murders on the outskirts of Raccoon City. Upon arriving they are attacked by a pack of blood-thirsty dogs and are forced to take cover in a nearby mansion. But the scent of death hangs heavy in the air. Supplies are scarce as they struggle to stay alive.'",
  "Genres:\n Open-world, sandbox, multiplayer game\n<br>About:\n 'Explore infinite worlds and build everything from the simplest of homes to the grandest of castles. Play in creative mode with unlimited resources or mine deep into the world in survival mode, crafting weapons and armor to fend off dangerous mobs.'",
  "Genres:\n Action-Fantasy, PvP, Strategy game\n<br>About:\n 'Team-based game, multiplayer online battle arena video game with over 140 champions to make epic plays with.'",
  "Genres:\n Open-world, PvP, shooter game\n<br>About:\n 'Overwatch is a colorful team-based action game starring a diverse cast of powerful heroes. Travel the world, build a team, and contest objectives in exhilarating 6v6 combat.'",
  "Genres:\n Multiplayer, RPG, Casual game\n<br>About:\n 'The history of Maple World is rich and storied, and stretches back for millennia. Begin your adventure today and you’ll relive the harrowing war against the sinister Black Mage and experience the continuing legacy of his secret society, the Black Wings. Each character and class has their own quest line and tale to tell- try them all to get the full story!'",
  "Genres:\n Story-rich, choice-based, mystery game\n<br>About:\n 'Follow the story of Max Caulfield, a photography senior who discovers she can rewind time while saving her best friend Chloe Price. The pair soon find themselves investigating the mysterious disappearance of fellow student Rachel Amber, uncovering a dark side to life in Arcadia Bay. Meanwhile, Max must quickly learn that changing the past can sometimes lead to a devastating future.'",
  "Genres:\n RPG, Psychological Horror, turn-based game\n<br>About:\n 'Explore a strange world full of colorful friends and foes. Navigate through the vibrant and the mundane in order to uncover a forgotten past. When the time comes, the path you’ve chosen will determine your fate... and perhaps the fate of others as well.'",
  "Genres:\n Fantasy, Open-world, Gatcha game\n<br>About:\n 'Genshin Impact is an action role-playing game that takes place in the fantasy world of Teyvat, which is home to seven distinct nations, each of which is tied to a different element and ruled by a different god.'",
  "Genres:\n Horror, Indie, Simulation game\n<br>About:\n 'Welcome to your new summer job at Freddy Fazbear's Pizza, where kids and parents alike come for entertainment and food! The main attraction is Freddy Fazbear, of course; and his two friends. They are animatronic robots, programmed to please the crowds!'",
  "Genres:\n Real-time strategy, PvP fantasy game\n<br>About:\n 'Age of Empires IV takes players on a journey through the ages as they command influential leaders, build expansive kingdoms, and fight some of the most critical battles of the Middle Ages.'",
  "Genres:\n Open-world, action, survival game\n<br>About:\n 'Descend into the depths of an alien underwater world filled with wonder and peril. Craft equipment, pilot submarines and out-smart wildlife to explore lush coral reefs, volcanoes, cave systems, and more - all while trying to survive.'",
  "Genres:\n PvP, Multiplayer, Casual game\n<br>About:\n 'Fall Guys is a massively multiplayer party game with up to 60 players online in a free-for-all struggle through round after round of escalating chaos until one victor remains!'",
  "Genres:\n PvP, Crime, Multiplayer game\n<br>About:\n 'When a young street hustler, a retired bank robber and a terrifying psychopath find themselves entangled with some of the most frightening and deranged elements of the criminal underworld, the U.S. government and the entertainment industry, they must pull off a series of dangerous heists to survive in a ruthless city in which they can trust nobody, least of all each other.'",
  "Genres:\n RPG Maker, Psychological Horror, Puzzle game\n<br>About:\n 'You play as the titular character Ib, a young girl who visits an art museum with her parents. She had simply been wandering off on her own when she suddenly realizes that the museum is now empty and she can’t seem to leave. She must explore the strange place, solve puzzles, team up with newfound allies, and try to steer clear of the strange monsters from the paintings to escape. '",
  "Genres:\n Story-rich, fantasy, RPG game\n<br>About:\n 'For the first time, players take control of Noctis's greatest foe in this brand-new episode of FINAL FANTASY XV! Delve into the dark tale of scorned saviour Ardyn Lucis Caelum and unravel the secrets surrounding his mysterious past.'",
  "Genres:\n Sci-fi, multiplayer, action game\n<br>About:\n 'In the far-future world of Warframe, grotesque clones and capitalist machines dominate our solar system. Fight back against greed and corruption as you explore 18 worlds filled with techno-organic horrors.'",
  "Genres:\n Dark-fantasy, Action, Fighting game\n<br>About:\n 'Diablo is an action role-playing dungeon crawler video game series based on the premise of a war between Heaven and Hell.'",
  "Genres:\n First-person shooter, multiplayer, action game\n<br>About:\n 'Dive into the world of Destiny 2 to explore the mysteries of the solar system and experience responsive first-person shooter combat. Unlock powerful elemental abilities and collect unique gear to customize your Guardian's look and playstyle. Enjoy Destiny 2’s cinematic story, challenging co-op missions, and a variety of PvP modes alone or with friends. Download for free today and write your legend in the stars.'"]
rate = ["7/10: If you like science fiction, space, and first-person shooters, this is the game for you!",
  "8/10: Starts off slow, but if you like the slow-build psychological horror, this is the game for you!",
  "7/10: Difficult for newcomers but fun once you get the hang of it. If you like competitive PvP fighting games, this is the game for you!",
  "10/10: A rich story line with great graphics and gameplay. Perfect for thriller-lovers!",
  "8/10: Chilling, suspenseful, and fun. If you like chasing from inevitable doom and an mysterious storyline, this is the game for you!",
  "10/10: The game you make. Spend hours exploring an endless world alone, or rush the ender dragon with a group of friends. If you love a game you can sink hours into, this is the one for you!",
  "6/10: A fun game with friends every now and then, but only play if you're ready to get flamed by an enemy team with no grasp of basic grammar. If you like PvP and repition, this is the game for you!",
  "8/10: Overall fun PvP game, but watch out for unbalanced characters. If you like open world fighting games, this is the one for you!",
  "8/10: Casual, nostalgic game for fantasy and anime-lovers. Watch out, though, you'll lose hours in this game. If you like that, this is the game for you!",
  "9/10: Amazing cinematic elements and fun time-travel mechanic. Definitely an emotional rollercoaster, get ready to cry! If you want to sit back and let your choices dictate your story, this is the game for you!",
  "10/10: A heavy, yet heartful story for psychological horror fans. One of the best aesthetics in gaming, and certainly a story that will leave you in tears. If you're emotionally prepared, this is the game for you!",
  "7/10: Amazing soundtrack and creative world-building! Just watch out, your wallet will surely suffer. For those who love to explore worlds and collect characters, this is the game for you!",
  "7/10: The start to a famously chilling horror series. You may need to watch some theories to get this one... For those who love jumpscares, this is the game for you!",
  "5/10: A bit slow but best suited for those in it for the long game. For the strategy nerds, this is the game for you!",
  "8/10: A fun exploration and survival game. Be prepared to sink hours into exploring. For those who are terrified yet awed by the deep sea, this is the game for you!",
  "7/10: Definitely a game to play with friends. If you like chaos and lots of laughs, this is the game for you!",
  "6/10: Best played with friends, but not a game to stay on for too long. For those who really want to steal a car but don't want to steal a car in real life, this is the game for you!",
  "9/10: A classic for RPG maker fanatics. Atmospheric and melancholic, this is the game for those who love psychological horror!",
  "9/10: Prepare to lose many hours to this game, but love the experience. Amazing graphics and a classic Final-Fantasy storytelling experience!",
  "9/10: Fun gameplay for those who like the grind. If that sounds up your alley, this is the game for you!",
  "8/10: Fun for those who like an insanely difficult game. Really. This game inspired the rage of a thousand suns. If that sounds up your alley, try it out!",
  "7/10: Good graphics, pretty fun PvP. If you're into competitive shooter games, try this out!"]
pictures = ["https://gamingbolt.com/wp-content/uploads/2021/07/halo-wars.jpg",
  "https://nintendoeverything.com/wp-content/uploads/doki-doki-literature-club-plus-scaled.jpg",
  "https://www.gamersnexus.net/media/k2/items/cache/41800ddcbf765d04344c295d60cdf173_XL.jpg",
  "https://static1.colliderimages.com/wordpress/wp-content/uploads/2021/07/best-moments-deadspace.jpg?q=50&fit=contain&w=750&h=375&dpr=1.5",
  "https://i1.wp.com/bloody-disgusting.com/wp-content/uploads/2016/08/Resident-Evil-Franchise.jpg?w=2220&ssl=1",
  "https://cdn.mos.cms.futurecdn.net/CxzfDaXkJQxwnsFzoY2xRK-970-80.jpeg.webp",
  "https://cdn1.dotesports.com/wp-content/uploads/2019/09/12195522/league-of-legends.jpg",
  "https://cdn.mos.cms.futurecdn.net/Qnd8MegrwWPVcqKjdoSfLH.jpg",
  "https://nxcache.nexon.net/maplestory/assets-new/img/default/microsites.jpg",
  "https://cdn.mos.cms.futurecdn.net/yZQopquPGrKNRKci3qxty9.jpg",
  "https://i1.sndcdn.com/artworks-IYCySe4K6pvvqC1T-oL3Euw-t500x500.jpg",
  "https://www.dexerto.com/wp-content/uploads/2020/10/GenshinImpactmiHoYo.jpg",
  "https://preview.redd.it/v0ycjswmnpo51.jpg?auto=webp&s=c1153e34b8f7ce74ee491b56695edc2e40f0747e",
  "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Age_of_Empires_II_-_The_Age_of_Kings_Coverart.png/220px-Age_of_Empires_II_-_The_Age_of_Kings_Coverart.png",
  "https://cdn.akamai.steamstatic.com/steam/apps/264710/capsule_616x353.jpg?t=1632886155",
  "https://assets.nintendo.com/image/upload/c_pad,f_auto,h_613,q_auto,w_1089/ncom/en_US/games/switch/f/fall-guys-ultimate-knockout-switch/hero?v=2021111311",
  "https://wallpaperaccess.com/full/938901.jpg",
  "https://e.snmc.io/lk/lv/x/3bb4b72efb518b87e33d89bf0e7d51d3/7447888",
  "https://s3.gaming-cdn.com/images/products/3833/orig/game-final-fantasy-xv-windows-edition-cover.jpg",
  "https://www.mobygames.com/images/covers/l/700400-warframe-playstation-5-front-cover.jpg",
  "https://commondatastorage.googleapis.com/images.pricecharting.com/d562f164eb5b23111a3754dfc7688e7a9e568333efae8baa121cd5b7df587378/240.jpg",
  "https://cdn.images.express.co.uk/img/dynamic/143/590x/Destiny-PC-Steam-840844.jpg"]
# corresponders = get_list()
# final_game = pick_game(corresponders)
# print()
# print(f"We think you would like {final_game}!")
# print()
# print(f"{plot[games.index(final_game)]}")
# print()
# print(f"{rate[games.index(final_game)]}")
# print("Have Fun!")
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)