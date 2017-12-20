from MaltegoTransform import *
import requests
import json
import re

apiurl = "https://www.virustotal.com/vtapi/v2/"
apikey = "<Your API Key>"


# c2host_to_hash
def c2host_to_hash():
    try:
        params = {'apikey': apikey, 'query': 'behaviour:' + data}
        response = requests.post(apiurl + 'file/search', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'hashes' in response_json:
                for item in response_json['hashes']:
                    me = mt.addEntity("maltego.Hash", '%s' % item)
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# host_to_downloadedhash
def host_to_downloadedhash():
    try:
        params = {'apikey': apikey, 'domain': data}
        response = requests.get(apiurl + 'domain/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'detected_downloaded_samples' in response_json:
                for item in response_json['detected_downloaded_samples']:
                    me = mt.addEntity("maltego.Hash", '%s' % item['sha256'])
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# c2ip_to_hash
def c2ip_to_hash():
    try:
        params = {'apikey': apikey, 'query': 'behaviour:' + data}
        response = requests.post(apiurl + 'file/search', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'hashes' in response_json:
                for item in response_json['hashes']:
                    me = mt.addEntity("maltego.Hash", '%s' % item)
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# ip_to_downloadedhash
def ip_to_downloadedhash():
    try:
        params = {'apikey': apikey, 'ip': data}
        response = requests.get(apiurl + 'ip-address/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'detected_downloaded_samples' in response_json:
                for item in response_json['detected_downloaded_samples']:
                    me = mt.addEntity("maltego.Hash", '%s' % item['sha256'])
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# domain_to_ip
def domain_to_ip():
    try:
        params = {'apikey': apikey, 'domain': data}
        response = requests.get(apiurl + 'domain/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'resolutions' in response_json:
                for item in response_json['resolutions']:
                    me = mt.addEntity("maltego.IPv4Address", '%s' % item['ip_address'])
                    me.setLinkLabel("VT PassiveDNS")

    except:
        return False

    return mt

# ip_to_domain
def ip_to_domain():
    try:
        params = {'apikey': apikey, 'ip': data}
        response = requests.get(apiurl + 'ip-address/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'resolutions' in response_json:
                for item in response_json['resolutions']:
                    me = mt.addEntity("maltego.Domain", '%s' % item['hostname'])
                    me.setLinkLabel("VT PassiveDNS")

    except:
        return False

    return mt

# hash_to_c2host
def hash_to_c2host():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'dns' in response_json['additional_info']['behaviour-v1']['network']:
                for item in response_json['additional_info']['behaviour-v1']['network']['dns']:
                    me = mt.addEntity("maltego.Domain", '%s' % item['hostname'])
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# hash_to_c2ip
def hash_to_c2ip():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'network' in response_json['additional_info']['behaviour-v1']:
                for item in response_json['additional_info']['behaviour-v1']['network']['tcp']:
                    item = re.sub(r':[0-9]{1,5}', '', item)
                    me = mt.addEntity("maltego.IPv4Address", '%s' % item)
                    me.setLinkLabel("VT")
                for item in response_json['additional_info']['behaviour-v1']['network']['dns']:
                    me = mt.addEntity("maltego.IPv4Address", '%s' % item['ip'])
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# hash_to_c2url
def hash_to_c2url():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
#            if 'http' in response_json['additional_info']['behaviour-v1']['network']:
            if response_json['additional_info']['behaviour-v1']['network']['http']:
                for item in response_json['additional_info']['behaviour-v1']['network']['http']:
                    me = mt.addEntity("maltego.Domain", '%s' % item['url'])
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# hash_to_avdetection
def hash_to_avdetection():
    try:
        params = {'apikey': apikey, 'resource': data}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'Microsoft' in response_json['scans']:
                if response_json['scans']['Microsoft']['detected']:
                    me = mt.addEntity("maltego.Avdetection", '%s' % response_json['scans']['Microsoft']['result'])
                    me.setLinkLabel("VT Microsoft")
            if 'TrendMicro' in response_json['scans']:
                if response_json['scans']['TrendMicro']['detected']:
                    me = mt.addEntity("maltego.Avdetection", '%s' % response_json['scans']['TrendMicro']['result'])
                    me.setLinkLabel("VT TrendMicro")
            if 'Kaspersky' in response_json['scans']:
                if response_json['scans']['Kaspersky']['detected']:
                    me = mt.addEntity("maltego.Avdetection", '%s' % response_json['scans']['Kaspersky']['result'])
                    me.setLinkLabel("VT Kaspersky")
            if 'Sophos' in response_json['scans']:
                if response_json['scans']['Sophos']['detected']:
                    me = mt.addEntity("maltego.Avdetection", '%s' % response_json['scans']['Sophos']['result'])
                    me.setLinkLabel("VT Sophos")
            if 'ESET-NOD32' in response_json['scans']:
                if response_json['scans']['ESET-NOD32']['detected']:
                    me = mt.addEntity("maltego.Avdetection", '%s' % response_json['scans']['ESET-NOD32']['result'])
                    me.setLinkLabel("VT ESET-NOD32")
            if 'F-Secure' in response_json['scans']:
                if response_json['scans']['F-Secure']['detected']:
                    me = mt.addEntity("maltego.Avdetection", '%s' % response_json['scans']['F-Secure']['result'])
                    me.setLinkLabel("VT F-Secure")
            if 'Symantec' in response_json['scans']:
                if response_json['scans']['Symantec']['detected']:
                    me = mt.addEntity("maltego.Avdetection", '%s' % response_json['scans']['Symantec']['result'])
                    me.setLinkLabel("VT Symantec")

    except:
        return False

    return mt

# hash_to_filename
def hash_to_filename():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'submission_names' in response_json:
                for item in response_json['submission_names']:
                    me = mt.addEntity("maltego.Phrase", '%s' % item)
                    me.setLinkLabel("VT Filename")

    except:
        return False

    return mt

# hash_to_useragent
def hash_to_useragent():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'http' in response_json['additional_info']['behaviour-v1']['network']:
                for item in response_json['additional_info']['behaviour-v1']['network']['http']:
                    me = mt.addEntity("maltego.Useragent", '%s' % item['user-agent'])
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# hash_to_imphash
def hash_to_imphash():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'additional_info' in response_json:
                me = mt.addEntity("maltego.Imphash", '%s' % response_json['additional_info']['pe-imphash'])
                me.setLinkLabel("VT")

    except:
        return False

    return mt

# hash_to_similar
def hash_to_similar():
    try:
        params = {'apikey': apikey, 'query': 'similar-to:' + data}
        response = requests.post(apiurl + 'file/search', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'hashes' in response_json:
                for item in response_json['hashes']:
                    me = mt.addEntity("maltego.Hash", '%s' % item)
                    me.setLinkLabel("VT similar-to")

    except:
        return False

    return mt

# useragent_to_hash
def useragent_to_hash():
    try:
        params = {'apikey': apikey, 'query': 'behaviour:' + data}
        response = requests.post(apiurl + 'file/search', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'hashes' in response_json:
                for item in response_json['hashes']:
                    me = mt.addEntity("maltego.Hash", '%s' % item)
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# imphash_to_hash
def imphash_to_hash():
    try:
        params = {'apikey': apikey, 'query': 'imphash:' + data}
        response = requests.post(apiurl + 'file/search', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'hashes' in response_json:
                for item in response_json['hashes']:
                    me = mt.addEntity("maltego.Hash", '%s' % item)
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# hash_to_rescan
def hash_to_rescan():
    try:
        params = {'apikey': apikey, 'resource': data}
        response = requests.post(apiurl + 'file/rescan', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
                    me = mt.addEntity("maltego.Phrase", '%s' % "Rescanning... Please wait...")
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# hash_to_section
def hash_to_section():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'sections' in response_json['additional_info']:
                for item in response_json['additional_info']['sections']:
                    me = mt.addEntity("maltego.Section", '%s' % item[0])
                    me = mt.addEntity("maltego.Section", '%s' % item[5])
                    me.setLinkLabel(item[0])

    except:
        return False

    return mt


# hash_to_timestamp
def hash_to_timestamp():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'TimeStamp' in response_json['additional_info']['exiftool']:
                me = mt.addEntity("maltego.Timestamp", '%s' % response_json['additional_info']['exiftool']['TimeStamp'])

    except:
        return False

    return mt

# hash_to_firstseen
def hash_to_firstseen():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'first_seen' in response_json:
                me = mt.addEntity("maltego.Firstseen", '%s' % response_json['first_seen'])
                me.setLinkLabel("VT")

    except:
        return False

    return mt

# hash_to_filesize
def hash_to_filesize():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'size' in response_json:
                me = mt.addEntity("maltego.Filesize", '%s' % response_json['size'])

    except:
        return False

    return mt

# hash_to_filetype
def hash_to_filetype():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'type' in response_json:
                me = mt.addEntity("maltego.Phrase", '%s' % response_json['type'])

    except:
        return False

    return mt

# hash_to_peresource
def hash_to_peresource():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
#            if 'pe-resource-list' in response_json['additional_info']:
            if 'pe-resource-detail' in response_json['additional_info']:
#                for item in response_json['additional_info']['pe-resource-list']:
                for item in response_json['additional_info']['pe-resource-detail']:
                    me = mt.addEntity("maltego.Peresource", '%s' % item['sha256'])
                    me.setLinkLabel(item['lang'] + " / " + item['type'])

    except:
        return False

    return mt

# hash_to_itw
def hash_to_itw():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'email_parents' in response_json['additional_info']:
                for item in response_json['additional_info']['email_parents']:
                    me = mt.addEntity("maltego.Hash", '%s' % item)
                    me.setLinkLabel("VT email_parents")
            if 'compressed_parents' in response_json['additional_info']:
                for item in response_json['additional_info']['compressed_parents']:
                    me = mt.addEntity("maltego.Hash", '%s' % item)
                    me.setLinkLabel("VT compressed_parents")

    except:
        return False

    return mt

# hash_to_mutex
def hash_to_mutex():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'created' in response_json['additional_info']['behaviour-v1']['mutex']:
                for item in response_json['additional_info']['behaviour-v1']['mutex']['created']:
                    me = mt.addEntity("maltego.Mutex", '%s' % item['mutex'])
                    me.setLinkLabel("VT mutex")

    except:
        return False

    return mt

# hash_to_md5
def hash_to_md5():
    try:
        params = {'apikey': apikey, 'resource': data}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'md5' in response_json:
                    me = mt.addEntity("maltego.Hash", '%s' % response_json['md5'])

    except:
        return False

    return mt

# hash_to_sha256
def hash_to_sha256():
    try:
        params = {'apikey': apikey, 'resource': data}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'sha256' in response_json:
                    me = mt.addEntity("maltego.Hash", '%s' % response_json['sha256'])

    except:
        return False

    return mt

# section_to_hash
def section_to_hash():
    try:
        params = {'apikey': apikey, 'query': 'section:' + data}
        response = requests.post(apiurl + 'file/search', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'hashes' in response_json:
                for item in response_json['hashes']:
                    me = mt.addEntity("maltego.Hash", '%s' % item)
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# mutex_to_hash
def mutex_to_hash():
    try:
        params = {'apikey': apikey, 'query': 'behaviour:' + data}
        response = requests.post(apiurl + 'file/search', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'hashes' in response_json:
                for item in response_json['hashes']:
                    me = mt.addEntity("maltego.Hash", '%s' % item)
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# peresource_to_hash
def peresource_to_hash():
    try:
        params = {'apikey': apikey, 'query': 'resource:' + data}
        response = requests.post(apiurl + 'file/search', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'hashes' in response_json:
                for item in response_json['hashes']:
                    me = mt.addEntity("maltego.Hash", '%s' % item)
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# hash_to_behaviour
# ['behaviour-v1']['process']['shellcmds']['cmd']
# ['behaviour-v1']['process']['created']['proc']
# ['behaviour-v1']['registry']['set']['key'] + ['val']
# ['behaviour-v1']['filesystem']['written']
def hash_to_behaviour():
    try:
        params = {'apikey': apikey, 'resource': data, 'allinfo': '1'}
        response = requests.get(apiurl + 'file/report', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])
#        print response_json

        if respcode == 1:
            if 'shellcmds' in response_json['additional_info']['behaviour-v1']['process']:
                for item in response_json['additional_info']['behaviour-v1']['process']['shellcmds']:
                    me = mt.addEntity("maltego.Behaviour", '%s' % item['cmd'])
                    me.setLinkLabel("VT process shellcmds")
            if 'created' in response_json['additional_info']['behaviour-v1']['process']:
                for item in response_json['additional_info']['behaviour-v1']['process']['created']:
                    me = mt.addEntity("maltego.Behaviour", '%s' % item['proc'])
                    me.setLinkLabel("VT process created")
            if 'set' in response_json['additional_info']['behaviour-v1']['registry']:
                for item in response_json['additional_info']['behaviour-v1']['registry']['set']:
                    me = mt.addEntity("maltego.Behaviour", '%s' % item['key'])
                    me.setLinkLabel("VT reg set val: " + item['val'])
            if 'written' in response_json['additional_info']['behaviour-v1']['filesystem']:
                for item in response_json['additional_info']['behaviour-v1']['filesystem']['written']:
                    me = mt.addEntity("maltego.Behaviour", '%s' % item['path'])
                    me.setLinkLabel("VT filesystem written")

    except:
        return False

    return mt

# behaviour_to_hash
def behaviour_to_hash():
    try:
        params = {'apikey': apikey, 'query': 'behaviour:' + data}
        response = requests.post(apiurl + 'file/search', params=params)
        response_json = response.json()
        respcode = int(response_json['response_code'])

        if respcode == 1:
            if 'hashes' in response_json:
                for item in response_json['hashes']:
                    me = mt.addEntity("maltego.Hash", '%s' % item)
                    me.setLinkLabel("VT")

    except:
        return False

    return mt

# 



# 



# 



# main
func = sys.argv[1]
data = sys.argv[2]

mt = MaltegoTransform()
mresult = eval(func)()
#print mresult
mresult.returnOutput()


