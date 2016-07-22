# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 09:19:21 2016

@author: lyyssmsk
"""
import knowledgebase
import localization
import classification

class KBarchitecture:
    __input=0
    def __init__(self,input):  
        self.__input=input
    
    def train(name,input_trainset):
        attr_name=knowledgebase.search(name=name)
        attr1=localization.train(attr_name=attr_name,trainset=input_trainset)
        eigen1=classification.train(trainset=input_trainset)
        knowledgebase.add(name=name,attr=attr1,eigen=eigen1)
    
    def fine_grained(input_image):
        area1=localization.locate(input_image)
        eigen1=classification.classify(area1)
        [name1 ,attr1]=knowledgebase.search(eigen=eigen1)
        area2=localization.locate(input_image,attr1)
        eigen2=classification.classify(area1,area2)
        result=knowledgebase.search(name=name1,eigen=eigen1,feature=eigen2)
        return result
        
        
    #def zero_shot:
        
    #def image_caption:
        
    
        

KBarchitecture.train
print 'hello knowledge base'
