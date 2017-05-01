from django.shortcuts import render, redirect
import random
from datetime import datetime
# Create your views here.
def index(request):
    if request.session.get('gold') == None:
        request.session['gold'] = 0
        request.session['arrayGold'] = []
    
    return render(request, 'ninjaGold/index.html', )

def process(request):
    if request.method == 'POST':

        if request.POST['building'] == 'farm':
            random_gold = random.randrange(10,21)
            location = 'farm'
            sentence = ("earned " +  str(random_gold) + " golds from the " + location + "!" )
            request.session['arrayGold'].insert(0, {'sentence': sentence})
        if request.POST['building'] == 'cave':
            random_gold= random.randrange(5,11)
            location = 'cave'
            sentence = ("earned " +  str(random_gold) + " golds from the " + location + "!" )
            request.session['arrayGold'].insert(0, {'sentence': sentence})

        if request.POST['building'] == 'house':
            random_gold= random.randrange(2,7)
            location = 'house'
            sentence = ("earned " +  str(random_gold) + " golds from the " + location + "!" )
            request.session['arrayGold'].insert(0, { 'sentence': sentence})

        if request.POST['building'] == 'casino':
            random_gold= random.randrange(-50,51)
            location = 'casino'
            if random_gold < 0:
                color = 'danger'
                sentence = ("Entered a "+location+ " and lost " +str(abs(random_gold)) + " golds... Ouch! ")
                request.session['arrayGold'].insert(0, {'color': color, 'sentence': sentence})

            elif random_gold >= 0:
                color = 'pass'
                sentence = ("earned " +  str(random_gold) +  " golds from  the " + location + "!")
                request.session['arrayGold'].insert(0, {"color": color, "sentence": sentence})
    request.session['gold'] += random_gold

    return redirect('/')
