#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class student:
    course = "MSBA7001"
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __str__(self):
        return f"{self.name} earned {self.score} in {self.course}."
    
    def passed(self, cutoff = 75):
        return True if self.score > cutoff else False
    
    def printout(self):
        if self.passed():
            print(f"{self.name} passed the course.")
        else:
            print(f"{self.name} failed the course.")

