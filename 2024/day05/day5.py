# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:33:40 2024

@author: tanou
"""

def add_rule(rules: list[tuple[str]], new_rule: str) -> None:
    numbers = tuple(new_rule.split("|"))
    if not numbers in rules:
        rules.append(numbers)

def test_update(rules: list[tuple[str]], update: list[str]) -> bool:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0])>update.index(rule[1]):
                return False
    return True

def fix_update(rules: list[tuple[str]], update: list[str]) -> bool:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0])>update.index(rule[1]):
                update[update.index(rule[0])], update[update.index(rule[1])] = update[update.index(rule[1])], update[update.index(rule[0])]
                if not test_update(rules, update):
                    fix_update(rules, update)

result: int = 0
result2: int = 0

file_name: str = "input1.txt"
with open(file_name, "r") as file:
    rule_phase: bool = True
    rules: list[tuple[str]] = []
    
    for line in file:
        line = line.strip()
        if line=="":
            rule_phase = False
            continue
        
        if rule_phase:
            add_rule(rules, line)
            
        else:
            update = line.split(",")
            if test_update(rules, update):
                result += int(update[len(update)//2])
            else:
                fix_update(rules, update)
                result2 += int(update[len(update)//2])

print(result, result2)