import requests
import time

# Initial request to get the task_id
print("🚀 Making initial request to chat completions endpoint...")
url = "https://chat.qwen.ai/api/v2/chat/completions?chat_id=d0e968d8-276a-4648-bf56-42879551793e"

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjliY2VhNTAwLWY1Y2ItNDIxNi04NWIzLWY5OGNkNTgyZDc4ZSIsImxhc3RfcGFzc3dvcmRfY2hhbmdlIjoxNzUwNjYwODczLCJleHAiOjE3NTM2OTU5MzV9.lJHez75GXmJ8xihb6xDuRNBLNWnYDerCeGZQ8UEsCIg",
    "bx-ua": "defaultFY2_load_failed with timeout@@https://chat.qwen.ai/@@1751104062108",
    "bx-umidtoken": "defaultFY2_load_failed with timeout@@https://chat.qwen.ai/@@1751104062108",
    "bx-v": "2.5.31",
    "connection": "keep-alive",
    "content-type": "application/json",
    "cookie": "cna=VKuOII3g12kCAZg7FD7PkNyf; _bl_uid=0ymkO9sjstpostzgIs44ckny4paR; cnaui=9bcea500-f5cb-4216-85b3-f98cd582d78e; aui=9bcea500-f5cb-4216-85b3-f98cd582d78e; _gcl_au=1.1.1764185934.1745337681.537199183.1748157215.1748157214; acw_tc=0a03e55917511036803365381e4c584f089521b93ce3332947cec89356be1c; x-ap=ap-southeast-1; sca=3b9e8c51; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjliY2VhNTAwLWY1Y2ItNDIxNi04NWIzLWY5OGNkNTgyZDc4ZSIsImxhc3RfcGFzc3dvcmRfY2hhbmdlIjoxNzUwNjYwODczLCJleHAiOjE3NTM2OTU5MzV9.lJHez75GXmJ8xihb6xDuRNBLNWnYDerCeGZQ8UEsCIg; atpsida=10012f1007eef822056473eb_1751104038_3; SERVERID=76dbb857173d0d7eac6948d9641a1962|1751104060|1751103680; ssxmod_itna=Qq+xRDc7G=0=lDeKxmu4x3kDeqGuAOx0dGM09DIqGQGcD82D0phBPar+Ke44D7KAQ7DD88QinGtY0xGN4d2D0=HDf40W+Coj5t5Z96uEhKWYGk0+PQqchopXLN0jyCvAkuFmxrDU4i8r=0zqo4DxxGTDCeDQxirDD4DADibrxD17DDkD0Rwa+OIr4GWDmRwDGeDeZ7+DYHeDD5DAg5DwhRwESHL7WLpqm3P=4DzN4G1AD0HqmCNN4LRQyTv/x0OfDi1DnI3dQWQfmOImRW+DlIgavoKzKa62Ygv8bfzq2mxeRpx1Y449ri5A0i/hySHP4b5K4inqPS0xFDYQ0zQqHAAYDDWBA5Ih5+GdqhDwBCEk16M1+GsKGtLjtCo+dBddAqmrNwY5M05qCxfm4MxxW04PoxMrsWiDD; ssxmod_itna2=Qq+xRDc7G=0=lDeKxmu4x3kDeqGuAOx0dGM09DIqGQGcD82D0phBPar+Ke44D7KAQ7DD88QinGtYexD3rKSODAAhZYD7P41SCp++4DBuP+LZRb7ABKW3s1Gx2A=n/1C5H1=mQ+t=YD9GK0uDje4QUCh=GDkDlYkAVK4XPCqtRChvLf4Q32j2=kCj3NeXqKZbUGeQje1=0QquUAD0b1LvHL6t7vd0V9ZftIpcKoehaPnP3o40tvkGkoATRQlbjC1tulEwk1xeynQ82zM3xxrj1UbgxeTRKrkha=ujS7Lky/u551kZQ6XY8wcDQFv8nuDwmjy9ApOKb5+TkB24IPQAus+cljAR9HCIunGqQmmE4qQB+DoqxebN8DwBRnUcDAnlGwxmmQNY1F59KPW3ah/qQMgtLvFKaZBEU3aoV7AY0nj7Veg5MW/fTR0TgbwdiKavPrR4hRR4SrHhBiROk9WunmqrAuGTnKntqcnRo+3BsQD+lBxr7I4w40TMBvlRbNbT9CFm3jIUpmCKV0+R0dpAd7iGOWfpoTgGwDXRzg+=5qP9cocb8lS7AWnDaP3aMIOW0wiKasUStq1rkqPFEE07lURwgnvXyf7wLLq=ubIOwG9R=2RIRvGxzhIpG7B6t/AnANQId9IdM44KRTSh75rIiqOWUN0vO8GGb0RkDnjIlow4uHnBbGCHqkGniZFG/uY3jU3kY0GuDg=KxdBXPn1fDGkxQPYhbm+/7a+QdeU/DGLqRdyDbfmBkqxKrmY0+/ieehz0PhrKD5nxz00tNAG4QDCD5tGvGDz41mDeD; isg=BD8_2rqqayknlm9tfGi71Mx9zhPJJJPGHMru0NEJv-454Epi2fcfF-i-IqgeuGs-; tfstk=gmDo5IYeNbPW-6LYMxwW_hVvn6dA28wQV2BLJJUegrzje2d7Jj2EbVVLTQG-oy4q7ylRakS4xua0YareNxq4jl7UaBtC3szYbk7FU_WV3kE14T-SKj6nfDMJVJK7F0wQLFL9BFnSVJ9fK-aKEiP4VmWPL7RY31ot_GL9Bdnrkz2TNFHpFCl4lkyU4zPe3nqgvyyUTuo2mkrdz6Wr8nx0VkEz8zrFuorUuyyUL2o2mkU44JyEt5jzP5Fq3ELVEwGsrFM8q74Z4zuKJx50O_g0o9WEnj2L7KUcL9k0qD4CI0WM9Pl_y5UquKBuKmrno5hkST0nYcGUivby2Voni2w-3H5z7b3-8WcXSOEuejV0mfxOIWe-B5yrMIT498qinSMkj_zuhr28gvY2I8htXvNZULb_k5Zno5hkST0N4b5V_YN1do-K361QaoZ0W--xwxf2JLyJmnfNO7rb4D-Dm61QaoZ0WnxcsuNzcuoF.",
    "host": "chat.qwen.ai",
    "origin": "https://chat.qwen.ai",
    "referer": "https://chat.qwen.ai/c/d0e968d8-276a-4648-bf56-42879551793e",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "source": "web",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "version": "0.0.125",
    "x-accel-buffering": "no",
    "x-request-id": "d52f88bd-7c2f-4440-a7ee-ea4fb2797275"
}

payload = {
    "stream": False,
    "incremental_output": True,
    "chat_id": "d0e968d8-276a-4648-bf56-42879551793e",
    "chat_mode": "normal",
    "model": "qwen3-235b-a22b",
    "parent_id": None,
    "messages": [
        {
            "fid": "7e16887f-8d68-4f1b-93e1-7e6de6636b35",
            "parentId": None,
            "childrenIds": ["a63a4775-2537-44bd-a6d6-2963ec91e06c"],
            "role": "user",
            "content": "Product photography, perfume bottle with red liquid inside on top of black rocks surrounded by berries, forest background, photo taken from the front, vibrant colors, soft lighting, high resolution, hyper realistic, highly detailed, sharp focus, commercial photography, professional product photographer, stunning photography, trending in art station, behance award winning photography, instagram story, advertising photography, beautiful, aesthetic, minimalistic, modern, sleek, shot using Canon EOS R5 camera --ar 3:4 --v 7 --stylize 750",
            "user_action": "chat",
            "files": [],
            "timestamp": 1751104059,
            "models": ["qwen3-235b-a22b"],
            "chat_type": "t2i",
            "feature_config": {
                "thinking_enabled": False,
                "output_schema": "phase"
            },
            "extra": {
                "meta": {
                    "subChatType": "t2i"
                }
            },
            "sub_chat_type": "t2i",
            "parent_id": None
        }
    ],
    "timestamp": 1751104062,
    "size": "1:1"
}

print("📤 Sending POST request to:", url)
response = requests.post(url, headers=headers, json=payload)

print("\n🔔 First Response Received:")
print("Status Code:", response.status_code)
response_json = response.json()
print("Full Response:", response_json)

# Extract task_id
try:
    task_id = response_json['data']['messages'][0]['extra']['wanx']['task_id']
    print("\n🎯 Extracted task_id:", task_id)
except KeyError as e:
    print("\n❌ Error extracting task_id:", e)
    exit()

# Polling configuration
max_attempts = 30  # Maximum number of polling attempts
poll_interval = 3  # Seconds between polls
attempt = 0
task_completed = False

print("\n🔍 Starting to poll task status...")
while not task_completed and attempt < max_attempts:
    attempt += 1
    print(f"\n🔄 Attempt {attempt}/{max_attempts} - Checking task status...")
    
    status_url = f"https://chat.qwen.ai/api/v1/tasks/status/{task_id}"
    print("🌐 Requesting:", status_url)
    
    status_response = requests.get(status_url, headers=headers)
    status_data = status_response.json()
    
    print("📥 Status Response:", status_data)
    
    # Check if task is completed
    if status_data.get('success') or status_data.get('task_status') in ['completed', 'success']:
        print("\n🎉 Task completed successfully!")
        print("Final Result:", status_data)
        task_completed = True
    elif status_data.get('task_status') in ['failed', 'error']:
        print("\n❌ Task failed!")
        print("Error:", status_data.get('message', 'No error message'))
        break
    else:
        print(f"⏳ Task still processing... (Status: {status_data.get('task_status', 'unknown')})")
        if attempt < max_attempts:
            print(f"⏲ Waiting {poll_interval} seconds before next check...")
            time.sleep(poll_interval)

if not task_completed:
    print(f"\n⌛ Reached maximum polling attempts ({max_attempts}) without completion")
