#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Bryan Stanley Rijanto
# DATE CREATED: 31 June 2021                        
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules

from os import listdir


def get_pet_labels(image_dir):
    
    filename_list = listdir(image_dir)
    
    results_dic = dict()
    
    items_in_dic = len(results_dic)

    for idx in range(0, len(filename_list), 1):

        if filename_list[idx][0] != ".":

            pet_image = filename_list[idx].lower().split("_")

            pet_name = ""

            for word in pet_image:

                if word.isalpha():

                    pet_name += word + " "

            pet_name = pet_name.strip()
            
            if filename_list[idx] not in results_dic:
                    results_dic[filename_list[idx]] = [pet_name]
            
            else:
                    print("** Warning: Duplicate files exist in directory:", 
                         filename_list[idx])
            
    print (results_dic)
    return results_dic
