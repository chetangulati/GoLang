
"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def test_params(container, datapath, key_name):
    params = []
    items = set(phantom.collect(container, datapath, scope='all'))
    for item in items:
        params.append({key_name:item}) 
    return params 

# added a function to test the parameters

def on_start(container):
    phantom.debug('on_start() called')
    
    domain_reputation_2(container=container)

    return

def domain_reputation_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('domain_reputation_2() called')

    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.destinationDnsDomain', 'artifact:*.id'])

    parameters = []
    
    for container_item in container_data:
        if container_item[0]:
            parameters.append({
                'domain': container_item[0],
                'context': {'artifact_id': container_item[1]},
            })

    phantom.act("domain reputation", parameters=parameters, assets=['virustotal'], name="domain_reputation_2")

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')

    return
