#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and a_dictionary.get:
        valor = sorted(a_dictionary, reverse=True)
        return (valor[0])
    return None
