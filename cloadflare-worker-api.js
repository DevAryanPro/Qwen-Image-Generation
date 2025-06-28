addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  // Parse the request URL to extract query parameters
  const url = new URL(request.url);
  const content = url.searchParams.get('content');
  const size = url.searchParams.get('size');

  if (!content || !size) {
    return new Response(JSON.stringify({ error: 'Missing content or size parameter' }), {
      headers: { 'Content-Type': 'application/json' },
      status: 400
    });
  }

  // Initial request to get the task_id
  const taskId = await getTaskId(content, size);
  if (!taskId) {
    return new Response(JSON.stringify({ error: 'Failed to get task ID' }), {
      headers: { 'Content-Type': 'application/json' },
      status: 500
    });
  }

  // Poll for task completion
  const result = await pollTaskStatus(taskId);
  if (result.success) {
    const responseData = {
      details: {
        chat_type: result.chat_type,
        task_status: result.task_status,
        message: result.message || "",
        remaining_time: result.remaining_time || "",
        content: result.content || ""
      }
    };
    return new Response(JSON.stringify(responseData), {
      headers: { 'Content-Type': 'application/json' },
    });
  } else {
    // Return empty response if task failed
    return new Response(JSON.stringify({}), {
      headers: { 'Content-Type': 'application/json' },
    });
  }
}

async function getTaskId(content, size) {
  const url = 'https://chat.qwen.ai/api/v2/chat/completions?chat_id=d0e968d8-276a-4648-bf56-42879551793e';
  const headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjliY2VhNTAwLWY1Y2ItNDIxNi04NWIzLWY5OGNkNTgyZDc4ZSIsImxhc3RfcGFzc3dvcmRfY2hhbmdlIjoxNzUwNjYwODczLCJleHAiOjE3NTM2OTU5MzV9.lJHez75GXmJ8xihb6xDuRNBLNWnYDerCeGZQ8UEsCIg",
    "bx-ua": "defaultFY2_load_failed with timeout@@https://chat.qwen.ai/@@1751104062108",
    "bx-umidtoken": "defaultFY2_load_failed with timeout@@https://chat.qwen.ai/@@1751104062108",
    "bx-v": "2.5.31",
    "connection": "keep-alive",
    "content-type": "application/json",
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
  };

  const payload = {
    "stream": false,
    "incremental_output": true,
    "chat_id": "d0e968d8-276a-4648-bf56-42879551793e",
    "chat_mode": "normal",
    "model": "qwen3-235b-a22b",
    "parent_id": null,
    "messages": [
      {
        "fid": "7e16887f-8d68-4f1b-93e1-7e6de6636b35",
        "parentId": null,
        "childrenIds": ["a63a4775-2537-44bd-a6d6-2963ec91e06c"],
        "role": "user",
        "content": content,
        "user_action": "chat",
        "files": [],
        "timestamp": 1751104059,
        "models": ["qwen3-235b-a22b"],
        "chat_type": "t2i",
        "feature_config": {
          "thinking_enabled": false,
          "output_schema": "phase"
        },
        "extra": {
          "meta": {
            "subChatType": "t2i"
          }
        },
        "sub_chat_type": "t2i",
        "parent_id": null
      }
    ],
    "timestamp": 1751104062,
    "size": size
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(payload)
  });

  const responseJson = await response.json();
  return responseJson.data?.messages?.[0]?.extra?.wanx?.task_id;
}

async function pollTaskStatus(taskId) {
  const maxAttempts = 30;
  const pollInterval = 3000; // 3 seconds
  const headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjliY2VhNTAwLWY1Y2ItNDIxNi04NWIzLWY5OGNkNTgyZDc4ZSIsImxhc3RfcGFzc3dvcmRfY2hhbmdlIjoxNzUwNjYwODczLCJleHAiOjE3NTM2OTU5MzV9.lJHez75GXmJ8xihb6xDuRNBLNWnYDerCeGZQ8UEsCIg",
    "bx-ua": "defaultFY2_load_failed with timeout@@https://chat.qwen.ai/@@1751104062108",
    "bx-umidtoken": "defaultFY2_load_failed with timeout@@https://chat.qwen.ai/@@1751104062108",
    "bx-v": "2.5.31",
    "connection": "keep-alive",
    "content-type": "application/json",
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
  };

  for (let attempt = 0; attempt < maxAttempts; attempt++) {
    const statusUrl = `https://chat.qwen.ai/api/v1/tasks/status/${taskId}`;
    const response = await fetch(statusUrl, { headers });
    const statusData = await response.json();

    if (statusData.success || statusData.task_status === 'completed' || statusData.task_status === 'success') {
      return {
        success: true,
        chat_type: statusData.chat_type || "t2i",
        task_status: statusData.task_status || "success",
        message: statusData.message || "",
        remaining_time: statusData.remaining_time || "",
        content: statusData.content || ""
      };
    } else if (statusData.task_status === 'failed' || statusData.task_status === 'error') {
      return { success: false };
    } else {
      await new Promise(resolve => setTimeout(resolve, pollInterval));
    }
  }

  return { success: false };
}
