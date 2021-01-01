text = "banana - mashed	227,barley - cooked	215,barley - flake	92,barley - flour	85,barley - pearled	213,berrie - frozen	142,blueberrie - dried	156,blueberrie - fresh	170,blueberry - juice	241,bran - cereal	60,bread - crumb	112,bread - japanese	50,bread - panko	50,buckwheat - flour	120,buckwheat - whole	170,bulgur - default	152,butter - default 	226,buttermilk - default	227,buttermilk - powder	144,cacao - nib	120,caramel - piece	284,caraway - seed	144,carrot - diced	142,carrot - grated	99,carrot - puréed	256,carrot - pureed	256,cashew - chopped\t113,cashew - whole	113,celery - diced	142,cheddar - cheese\t113,cherrie - candied	200,cherrie - chopped	160,cherrie - dried	142,cherrie - frozen	113,cherrie - pitted	160,chickpea - flour	85,chive - defalt	42,chocolate - mini	177,chocolate - chip	170,chocolate - chopped	170,chocolate - chunk	170,cinnamon - sugar	200,cocoa - unsweetened	84,coconut - desiccated	85,coconut - flake	60,coconut - flour	128,coconut - oil	226,coconut - powder	114,coconut - shredded	53,coconut - sugar	154,coconut - sweetened	85,coconut - toasted	85,corn - popped	5.25,corn - syrup	312,cornmeal - coarse	163,cornmeal - quaker	156,cornmeal - whole	138,cornmeal - yellow	156,cornstarch - default\t112,cranberrie - dried	114,cranberrie - fresh	99,cream - heavy	227,currant - default	142,date - chopped	149,espresso - powder	112,feta - default	114,fig - dried	149,flax - meal	100,flaxseed - default	140,flour - almond	96,flour - amaranth	103,flour - ap	120,flour - barley	85,flour - bread	120,flour - buckwheat	120,flour - cake	120,flour - chickpea	85,flour - coconut	128,flour - durum	124,flour - gluten-free	156,flour - gluten	156,flour - oat	92,flour - pizza	116,flour - potato	184,flour - quinoa	110,flour - rice 	135,flour - rye	106,flour - self-rising	113,flour - rising	113,flour - spelt	99,flour - tapioca	113,flour - wheat	113,flour - hazelnut	89,garlic - minced	224,garlic - peeled and sliced	149,ginger - crystallized	184,ginger - sliced	228,graham - crumb	99,graham - crushed	142,granola - default	113,hazelnut - flour	89,hazelnut - spread	320,hazelnut - whole	142,honey - default	336,jack - default	113,jam - default	340,lard - default	226,leek - diced	92,lemon - powder	144,lime - juice	227,lime - powder	144,macadamia - nut	149,malt - syrup	344,malted - powder	140,maple - syrup	312,marshmallow - crème	85,marshmallow - creme	85,marshmallow - cream	85,marshmallow - fluff	128,marshmallows - mini	43,marzipan - default	290,mascarpone - default	227,mayo - default	226,mayonnaise - default	226,milk - condensed 	312,milk - powdered	112,milk - evaporated	226,milk - fresh	227,millet - default	206,molasses - default	340,mozzarella - default	113,mushroom - default\t78,oat - bran	106,oat - flour	92,oat - steel	140,oat - normal	89,olive - oil	200,olive - sliced	142,onion - diced	142,parmesan - default\t100,peache - diced	170,peanut - butter	270,peanut - whole	142,pear - diced	163,pecan - diced	114,peel - candied	170,pepper - bell	142,pesto - default\t224,pine - nut	142,pineapple - dried	142,pineapple - fresh	170,pistachio - paste	312,pistachio - shelled	120,polenta	- default 163,poppy - seeds	144,potato - flour	184,potato - starch	152,potatoe - mashed	213,preserve - default\t340,pumpkin - purée	227,pumpkin - puree	227,quinoa - cooked	184,quinoa - flour	110,quinoa - whole	177,raisin - loose	149,raisin - packed	170,raspberrie - fresh	120,rhubarb - default\t120,rice - cooked	170,rice - dry	198,rice - flour	135,rice - krispies	28,ricotta - default\t227,rye - default	124,salt - diamond	128,salt - morton'	256,salt - morton	256,salt - table	288,scallion - sliced	64,sesame - seed	142,shallot	- default 156,strawberrie - sliced	167,sugar - brown	213,sugar - castor	190,sugar - cinnamon	200,sugar - coconut	154,sugar - confectioner	113.5,sugar - demerara	220,sugar - superfine	190,sugar - turbinado	180,sugar - white	198,sunflower - default	140,swis - default\t113,tahini - default\t256,tapioca -  starch	113,tapioca - flour	113,tapioca - quick	168,toffee - default	156,tomatoe - sundried	170,vanilla - default\t224,vegetable - oil\t198,vegetable - shortening\t184,walnut - chopped\t113,walnut - whole\t128,water - default\t227,wheat - cracked\t149,yeast - default	\t50,yogurt - default\t227,zucchini - default\t140"

textList = text.split(",")

category = ""
output = open("textRead.txt","w")
for entry in textList:
    newCategory = entry.split('-')[0].strip()
    if(category != newCategory):
        category = newCategory
        output.write("], \"" + category + "\": [")
    descriptor = entry.split(' ')[2].split('\t')[0]
    output.write("\"" + descriptor + "\":")
    weight = entry.split('\t')[1]
    output.write(weight+",")

{
  "almond": {
    "flour": 96,
    "meal": 84,
    "paste": 259,
    "sliced": 86,
    "slivered": 114,
    "whole": 142,
    "default": 86
  },
  "apple": {
    "default": 113,
    "dried": 85,
    "sliced": 113
  },
  "applesauce": {
    "default": 255
  },
  "apricot": {
    "dried": 128,
    "default": 128
  },
  "baking": {
    "default": 288,
    "powder": 192,
    "soda": 288
  },
  "banana": {
    "default": 227,
    "mashed": 227
  },
  "barley": {
    "default": 215,
    "cooked": 215,
    "flake": 92,
    "flour": 85,
    "pearled": 213
  },
  "berrie": {
    "default": 142,
    "frozen": 142
  },
  "blueberrie": {
    "default": 170,
    "dried": 156,
    "fresh": 170
  },
  "blueberry": {
    "default": 241,
    "juice": 241
  },
  "bran": {
    "default": 60,
    "cereal": 60
  },
  "bread": {
    "default": 50,
    "crumb": 112,
    "japanese": 50,
    "panko": 50
  },
  "buckwheat": {
    "default": 120,
    "flour": 120,
    "whole": 170
  },
  "bulgur": {
    "default": 152
  },
  "butter": {
    "default": 226
  },
  "buttermilk": {
    "default": 227,
    "powder": 144
  },
  "cacao": {
    "default": 120,
    "nib": 120
  },
  "caramel": {
    "default": 284,
    "piece": 284
  },
  "caraway": {
    "default": 144,
    "seed": 144
  },
  "carrot": {
    "default": 142,
    "diced": 142,
    "grated": 99,
    "puréed": 256,
    "pureed": 256
  },
  "cashew": {
    "default": 113,
    "chopped": 113,
    "whole": 113
  },
  "celery": {
    "default": 142,
    "diced": 142
  },
  "cheddar": {
    "default": 113,
  },
  "cherrie": {
    "default": 160,
    "candied": 200,
    "chopped": 160,
    "dried": 142,
    "frozen": 113,
    "pitted": 160
  },
  "chickpea": {
    "default": 85,
    "flour": 85
  },
  "chive": {
    "defalt": 42
  },
  "chocolate": {
    "default": 170,
    "mini": 177,
    "chip": 170,
    "chopped": 170,
    "chunk": 170
  },
  "cinnamon": {
    "default": 200,
    "sugar": 200
  },
  "cocoa": {
    "default": 84,
    "unsweetened": 84
  },
  "coconut": {
    "default": 85,
    "desiccated": 85,
    "flake": 60,
    "flour": 128,
    "oil": 226,
    "powder": 114,
    "shredded": 53,
    "sugar": 154,
    "sweetened": 85,
    "toasted": 85
  },
  "corn": {
    "default": 5.25,
    "popped": 5.25,
    "syrup": 312
  },
  "cornmeal": {
    "default": 156,
    "coarse": 163,
    "quaker": 156,
    "whole": 138,
    "yellow": 156
  },
  "cornstarch": {
    "default": 112
  },
  "cranberrie": {
    "default": 99,
    "dried": 114,
    "fresh": 99
  },
  "cream": {
    "default": 227,
    "heavy": 227
  },
  "currant": {
    "default": 142
  },
  "date": {
    "default": 149,
    "chopped": 149
  },
  "espresso": {
    "default": 112,
    "powder": 112
  },
  "feta": {
    "default": 114
  },
  "fig": {
   "default": 149,
    "dried": 149
  },
  "flax": {
   "default": 100,
    "meal": 100
  },
  "flaxseed": {
    "default": 140
  },
  "flour": {
   "default": 120,
    "almond": 96,
    "amaranth": 103,
    "ap": 120,
    "all": 120,
    "barley": 85,
    "bread": 120,
    "buckwheat": 120,
    "cake": 120,
    "chickpea": 85,
    "coconut": 128,
    "durum": 24,
    "gluten-free": 156,
    "gluten": 156,
    "oat": 92,
    "pizza": 116,
    "potato": 184,
    "quinoa": 110,
    "rice": 135,
    "rye": 106,
    "self-rising": 113,
    "rising": 113,
    "spelt": 99,
    "tapioca": 113,
    "wheat": 113,
    "hazelnut": 89
  },
  "garlic": {
   "default": 224,
    "minced": 224,
    "peeled": 149
  },
  "ginger": {
   "default": 228,
    "crystallized": 184,
    "sliced": 228
  },
  "graham": {
   "default": 142,
    "crumb": 99,
    "crushed": 142
  },
  "granola": {
    "default": 113
  },
  "hazelnut": {
   "default": 142,
    "flour": 89,
    "spread": 320,
    "whole": 142
  },
  "honey": {
    "default": 336
  },
  "jack": {
    "default": 113
  },
  "jam": {
    "default": 340
  },
  "lard": {
    "default": 226
  },
  "leek": {
   "default": 92,
    "diced": 92
  },
  "lemon": {
   "default": 144,
    "powder": 144
  },
  "lime": {
   "default": 227,
    "juice": 227,
    "powder": 144
  },
  "macadamia": {
   "default": 149,
    "nut": 149
  },
  "malt": {
    "syrup": 344,
    "default": 140,
    "powder": 140
  },
  "malted": {
    "syrup": 344,
    "default": 140,
    "powder": 140
  },
  "maple": {
    "default": 312,
    "syrup": 312
  },
  "marshmallow": { 
    "default": 43,  
    "crème": 85,
    "creme": 85,
    "cream": 85,
    "fluff": 128,
    "mini": 43
  },
  "marzipan": {
    "default": 290
  },
  "mascarpone": {
    "default": 227
  },
  "mayo": {
    "default": 226
  },
  "mayonnaise": {
    "default": 226
  },
  "milk": {
    "default": 227,
    "condensed": 312,
    "powdered": 112,
    "evaporated": 226,
    "fresh": 227
  },
  "millet": {
    "default": 206
  },
  "molasses": {
    "default": 340
  },
  "mozzarella": {
    "default": 113
  },
  "mushroom": {
    "default": 78
  },
  "oat": {
    "default": 89,
    "bran": 106,
    "flour": 92,
    "steel": 140,
    "normal": 89
  },
  "olive": {
    "default": 200,
    "oil": 200,
    "sliced": 142
  },
  "onion": {
    "default": 142,
    "diced": 142
  },
  "parmesan": {
    "default": 100
  },
  "peache": {
    "default": 170,
    "diced": 170
  },
  "peanut": {
    "default": 142,
    "butter": 270,
    "whole": 142
  },
  "pear": {
    "default": 163,
    "diced": 163
  },
  "pecan": {
    "default": 114,
    "diced": 114
  },
  "peel": {
    "default": 170,
    "candied": 170
  },
  "pepper": {
    "default": 142,
    "bell": 142
  },
  "pesto": {
    "default": 224
  },
  "pine": {
    "default": 142,
    "nut": 142
  },
  "pineapple": {
    "default": 170,
    "dried": 142,
    "fresh": 170
  },
  "pistachio": {
    "default": 120,
    "paste": 312,
    "shelled": 120
  },
  "polenta": {
    "default": 163
  },
  "poppy": {
    "default": 144,
    "seeds": 144
  },
  "potato": {
    "default": 152,
    "flour": 184,
    "starch": 152
  },
  "potatoe": {
    "default": 213,
    "mashed": 213
  },
  "preserve": {
    "default": 340
  },
  "pumpkin": {
    "default": 227,
    "purée": 227,
    "puree": 227
  },
  "quinoa": {
    "default": 177,
    "cooked": 184,
    "flour": 110,
    "whole": 177
  },
  "raisin": {
    "default": 149,
    "loose": 149,
    "packed": 170
  },
  "raspberrie": {
    "default": 120,
    "fresh": 120
  },
  "rhubarb": {
    "default": 120
  },
  "rice": {
    "default": 198,
    "cooked": 170,
    "dry": 198,
    "flour": 135,
    "krispies": 28
  },
  "ricotta": {
    "default": 227
  },
  "rye": {
    "default": 124
  },
  "salt": {
    "default": 256,
    "diamond": 128,
    "morton'": 256,
    "morton": 256,
    "table": 288
  },
  "scallion": {
    "default": 64,
    "sliced": 64
  },
  "sesame": {
    "default": 142,
    "seed": 142
  },
  "shallot": {
    "default": 156
  },
  "strawberrie": {
    "default": 167,
    "sliced": 167
  },
  "sugar": {
    "default": 198,
    "brown": 213,
    "castor": 190,
    "cinnamon": 200,
    "coconut": 154,
    "confectioner": 113.5,
    "demerara": 220,
    "superfine": 190,
    "turbinado": 180,
    "white": 198
  },
  "sunflower": {
    "default": 140
  },
  "swis": {
    "default": 113
  },
  "tahini": {
    "default": 256
  },
  "tapioca": {
    "default": 168,
    "starch": 113,
    "flour": 113,
    "quick": 168
  },
  "toffee": {
    "default": 156
  },
  "tomatoe": {
    "default": 170,
    "sundried": 170
  },
  "vanilla": {
    "default": 224
  },
  "vegetable": {
    "default": 198,
    "oil": 198,
    "shortening": 184
  },
  "walnut": {
    "default": 113,
    "chopped": 113,
    "whole": 128
  },
  "water": {
    "default": 227
  },
  "wheat": {
    "default": 149,
    "cracked": 149
  },
  "yeast": {
    "default": 150
  },
  "yogurt": {
    "default": 227
  },
  "zucchini": {
    "default": 140
  }
}