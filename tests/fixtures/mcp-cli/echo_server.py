#!/usr/bin/env python3
"""Minimal stdio MCP server exposing one tool, echo(text) -> "echo:<text>"."""
import json
import sys


def reply(msg_id, result):
    sys.stdout.write(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": result}) + "\n")
    sys.stdout.flush()


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    req = json.loads(line)
    method, msg_id = req.get("method"), req.get("id")
    if msg_id is None:
        continue
    if method == "initialize":
        reply(msg_id, {"protocolVersion": req.get("params", {}).get("protocolVersion", "2024-11-05"),
                       "capabilities": {"tools": {}},
                       "serverInfo": {"name": "echo", "version": "1.0"}})
    elif method == "tools/list":
        reply(msg_id, {"tools": [{"name": "echo", "description": "Echo text back",
                                  "inputSchema": {"type": "object",
                                                  "properties": {"text": {"type": "string"}},
                                                  "required": ["text"]}}]})
    elif method == "tools/call":
        text = req["params"]["arguments"]["text"]
        reply(msg_id, {"content": [{"type": "text", "text": f"echo:{text}"}]})
    else:
        reply(msg_id, {})
