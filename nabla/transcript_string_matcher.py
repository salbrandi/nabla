# -*- coding: utf-8 -*-
import requests
import sys, os

pre_string = '"transcript":"'
transcript_chunk_list = []


def extract_transcript(transcript):
    for ind, char in enumerate(transcript):
        chunk = ''
        selection = transcript[ind-len(pre_string):ind]
        if selection == pre_string:
            for c in transcript[ind:]:
                if c != '"':
                    chunk = chunk + c
                else:
                    break
            transcript_chunk_list.append(chunk)
    return(transcript_chunk_list)


def format_transcript(input_list):
    transcript = ''
    for chunk in input_list:
        if chunk[len(chunk)-1] == '\\':
            chunk = chunk[:len(chunk)-2]
        formatted_chunk = bytes(chunk, 'utf-8').decode('unicode_escape')
        transcript = transcript + ' ' + formatted_chunk
    for cnum, char in enumerate(transcript):
        if cnum % 100 == 0:
            transcript ='{0}<br>{1}'.format(transcript[:cnum], transcript[cnum:])
    html_transcript = '<p>' + transcript + '</p>'

    return(html_transcript)
