#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Quick & dirty helper to dump instagram json into frontmatter format for
ristrettogram.
"""

import requests
import json
import six

import yaml

try:
    from yaml import CSafeDumper as SafeDumper
except ImportError:
    from yaml import SafeDumper

CLIENT_ID = ''

FM_TEMPLATE = """\
---
{metadata}
---
"""

def u(text, encoding='utf-8'):
    "Return unicode text, no matter what"

    if isinstance(text, six.binary_type):
        return text.decode(encoding)

    # it's unicode, bro
    return text


def dumps(post, **kwargs):
    """
    Serialize post to a string and return text.
    """
    kwargs.setdefault('Dumper', SafeDumper)
    kwargs.setdefault('default_flow_style', False)

    metadata = yaml.dump(post, **kwargs).strip()
    metadata = u(metadata)  # ensure unicode
    return FM_TEMPLATE.format(metadata=metadata, content='').strip()


def get_posts(keyword, max_id=None, min_id=None):
    """
    returns frontmatter-ish data for the city files.

    link_shortcode:
    cafe_name:
    width:
    height:
    cover_image:
    video_url_high:
    video_url_low:
    user_name:
    user_image:
    created_time:
    latitude:
    longitude:
    cafe_name_ig:
    """
    url = 'https://api.instagram.com/v1/tags/%s/media/recent/' % keyword
    url += '?client_id=%s' % CLIENT_ID
    if max_id:
        url += '&max_tag_id=%s' % max_id
    if min_id:
        url += '&min_tag_id=%s' % min_id
    djson = json.loads(requests.get(url).content)
    results = []
    for post in djson['data']:
        latitude = ''
        longitude = ''
        cafe_name_ig = ''
        result = {
            # 'id' : post['id'],
            'cafe_name': 'ADD CAFE NAME',
            'user_name': post['user']['username'],
            'user_image': post['user']['profile_picture'],
            'cover_image': post['images']['standard_resolution']['url'],
            'link_shortcode': post['link'].split('/')[-2],
            'created_time': post['created_time'],
        }

        if post['type'] == 'video' and 'videos' in post:
            result['video_url_low'] = post['videos']['low_resolution']['url']
            result['video_url_high'] = post['videos']['standard_resolution']['url']
            result['width'] = post['videos'][ 'standard_resolution']['width']
            result['height'] = post['videos'][ 'standard_resolution']['height']

        if post['location']:
            result['latitude'] = post['location']['latitude']
            result['ongitude'] = post['location']['longitude']
            result['cafe_name_ig'] = post['location']['name']
        results.append(result)
    return results


if __name__ == '__main__':
    posts = get_posts('ristrettogram')
    for p in posts:
        print dumps(p)
