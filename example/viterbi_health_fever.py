# coding: utf-8
from __future__ import (print_function, unicode_literals)

import sys
sys.path.append('..')

from Pinyin2Hanzi import AbstractHmmParams
from Pinyin2Hanzi import viterbi

class HmmParams(AbstractHmmParams):

    def __init__(self,):

        self.states = ('Healthy', 'Fever')

        self.observations = ('normal', 'cold', 'dizzy')
         
        self.start_probability = {'Healthy': 0.6, 'Fever': 0.4}
         
        self.transition_probability = {
           'Healthy' : {'Healthy': 0.7, 'Fever': 0.3},
           'Fever' : {'Healthy': 0.4, 'Fever': 0.6}
           }
         
        self.emission_probability = {
           'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
           'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
           }

    def start(self, state):
        ''' get start prob of state(hanzi) '''
        return self.start_probability[state]

    def emission(self, state, observation):
        ''' state (hanzi) -> observation (pinyin) '''
        return self.emission_probability[state][observation]

    def transition(self, from_state, to_state):
        ''' state -> state '''
        return self.transition_probability[from_state][to_state]

    def get_states(self, observation):
        ''' get states which produce the given obs '''
        return self.states


result = viterbi(hmm_params=HmmParams(), observations=('normal', 'cold', 'dizzy'), path_num = 10, log = False)
for item in result:
    print(item.score, item.path)

print(20*'--')

result = viterbi(hmm_params=HmmParams(), observations=('normal', 'cold', 'dizzy'), path_num = 2, log = False)
for item in result:
    print(item.score, item.path)

print(20*'--')

result = viterbi(hmm_params=HmmParams(), observations=('normal', 'cold', 'dizzy'), path_num = 1, log = False)
for item in result:
    print(item.score, item.path)

print(20*'--')

result = viterbi(hmm_params=HmmParams(), observations=('normal', 'cold', 'dizzy'), path_num = 1)
for item in result:
    print(item.score, item.path)

print(20*'--')

result = viterbi(hmm_params=HmmParams(), observations=('normal', 'cold', 'dizzy'), path_num = 4, log = True)
for item in result:
    print(item.score, item.path)

print(20*'--')

result = viterbi(hmm_params=HmmParams(), observations=('normal', 'cold', 'dizzy'), path_num = 2, log = True)
for item in result:
    print(item.score, item.path)