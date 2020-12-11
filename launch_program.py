import os
import json

client_id = "appID%3ANMDPTRIAL_arjun_sahni_nuance_com_20200908T211437960602%3Ageo%3Aus%3AclientName%3Adefault"
client_secret = "h5x0gp0w2pnRQ0vBUdYS51HaXwe6VY3u9ArQUh5SbAM"
auth_url = "https://auth.crt.nuance.com/oauth2/token"
sys_out = os.popen(f'curl -s -u "{client_id}:{client_secret}" "{auth_url}" -d "grant_type=client_credentials" -d "scope=dlg"')
a = sys_out.read()
sys_out.close()
access_token = json.loads(a)['access_token']
tag = "A1421_C1"
tag = "MEDICAL_DIAGNOSIS_721"

sys_out_1 = os.popen(f'python final_client.py \
--serverUrl dlg.api.nuance.com:443 \
--token {access_token} \
--modelUrn "urn:nuance-mix:tag:model/{tag}/mix.dialog"', "r")

a = sys_out_1.read()
print(a)



