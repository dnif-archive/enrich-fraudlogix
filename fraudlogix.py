import yaml
import requests
import os
import logging

inteltype = ['INTEL_ADDR']
path = os.environ["WORKDIR"]

try:
    with open(path + "/enrichment_plugins/fraudlogix/dnifconfig.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    fl_api = cfg['enrich_plugin']['FL_API']
except Exception, e:
    logging.error("FraudLogix enrichment error in reading dnifconfig.yml: {}".format(e))


def import_ip_intel():
    try:
        headers = {
            'Content-Type': 'application/json'
        }

        params = {'akey': fl_api, 'method': 'json', 'threat_level': 'Default', 'show_level': 1,
                  'show_type': 1}
        url = "https://api.fraudlogix.com/iplookup/webservice.php"
        res = requests.post(url, params=params, headers=headers)
        json_response = res.json()

        if res.status_code == 200:
            try:
                lines = []
                for line in json_response[0]:

                    tmp_dict = {}
                    tmp_dict["EvtName"] = line['ip']
                    if '.' in line['ip']:
                        tmp_dict["EvtType"] = "IPv4"
                    else:
                        tmp_dict["EvtType"] = "IPv6"
                    tmp_dict2 = {}
                    tmp_dict2["IntelRef"] = ["FRAUDLOGIX"]
                    tmp_dict2["IntelRefURL"] = [""]
                    tmp_dict2["FLThreatDetail"] = [line["threat_type"]]
                    tmp_dict2["ThreatType"] = ["Malicious"]
                    tmp_dict2["FLThreatActivityLevel"] = [line["threat_activity_level"]]
                    tmp_dict["AddFields"] = tmp_dict2
                    lines.append(tmp_dict)
            except Exception,e:
                logging.error("FraudLogix error in processing enrichment api response %s"%e)
                lines = []
    except Exception,e:
        logging.error("FraudLogix enrichment error in requesting  API :{}".format(e))
    return lines,"INTEL_ADDR"

