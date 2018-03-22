from collections import OrderedDict, namedtuple

base_verse = "This is the house that Jack built."

Pair = namedtuple('Pair', ['subject', 'action'])

pair_list = [
    Pair('malt', 'lay in'),
    Pair('rat', 'ate'),
    Pair('cat', 'killed'),
    Pair('dog', 'worried'),
    Pair('cow with the crumpled horn', 'tossed'),
    Pair('maiden all forlorn', 'milked'),
    Pair('man all tattered and torn', 'kissed'),
    Pair('priest all shaven and shorn', 'married'),
    Pair('rooster that crowed in the morn', 'woke'),
    Pair('farmer sowing his corn', 'kept'),
    Pair('horse and the hound and the horn', 'belonged to'),

]


def _construct_stanza(stanza_num_input):

    constructed_stanza = base_verse

    for stanza_num in range(0, stanza_num_input):
        insert = " {}\nthat {} the".format(pair_list[stanza_num].subject, pair_list[stanza_num].action)
        constructed_stanza = constructed_stanza[:11] + insert + constructed_stanza[11:]

    return constructed_stanza.split('\n')


def recite(start_verse, end_verse):

    song = []

    for i in range(start_verse - 1, end_verse):
        song.extend(_construct_stanza(i))

    return song

