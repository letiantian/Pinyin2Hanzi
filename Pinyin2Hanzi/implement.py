# coding: utf-8
from __future__ import (print_function, unicode_literals, absolute_import)

from .interface import AbstractHmmParams, AbstractDagParams
from .util import as_text
import os
import json


DATA    = 'data'
DEFAULT = 'default'

class DefaultHmmParams(AbstractHmmParams):

    def __init__(self,):
        current_dir = self.pwd()
        self.py2hz_dict      = self.readjson(os.path.join(current_dir, 'data', 'hmm_py2hz.json'))
        self.start_dict      = self.readjson(os.path.join(current_dir, 'data', 'hmm_start.json'))
        self.emission_dict   = self.readjson(os.path.join(current_dir, 'data', 'hmm_emission.json'))
        self.transition_dict = self.readjson(os.path.join(current_dir, 'data', 'hmm_transition.json'))

    def readjson(self, filename):
        with open(filename) as outfile:
            return json.load(outfile)

    def pwd(self):
        return os.path.dirname(os.path.abspath(__file__))

    def start(self, state):
        ''' get start prob of state(hanzi) '''
        state = as_text(state)

        data = self.start_dict[DATA]
        default = self.start_dict[DEFAULT]

        if state in data:
            prob = data[state]
        else:
            prob = default
        return float(prob)


    def emission(self, state, observation):
        ''' state (hanzi) -> observation (pinyin) '''
        pinyin = as_text(observation)
        hanzi = as_text(state)

        data = self.emission_dict[DATA]
        default = self.emission_dict[DEFAULT] 

        if hanzi not in data:
            return float( default )
        
        prob_dict = data[hanzi]

        if pinyin not in prob_dict:
            return float( default )
        else:
            return float( prob_dict[pinyin] )

    def transition(self, from_state, to_state):
        ''' state -> state '''
        from_state = as_text(from_state)
        to_state = as_text(to_state)
        prob = 0.0

        data = self.transition_dict[DATA]
        default = self.transition_dict[DEFAULT]

        if from_state not in data:
            return float( default )
        
        prob_dict = data[from_state]

        if to_state in prob_dict:
            return float( prob_dict[to_state] )
        
        if DEFAULT in prob_dict:
            return float( prob_dict[DEFAULT] )

        return float( default )

    def get_states(self, observation):
        ''' get states which produce the given obs '''
        return [hanzi for hanzi in self.py2hz_dict[observation]]



class DefaultDagParams(AbstractDagParams):

    def __init__(self,):
        current_dir = self.pwd()
        self.char_dict      = self.readjson(os.path.join(current_dir, 'data', 'dag_char.json'))
        self.phrase_dict    = self.readjson(os.path.join(current_dir, 'data', 'dag_phrase.json'))

    def readjson(self, filename):
        with open(filename) as outfile:
            return json.load(outfile)

    def pwd(self,):
        return os.path.dirname(os.path.abspath(__file__))

    def get_phrase(self, pinyin_list, num=6):
        ''' pinyin_list是拼音组成的list，例如['yi', 'ge'] '''
        if len(pinyin_list) == 0:
            return []
        if len(pinyin_list) == 1:
            data = self.char_dict
        else:
            data = self.phrase_dict

        pinyin = ','.join(pinyin_list)

        if pinyin not in data:
            return []

        return data[pinyin][:num]
        

