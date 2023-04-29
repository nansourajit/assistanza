import streamlit as st
import random
import Rearrange



d=0
c=0
word = ["Excellent","cat","rat","Parrot","axe","chocolate", "sun", 'rainbow', 
            'computer', 'science', 'programming','mathematics', 'player', 'condition', 'reverse','water', 'board',
            'baby', 'back', 'bad', 'bag', 'ball', 'bank', 'base', 'basket', 'bath','bean', 'bear', 
            'beautiful', 'bed', 'bedroom', 'beer', 'behave', 'before', 'begin', 
            'behind', 'bell', 'below', 'besides', 'best', 'better', 'between', 'big', 'bird', 
            'birth', 'birthday', 'bit', 'bite', 'black', 'bleed', 'block', 'blood', 'blow', 'blue', 
            'board', 'boat', 'body', 'boil', 'bone', 'book', 'border', 'born', 'borrow', 'both', 'bottle', 'bottom', 
            'bowl', 'box', 'boy', 'branch', 'brave', 'bread', 'break', 'breakfast', 'breathe', 'bridge', 'bright', 'bring', 
            'brother', 'brown', 'brush', 'build', 'burn', 'business', 'bus', 'busy', 'page', 'pain', 'paint','pair', 'pan', 'paper', 'parent', 'park', 
            'part', 'partner', 'party', 'pass', 'past', 'path', 'pay', 'peace', 'pen', 'pencil', 'people', 'pepper', 'perfect', 'period', 
            'person', 'petrol', 'photograph', 'piano', 'pick', 'picture', 'piece', 'pig', 'pin', 'pink', 'place', 'plane', 'plant', 'plastic', 'plate', 
            'play', 'please',  'plenty', 'pocket', 'point', 'poison', 'police', 'polite', 'pool', 'poor', 'popular', 'position', 
            'possible', 'potato', 'pour', 'power', 'present', 'press', 'pretty', 'prevent', 'price', 'prince', 'prison', 'private', 'prize', 'probably', 
            'problem', 'produce', 'promise', 'proper', 'protect', 'provide', 'public', 'pull', 'punish', 'pupil', 'push','sad', 'safe', 'sail', 
            'salt', 'same', 'sand', 'save', 'say', 'school', 'science', 'scissors', 
            'search', 'seat', 'second', 'see', 'seem', 'sell', 'send', 'sentence', 
            'serve', 'seven', 'several', 'sex', 'shade', 'shadow', 'shake', 'shape', 'share', 'sharp', 'she', 'sheep', 'sheet', 'shelf', 'shine', 'ship', 
            'shirt', 'shoe', 'shoot', 'shop', 'short', 'should', 'shoulder', 'shout', 'show', 'sick', 'side', 'signal', 'silence', 'silly', 'silver', 'similar', 'simple', 
            'single', 'since', 'sing', 'sink', 'sister', 'sit', 'six', 'size', 'skill', 'skin', 'skirt', 'sky', 'sleep', 'slip', 'slow', 'small', 
            'smell', 'smile', 'smoke', 'snow', 'so', 'soap', 'sock', 'soft', 'some', 'someone', 'something', 'sometimes', 'son', 'soon', 'sorry', 'sound', 'soup', 'south', 'space', 'speak', 'special', 'speed', 'spell', 'spend', 'spoon', 'sport', 'spread', 'spring', 'square', 'stamp', 'stand', 'star', 
            'start', 'station', 'stay', 'steal', 'steam', 'step', 'still', 'stomach', 'stone', 'stop', 'store', 'storm', 'story', 'strange', 'street', 'strong', 'structure', 'student', 'study', 'stupid', 'subject', 'substance', 'successful', 'such', 'sudden', 'sugar', 'suitable', 'summer', 'sun', 'sunny', 
            'support', 'sure', 'surprise', 'sweet', 'swim', 'sword', 'ladder', 'lady', 'lamp', 'land', 'large', 'last', 'late', 'lately', 'laugh', 'lazy', 'lead', 'leaf', 'learn', 'leave', 'leg', 'left', 'lend', 'length', 'less', 
            'lesson', 'let', 'letter', 'library', 'lie', 'life', 'light', 'like', 'lion', 'lip', 'list', 'listen', 'little', 'live', 'lock', 'lonely', 'long', 'look', 'lose', 'lot', 'love', 'low', 'lower', 'luck',
            'cake', 'call', 'can', 'candle', 'cap', 'car', 'card', 'care', 'careful', 'careless', 'carry', 'case', 'cat', 'catch', 'central', 'century', 'certain', 'chair', 'chance', 'change', 'chase', 'cheap', 'cheese', 'chicken', 'child', 'children', 'chocolate', 'choice', 'choose',
            'circle', 'city', 'class', 'clever', 'clean', 'clear', 'climb', 'clock', 'cloth', 'clothes', 'cloud', 'cloudy', 'close', 'coffee', 'coat', 'coin', 'cold', 'collect', 'colour', 'comb', 'comfortable', 'common', 'compare', 'come', 'complete', 'computer', 'condition', 'continue', 'control', 'cook', 'cool', 'copper', 'corn','corner', 'correct', 'cost', 'contain', 'count', 'country', 'course', 'cover', 'crash',
            'cross', 'cry', 'cup', 'cupboard', 'cut']
a=random.choice(word)
shuffled = list(a)
random.shuffle(shuffled)
shuffled = ''.join(shuffled)


def check2(val):
    global c,a,shuffled,d
    d+=1
    if(val==a):
        c+=1
        st.success("Correct:smiley:")
        st.info(c)
        a=word[random.randint(1,150)]
        shuffled = list(a)
        random.shuffle(shuffled)
        shuffled = ''.join(shuffled)
        st.warning("Next word :point_down: :")
        st.info(shuffled)
        Rearrange()
        
    if(val!=a):
        d=0
        st.error("Wrong!:white_frowning_face: The Correct word was: ")
        st.error(a)
        st.warning("Your current score is:")
        st.info(c)
        st.error("Game Over! Click on End and then uncheck to play again! :pensive:")
        st.info("You can also restart and continue by correcting the word again :blush:")
        c=0
        

