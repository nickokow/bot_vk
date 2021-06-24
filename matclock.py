# -*- coding: <UTF-8> -*-
import datetime
from datetime import datetime
import matdict
from matdict import *
def h_n():
    now = datetime.now()
    return now

def h_morph ():
    numwordh = number_to_words(h_n().hour)
    hmorph = morph.parse(numwordh)[0]
    return hmorph
def m_morph():
    numwordm = number_to_words(h_n().minute)
    mmorph = morph.parse(numwordm)[0]
    return mmorph
def mclock():
    resultat =(str(h_morph ().make_agree_with_number(h_n().hour).word) + ' '
           + str(dirt_morph_1().make_agree_with_number(h_n().hour).word) + ' '
           + str(hour_morph().make_agree_with_number(h_n().hour).word) + ' '
           + str(m_morph().make_agree_with_number(h_n().minute).word) + ' '
           + str(dirt_morph_2().make_agree_with_number(h_n().minute).word) + ' '
           + str(minu_morph().make_agree_with_number(h_n().minute).word)
           + ' Уважаемый кожаный мешок!')
    return resultat
