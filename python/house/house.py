from collections import namedtuple

base_verse = "This is the house that Jack built."

SubjectActionPair = namedtuple('SubjectActionPair', ['subject', 'action'])

pair_list = [
    SubjectActionPair('malt', 'lay in'),
    SubjectActionPair('rat', 'ate'),
    SubjectActionPair('cat', 'killed'),
    SubjectActionPair('dog', 'worried'),
    SubjectActionPair('cow with the crumpled horn', 'tossed'),
    SubjectActionPair('maiden all forlorn', 'milked'),
    SubjectActionPair('man all tattered and torn', 'kissed'),
    SubjectActionPair('priest all shaven and shorn', 'married'),
    SubjectActionPair('rooster that crowed in the morn', 'woke'),
    SubjectActionPair('farmer sowing his corn', 'kept'),
    SubjectActionPair('horse and the hound and the horn', 'belonged to'),
]


def construct_stanza(stanza_num_input):

    constructed_stanza = base_verse

    for stanza_num in range(0, stanza_num_input):
        insert = " {}\nthat {} the".format(pair_list[stanza_num].subject, pair_list[stanza_num].action)
        constructed_stanza = constructed_stanza[:11] + insert + constructed_stanza[11:]

    return constructed_stanza.split('\n')


def recite(start_verse, end_verse):

    song = []

    for i in range(start_verse - 1, end_verse):
        song.extend(construct_stanza(i))
        song.append("")

    return song[:-1]

