#!/usr/bin/env python3
"""
OpenClaw Tool: smart_life_agent
智能育儿生活助手 - 可被 OpenClaw 调用
"""

import json
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from demo import SmartLifeAgent

def main():
    """OpenClaw 工具入口"""
    # 读取输入
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        user_input = "有什么功能"
    
    # 创建 Agent 实例
    agent = SmartLifeAgent()
    
    # 执行对话
    result = agent.chat(user_input)
    
    # 输出 JSON 格式（OpenClaw 工具格式）
    output = {
        "success": True,
        "response": result,
        "input": user_input
    }
    
    print(json.dumps(output, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
