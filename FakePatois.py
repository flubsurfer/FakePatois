import re
import nltk

while 1==1:
	english = raw_input("English: ")
	
	broken_english = english.split()
	
	#CREATE DICTIONARIES
	#verbs = {}
	#pronouns = {thing: ting, something: sintin}
	
	
	
	#SYNTAX
	#analyze effect of words in on the sentence (list) such as "Give those apples to me"
	remove_first_do_in_sentence = "how do you do that? changes to: a how you do that?"
	little_use_of_possessive_pronouns = 'a fi'
	
	#VOCAB
	broken_english = [b.replace('children', 'picny') for b in broken_english]
	broken_english = [b.replace('ur', 'u') for b in broken_english]
	broken_english = [b.replace(" was ", " de ") for b in broken_english]
	broken_english = [b.replace(' they ', ' dem ') for b in broken_english] 
	broken_english = [b.replace("didn't", "no") for b in broken_english]
	broken_english = [b.replace("didnt", "no") for b in broken_english]
	broken_english = [b.replace("did not", "no") for b in broken_english]
	broken_english = [b.replace("wanted", "waa'") for b in broken_english]
	broken_english = [b.replace("them", "dem") for b in broken_english]
	broken_english = [b.replace("what's", "a waa'") for b in broken_english]
	broken_english = [b.replace("what is", "a waa'") for b in broken_english]
	broken_english = [b.replace("whats", "waa'") for b in broken_english]
	broken_english = [b.replace("the others", "dem") for b in broken_english]
	broken_english = [b.replace("where", "a'") for b in broken_english]
	broken_english = [b.replace("I'm", "Mi") for b in broken_english]
	
	#JOIN LIST TO MAKE STRING 
	patois = " ".join(broken_english)

	#PHRASES)
	
	#GRAMMAR
	patois = re.sub(r"[\s]Th" , " D", patois)
	patois = re.sub(r"[\s]th" , " d", patois)
	patois = re.sub(r"[\s]his[\s]" , " him ", patois)
	patois = re.sub(r"[\s]I[\s]" , "Mi ", patois)
	patois = re.sub(r"ing" , "", patois)
	patois = re.sub(r"He[\s]" , "Him ", patois)
	patois = re.sub(r"is not" , "nah", patois)
	patois = re.sub(r"[\s]is[\s]" , " a ", patois)
	patois = re.sub(r"[\s]to[\s]" , " ", patois)
	patois = re.sub(r"ttle" , "kkl", patois)
	patois = re.sub(r"[\s]an[\s]" , "wan", patois)
	#patois = re.sub(r"([Ii]m?)+" , "Mia", patois)
	patois = re.sub(r"ed[\s]" , " ", patois)
	patois = re.sub(r"[\S]th" , "dd", patois)
	patois = re.sub(r"[\s]in[\s]" , " inna ", patois)
	patois = re.sub(r"oul" , "uu", patois)
	patois = re.sub(r"[\s]the[\s]" , " di ", patois)
	patois = re.sub(r"[\s]huh[\s]" , " eeh ", patois)
	patois = re.sub(r"[\s]it[\s]" , " i' ", patois)
	#patois = re.sub(r"[\s]please[\s]" , " eeh ", patois)
	patois = re.sub(r"er[\s]" , "a ", patois)
	#patois = re.sub(r"[\S]er" , "re", patois)
	patois = re.sub(r"es[\s]" , "e ", patois)
	patois = re.sub(r"el[\s]" , "al ", patois)
	patois = re.sub(r"re[\s]" , "a ", patois)
	patois = re.sub(r"[\s]us[\s]" , "we ", patois)
	#patois = re.sub(r"[^hb]ea" , "ay", patois) as is create
	patois = re.sub(r"[^u]ake" , "ek", patois)
	patois = re.sub(r"has[\s]" , "'av ", patois)
	patois = re.sub(r"[Tt]hey[\s]" , "dem ", patois)
	#patois = re.sub(r"[Oo]kay" , "Awoh ", patois)
	#patois = re.sub(r"[Oo]k[\s]" , "Awoh ", patois)
	patois = re.sub(r"'ve[\s]" , " ", patois)
	patois = re.sub(r"[\s]become[\s]" , " ", patois)
	patois = re.sub(r"[Gg]irl[\s]" , "gal ", patois)
	patois = re.sub(r"[\s]us[\s]" , " we ", patois)
	patois = re.sub(r"[\s]am[\s]" , " ", patois)
	patois = re.sub(r"Hello[\s]" , "Wa gwaan ", patois)
	patois = re.sub(r"Hey[\s]" , "Wa gwaan ", patois)
	patois = re.sub(r"Hi[\s]" , "Wa gwaan ", patois)
	patois = re.sub(r"Whats[\s]" , "Wa ", patois)
	patois = re.sub(r"What's[\s]" , "Wa ", patois)
	patois = re.sub(r"[\s][Hh]" , " '", patois)
	patois = re.sub(r"[\s][i]" , " h'i", patois)
	patois = re.sub(r"[\s]a[\s]" , " wan ", patois)
	patois = re.sub(r"[\s]an[\s]" , " ", patois)
	patois = re.sub(r"[\s]and[\s]" , " an' ", patois)
	patois = re.sub(r"[\s]And[\s]" , " An' ", patois)
	patois = re.sub(r"[\s]speak[\s]" , " chat ", patois)
	patois = re.sub(r"[\s]want[\s]" , " waa' ", patois)
	patois = re.sub(r"[\s]will[\s]" , " a' go ", patois)
	patois = re.sub(r"[\s]are[\s]" , " a' go ", patois)
	#patois = re.sub(r"[\S]s[\s]" , " ", patois) there not really any plural words in patois
	patois = re.sub(r"[\s]for[\s]" , " fi ", patois)
	patois = re.sub(r"[\s]does[\s]" , " ", patois)
	patois = re.sub(r"[\s]dont[\s]" , " nuh ", patois)
	patois = re.sub(r"Dont[\s]" , "Dont ", patois)
	
	print "Patois: " + patois








"""
This will use machine translation

Major Rules:
No plural words
No past tense
No 'ing' words

Wrong Sentences:
Give those apples to me
It has to be a balanced portfolio
The beautiful thing about speculation

ToDo
0. Add verbs
 . Add pronouns (something = sintin, thing = ting)
1. Add grammer rules and syntax
2. Make comments for each step
3. Add vocab
4. Check if I can consilate python arguements
5. Make a twitter bot that retweets certain users tweets into patois
6. Make a us english to american app
7. Check patois to english app by entering lyrics to reggae and dancehall songs
8. The free mobile app will only work in Jamaica, if you want it you'll have to pay 5.99



	o = "o"
	u = "u"
	
	o_u = maketrans(o, u)
	patois = patois.translate(o_u)
"""