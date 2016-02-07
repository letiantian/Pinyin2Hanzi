# coding: utf-8

class AbstractHmmParams(object):
    
    def start(self, state):
        ''' get start prob of state(hanzi) '''
        pass

    def emission(self, state, observation):
        ''' state (hanzi) -> observation (pinyin) '''
        pass

    def transition(self, from_state, to_state):
        ''' state -> state '''
        pass

    def get_states(self, observation):
        ''' get states which produce the given obs '''
        pass

class AbstractDagParams(object):

    def get_phrase(self, pinyin_list, num):
        pass