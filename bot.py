import os
from pydoc import cli
import time
import sys
import discord
import json
import requests
import textwrap
from textwrap import wrap
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import random

flows = [
    # FLOW 1
    "We straight gassin', cuttin' straight to the bricks, haha",
    "This shit ain't nothin' to me man",
    "We smokin' runtz",
    "Shorty got a BBL, took that shit out because she couldn't run",
    "I had to do it to them, snipe",
    "I went Judge Judy on that pussy",
    "I'm not loyal to anybody, I'm a demon",
    "I have no loyalty for anyone, never did, never will",
    "Shorty chose to be with a demon",
    "My money longer than James Cameron",
    "On and off the court, straight fundamentals, no funny business",
    "Movin' like Dracula, we get it back in blood",
    "You see it, I really did this, I'm really him",
    "Flipped a whole brick into an empire, stop playin' with me",
    "I have no sympathy, I live for this shit",
    "My money long, my pockets deep",
    "No pocket watchin' in these parts",
    "We straight gassin', cuttin' straight to the bricks",
    "Chanel optics got me seein' shit",
    # FLOW 2
    "That pussy better stank, otherwise I don't want it",
    "Popped a Perc 30, got straight to fuckin'",
    "That pussy dulce, smokin' fentanyl-laced cereal milk, I see God",
    "This shit ain't nothin' to me man",
    "That pussy got me screamin', cryin', pissin', shittin', shootin' ropes",
    "Yeah, we gettin' that Pirate Bay, alien shish kabob, cordyceps money",
    "I hope them aliens are real, so that I have more things to fuck",
    "Smokin' the Qui-Gon Jinn, Vietnamese, Phillips-head runtz",
    "She suck me, like a cordless Dyson V8",
    "I'm in a k-hole lickin' balloon knot",
    "When I got the meat cannon, I bе shootin' straight rope",
    "This shit ain't nothin' to me man",
    "I need fentanyl, slime",
    "I just popped a whole garbanzo bean, fuck you mean?",
    "I smoke real Emrānī, rapscallion ghost nuggets",
    "Y'all can't fuck with me",
    "I'm him, I been him, I will continue to be him",
    "Yellow rubies glistenin', like piss",
    "Gulpin' sea monkeys by the gallon, my tummy feel crazy",
    "That coochie yummy, slime",
    "That coochie doin' it for me, slime",
    "They thought they could stop a demon, I'm back",
    "The zaza got me speakin' Esperanto",
    "This shit ain't nothin' to me man",
    "We out here cloud seedin', the scope gleamin'",
    "You can't trust me, I don't even trust myself",
    "I don't even know who I am anymore, I'm gettin' too much money",
    "Ass so fat, I'm peakin' off this Danny Phantom, slime",
    "Can you remind me who I am?",
    "Get the president on the phone now. I fronted him a brick. I need my money",
    "Hello? Blac Chyna?",
    #FLOW 3
    "I'm movin' different",
    "This shit ain't nothin' to me man, I'm a dog",
    "I'm bitin' the fart bubbles in the bath, we smokin' Symbiotes",
    "Smokin' that Whoopi Goldberg, south Egyptian, Furburger deluxe, Mega Millions scratcher, skunk, Bubba kush",
    "We smokin' dung beetle",
    "I'm on twelve Vicodin, smokin' on Scooby-Doo dick",
    "We smokin' sequoia banshee boogers",
    "We snortin' that good buffalo soldier, tamarind, Jordanian jibbies",
    "They must have amnesia, they forgot that I'm him",
    "That Burberry Backwoods pack hittin'",
    "That pussy smell like a Hellcat V8",
    "We smokin' shit in a glass pipe, blowin' the Lord's bubbles",
    "I'm sick in the head, I'm on them Broward County Tic-Tacs",
    "I'm on them Georgetown Gеronimos",
    "I'm on them Nashville nibblers",
    "I lеft my Margielas in the Benz truck",
    "I'll have to stunt on them next time",
    "I don't give a fuck if I go blind, I don't need to see the price tag anyways",
    "I'm high on twelve Jason Bournes, lookin' to beat the cum out of a thick, fresh oak",
    "We're smokin' filtered crack, you stupid piece of shit, I'll fuckin' kill you",
    "Call that pussy The Matrix because I'm in this bitch and I can't get out",
    "Last guy who ran off on the pack got choked out by some Givenchy gloves, The last thing he ever saw was the price tag on them, Slowly faded into darkness and I let the archangels take him",
    "I need more sequoia banshee boogers",
    "Don't be shy, girl, I love me some pastrami mud flaps",
    "I'm movin' like French Montana—Haaanh?",
    "Welcome to the cream kingdom, bitch, open up",
    "Blac Chyna, I'd drink her piss out of another man's balls",
    "My shooter a crackhead, he look like Woody Harrelson",
    "You ain't seen ten bands in your life, jit",
    "Reach for my neck, you'll get turned into an example",
    "Y'all gotta stop playin' with me, man",
    "I threw diamonds at the strip clubs under the Great Pyramids",
    "I pushed the camel through the eye of a needle",
    "This shit ain't nothin' to me man",
    "Tied the ops to the back of a Trackhawk and dragged 'em around the block for 24-hours",
    "Motherfucker looked like a Resident Evil 5 campaign extra after we was done with him",
    "Ops wanted some initiative, blew up their entire quadrant",
    "I'm movin' like Oppenheimer",
    "She dropped that ass on me from an egregarious angle",
    "They thought I was Steven Wallace",
    "Top shelf zaza disrupted my circadian rhythm",
    "I have seen the Magna Carta.",
    "I was flippin' bricks for Mansa Musa before y'all even became a type-1 civilization",
    "This shit ain't nothin' to me, you stupid piece of shit",
    "Step the wrong way and you will perish",
    "That pussy feel like Biscoff butter",
    "You think I care about this shit?",
    "Ask me if I care about this shit, 'cause I don't give a shit",
    "If I had a dollar for every time they said I gave a shit, I'd be broke, 'Cause I don't give a shit",
    "My bitch look like David Hasselhoff",
    "I balled so hard they thought I was a fuckin' nutsack",
    "This shit ain't nothin' to me man",
    "I'll kill you, you stupid piece of shit",
    # FLOW 4
    "This shit ain't nothin' to me man",
    "Haters in shambles, they stay pickin' the corn outta my shit",
    "This Smith & Wesson got me movin' like an invasive species",
    "I got Midas touch, fuck boy",
    "Bitch so bad I made her shit in my chopped cheese",
    "I'm at the bank 'bouta withdraw all of it",
    "These Valentinos are from Milan, you fuckin' idiot",
    "That Fentanyl gave me Vitruvian Man flexibility, Got me in a state of rigor mortis",
    "Caught a broke boy trying to come up on my Amazon package, So I skinned his ass alive, ahhhhh",
    "We smokin' Serge Ibaka, spinal fluid infused, quick-release Percs",
    "She spread it and let mе take a deep sniff of that Mahi-mahi",
    "I gave that pussy a raspberry",
    "Thеy needed a stealth soldier, so I put my hands on the hibachi hot plate at Benihana and burned my fuckin' fingerprints off, They will not find me",
    "Konichiwa, you little jit",
    "Snortin' some premium Matisyahu, got me fightin' for my life",
    "I make a nice stew out of that pussy",
    "Blacked out on the Percocet, ordered a Desert Eagle off Amazon",
    "I used to nut in my socks until the crust smelled sweet",
    "I ain't never going back",
    "Hidden Valley Ranch ice cream cake in my Fronto Leaf",
    "Got Subanese crystalline shards pokin' out my lungs, fuck boy",
    "I'm in Göbekli Tepe shirtless in a loin cloth, Blowing bareback asshole, out-smokin' aqueduct filtered sherm",
    "Told shorty to keep that box breathin' yeah",
    "She squeezin' the garlic, we smokin' java man",
    "Face pressed up against that monkey, sniffin' for dear life",
    "The Cuban link will turn the diamond tester into a pipe bomb",
    "Glock-34 shivered his timbers",
    "Blew her back out usin' a mammoth-skin condom",
    "Dick/pussy freeballin', like Shaq and Kobe",
    "I'm smokin' Mesopotamian, Stanley Cup triple-award-winning, soul-bleeder, taint blaster, J.D. Power Associates, dingleberry zaza",
    "We smokin' that IBM Quantum Computer",
    "I can't wait to curb stomp you in these dumb ugly ass Rick Owens shoes",
    "I'm Dracula, I'm twelve million years old, When I hit it from behind, the room smells like absolute michi",
    "They said I wouldn't shit on 'em, I spread my cheeks and hit 'em with an absolute screamer",
    "Lil' bro was emaciated, the Percs done ate lil' cuzzo ass up",
    "These cops are interrogating me about an ounce of weed, As if I didn't kill an Applebee's hostess two miles away",
    "I come from a long bloodline of Italian leather",
    "My Bottegas have veins pumpin' through them",
    "Smoking indigenous Fronto Leaf in a bacon, egg, and cheese",
    "Hashtag: 'Le Chemin du Roi'",
    "Eyes bloodshot, leanin' up against the wall, Beatin' off to my Chrome Hearts boots",
    "Opps was talkin' crazy, shot 'em in the mouth",
    "My Audemars Piguet worth the GDP of Yemen",
    "If this watch breaks, the foreign exchange market will take a twenty-eight percent hit, people will die",
    "My diamonds come from the most horrific situations possible",
    "Slurpin' a quick-release Perc off the plate, like a pinto bean",
    "I keep my Glock at the Vatican",
    "She squirt on me, I love bein' covered in the chichi manga",
    "They're sick in the head, they forgot I'm him",
    "I'm the 'Him-ulation', I am 'Him Kardashian', 'Him-buktu', 'Him-on and Pumba'",
    "I got my DNA test back, Turns out I'm one-hundred percent 'Him-alayan'",
    "Fuck it, I ate the opp",
    "That gash sound like salmon roe",
    "You ran off with the Diddy Kong",
    "Triple espresso",
    "Personal hot spot stim-gripper runts",
    "There are consequences to your crimes against Dracula",
    "Get shorty out of here, she's built like a Jay Electronica verse",
    "Icewear Vezzo said it best, 'I'm a mud baby, I can't stop'",
    "I have more Percs than there are stars in the Leo Cluster",
    "I'm claiming every corner, every block",
    "Fuck it, I'm coming for every enzyme",
    "Snorting dexie",
    "Eating skate right out of the lake",
    "Opp was sneak-dissing on the 'gram, Turned his city into Pompeii",
    "These ain't no Mall-mains, you ugly bastard",
    "They want to drive a wooden stake into my heart, For pulling my cock out at the Toronto Blue Jays game, All I'm saying is I paid for the tickets",
    "My Ducati leather trench coat bright red",
    "I look like ten million crawdads fucking",
    "That elite pussy turn me into a radical",
    "I'm moving lucrative",
    "I'm in the pod smoking Sebulba",
    "Smoking that good schooby-doo waa",
    "I'm fucked up in the crib listening to Trill Sammy",
    "I'm on the Ivory Coast eating, Vermilion snapper",
    "War is all I think about",
    "I never been scared in my life jit",
    "This shit ain't nothing to me man",
    "I need my percs!",
    "One perc is never enough (Yo!)",
    "Popped a Brazillian butt berserker, and had that pussy screeching like a harpy eagle, [Growls]",
    "I'm smoking that shit that makes the toes curl",
    "I'm doing a lot of drugs, a lot!",
    "Walked along the sand dunes of the Sahara desert for forty days and forty nights with nothing but a pack of Newports And a fifth of henny, I really do this shit",
    "I'm starting to get real pissed off",
    "What the fuck is Obamacare? Hey Obama, I don't care about shit!",
    "Look at this shit, I sold crack to myself",
    "Spun around the block so many times, They thought it was fucking Minecraft",
    "We smoking that Boomhauer",
    "Choked his goofy ass out with a B.B. Simon belt",
    "She wanted dick, but I gave her crack",
    "I'm smoking lizard taint",
    "Sniffing monkey",
    "It's monkey monday, show me that monkey",
    "[Screams]",
    "I'm getting too much money!",
    "I'm fucked up drinking a Chinese modelo",
    "I'm smoking on that hush puppy limon",
    "Broke boy wasn't balling enough",
    "Welcome to the Guangdong Tigers",
    "These Ferragamos are real, cunt",
    "I got more sticks than a fucking forest",
    "I have the blueprint to the catacombs",
    "Popped four flim-flams at K.O.D., Came out with Hepatitis",
    "This shit ain't nothing to me man!",
    "I'll fucking kill you!",
    "Smoked a new opp, his meat came right off the bone",
    "The first time I smoked runts, I coughed so fucking hard, I started passing kidney stones, Then shat myself in front of the gang! There was scat all over the pounds we shipped out for the next thirty business days",
    "I don't have any compassion for broke boys everybody has an asshole. Most people have dick and balls",
    "Go outside and get a bag!",
    "I knew the perc was fake but I still ate it because I'm a gremlin",
    "I'll air this bitch out like I shit in it",
    "I took two limitless pills to limit myself",
    "I got so much cheese in my pocket, They thought I was a fucking calzone",
    "That pussy balder than Howie Mandel",
    "Crash the Benz truck",
    "Sip some mud",
    "Everything felt alright",
    "Popped a bean, now I wanna kill someone",
    "Yeah, I drill with my mask off",
    "I'm moving like Gilbert Arenas",
    "Sniffing white phosphorus",
    "The Vatican wants to wet me up with silver bullets, But I'm on a god damn samurai pill!",
    "I'm a real creature, I'll spin the block, Huffing spores, To see tomorrow's stock market",
    "Lungs looking crazy",
    "Rolling the old flesh cigar around your fingertips",
    "Boy ran off with a Banjo-Kazooie, I had to cast a spell on that motherfucker",
    "I got strands of RNA in my hookah, Every puff is an insult to God",
    "The dust pack got me doing the third world stare",
    "This zaza will give you a 2019 Alex Caruso hairline",
    "Chopper small and sturdy. Built like Wilmer Valderrama",
    "I let her hit the zaza just to buy her a bit more time. But all she wanted to do was fuck my brains out, then euthanize herself",
    "I hydrated the soot between her ass cheeks, And snorted that shit through my eyelids",
    "I'll give you that fluoride stare",
    "Pussy so tight I had to scissor her ass",
    "This henny got me feeling crazy",
    "This henny got me wanting the shit",
    "This henny got me feeling like DDG",
    "My bitch pussy fatter than Druski",
    "I'm thirsty!",
    "I'm ready, I'm trying to po' up",
    "Drank man, please!",
    "This henny making me want to go to the mall and do something crazy",
    "If Santa come down my chimney, I'm gon' fuck him",
    "That's what my Hellcat sounds like",
    "This shit ain't nothing to me man!",
]


def GetFlow(n):
    flow = ""
    suffix = ""
    prefix = ""
    for i in range(n):
        if (i is 0):
            suffix = ""
        else:
            if (i is 1):
                prefix = "\n"
            suffix = "\n"
        flow += prefix + random.choice(flows) + suffix
        prefix = ""
        suffix = ""
    return flow

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=discord.Intents.default())

bot = commands.Bot(intents=discord.Intents.default(),command_prefix="drac ",
                   help_command=None)

@bot.event
async def on_ready():
    await bot.tree.sync()

@bot.tree.command(name="flow",description="Spew forth like the rivers of babylon.")
async def flow(interaction:discord.Interaction, lines: int = 1):
    await interaction.response.defer()

    
    if (lines < 0):
        return
    
    if (lines > 100):
        lines = 100

    theFlows = GetFlow(lines)
    
    str_bytes = sys.getsizeof(theFlows)
    print(str(str_bytes))

    index = 0
    chunk_size = 2000

    
    while True:
        chunk = theFlows[index:chunk_size + index]
        if (index is 0):
            await interaction.followup.send(chunk)
        else:
            await interaction.followup.send(chunk)
        index += chunk_size

        del chunk

        if (index >= len(theFlows) - 1):
            break

bot.run(TOKEN)