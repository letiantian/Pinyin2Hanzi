# coding: utf-8
from __future__ import (print_function, unicode_literals, absolute_import)

from .interface import AbstractHmmParams
from .priorityset import PrioritySet
import math

def viterbi(hmm_params, observations, path_num=6, log=False, min_prob=3.14e-200):

    assert( isinstance(hmm_params, AbstractHmmParams) )

    V = [{}]
    t = 0
    cur_obs = observations[t]
    
    # Initialize base cases (t == 0)
    prev_states = cur_states = hmm_params.get_states(cur_obs)  # wordset
    for state in cur_states:
        if log:
            __score   = math.log(max(hmm_params.start(state), min_prob)) + \
                math.log(max(hmm_params.emission(state, cur_obs), min_prob))
        else:
            __score   = max(hmm_params.start(state), min_prob) * \
                max(hmm_params.emission(state, cur_obs), min_prob)
        __path    = [state]
        V[0].setdefault(state, PrioritySet(path_num))
        V[0][state].put(__score, __path)

    
    # Run Viterbi for t > 0
    for t in range(1, len(observations)):
        cur_obs = observations[t]

        if len(V) == 2:
            V = [V[-1]]

        V.append({})

        prev_states = cur_states
        cur_states = hmm_params.get_states(cur_obs)

        for y in cur_states:
            V[1].setdefault( y, PrioritySet(path_num) )
            max_item = None
            for y0 in prev_states:  # from y0(t-1) to y(t)
                for item in V[0][y0]:
                    if log:
                        _s = item.score + \
                            math.log(max(hmm_params.transition(y0, y), min_prob)) + \
                            math.log(max(hmm_params.emission(y, cur_obs), min_prob))
                    else:
                        _s = item.score * \
                            max(hmm_params.transition(y0, y), min_prob) * \
                            max(hmm_params.emission(y, cur_obs), min_prob)

                    _p = item.path + [y]
                    V[1][y].put(_s, _p)

    result = PrioritySet(path_num)
    for last_state in V[-1]:
        for item in V[-1][last_state]:
            result.put(item.score, item.path)
    result = [item for item in result]

    return sorted(result, key=lambda item: item.score, reverse=True)