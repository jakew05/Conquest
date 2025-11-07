import textwrap

# sub world-dictionaries
wh = {
    'main': textwrap.fill("You awake on polished stone floor in a room of white light.You bring yourself to your feet, the"
    " horizon expands endlessly in all directions. Before you are three pedestals each with a weapon upon it. "
    "'Conquest...' a distant voice calls. \n'You are called now to these corrupted lands. Select your weapon, and fulfill your "
    "duty.'", 50)
}
fog = {
    'main': textwrap.fill("You fall from the heavens and land upon the earth. Around you " \
    "stand ten thousand graves, each bearing the name of a fallen knight. Though many of the graves have eroded " \
    "under the cruel currents of time, some still stand to honor the soldier in the ground beneath them. There " \
    "is a grave before you, at the foot of which lies a leather sack. In the distance, you spot a large wooden " \
    "crate. Behind you, there is a monument, with text carved into its smooth surface. [objects: grave, crate, monument]", 50),

    'grave': textwrap.fill("On the grave before you a name is inscribed: \n\nRyle Grayloom \n11313 - 11340\nMay you tread easy on"
    " Heva's Path. May she guide you from the dark.\n\nYou look to the foot of the grave and open the leather sack."
    " you find a meager supply:", 50),

    'crate': textwrap.fill("as you approach the crate, you see that it is long and low to the ground. You pry off the top of the crate"
    " and find a man inside. He is without skin, muscle, or mind, but you can feel his life, clinging with what strength"
    " it has left to its boney frame. You feel the fallen soldier call you to battle [enemy: skeleton]. Beside the crate there is a small stash of weapons.", 50),

    'monument': textwrap.fill("A monument stands tall before you. Inscribed upon the weathered stone is a short dedication:\n\n"
    "'Our lands, corrupt. Our minds, troubled and tortured. Our kingdom, threatened by those of the Spire. "
    "CONQUEST, we call for your aid. Descend once more and accept this call. Help us fight the Corrupted One and "
    "save us from this dark era. We shall await your arrival in Sorrowieve.' There is a rolled up map at the foot of "
    "the monument:", 50)
}
df = {
    'main' : textwrap.fill("After traveling for hours, you find that you have become lost in a thick," \
    "misty wilderness. The trees creek and whisper as you tread on course dirt, and you cant shake the feeling" \
    "that something is watching you. You decide to stop so you don't get more lost: before you there is a hollowed" \
    "tree trunk, to your left, there is a small pit filled with a green, gellatinous substance. [objects: trunk, pit]", 50),

    'trunk': textwrap.fill("You approach the hollow trunk, inside you find a small stach of items:", 50),

    'pit' : textwrap.fill("You approach the pit, and the slimy substance inside it suddenly come to life!" \
    " The slime charges toward you, will you fight it? [enemy: slime]", 50)
}
tr = {}
br = {}
s = {}
at = {}
hh = {}
h = {}
dw = {}
gg= {}
cs = {}

# main world-dictionary
world = {
    'white_hall' : wh,
    'field_of_graves' : fog,
    'dead_forest' : df,
    'tall_rocks' : tr,
    'burned_ruins' : br,
    'sorroweive' : s,
    'abandoned_tower' : at,
    'helmet_high' : hh,
    'helmwind' : h,
    'distant_windlands' : dw,
    'great_gate' : gg,
    'corrupted_spire' : cs,
}