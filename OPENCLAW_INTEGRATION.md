# OpenClaw 集成指南

本文档说明如何将 Smart Life Agent 接入 OpenClaw。

## 方式一：通过 Skill 调用

### 1. 安装 Skill

```bash
mkdir -p ~/.openclaw/skills/smart-life-agent
# 把 SKILL.md 复制过去
```

### 2. 在 OpenClaw 中使用

```
用户：小管家，今天吃什么？
OpenClaw：[调用 skill] → 返回食谱
```

---

## 方式二：通过 Tool 调用

### 1. 注册 Tool

在 OpenClaw 配置中添加：

```json
{
  "tools": {
    "smart_life": {
      "command": "python3",
      "args": [
        "/Users/chenxu/.openclaw/workspace/xiaohongshu-agent/tool_smart_life.py"
      ],
      "input": "string"
    }
  }
}
```

### 2. 使用 Tool

```
用户：帮我问问小管家今天吃什么
OpenClaw → tool:smart_life("今天吃什么") → 返回结果
```

---

## 方式三：创建专属 Agent

### 1. 定义 Agent

```json
{
  "agents": {
    "smart-life": {
      "model": "minimax/MiniMax-M2.5",
      "system": "你是 Smart Life Agent，一个智能育儿助手...",
      "tools": ["smart_life"]
    }
  }
}
```

### 2. 对话使用

```
@smart-life 今天孩子吃什么好？
```

---

## 接入渠道

| 渠道 | 接入方式 | 说明 |
|------|----------|------|
| Telegram | 配置 botToken | 文字/语音对话 |
| 飞书 | 配置 appId/Secret | 文字/菜单交互 |
| Web | 访问 Dashboard | 网页对话 |
| 语音 | 接入 TTS/STT | 语音交互 |

---

## 硬件联动（加分项）

可以接入硬件设备获得额外加分：

### 1. 智能音箱
- 小爱同学
- 小度音箱
- 天猫精灵

### 2. 早教机器人
- 语音对话
- 故事播放

### 3. 智能屏
- 食谱展示
- 视频故事

---

## 完整工作流

```
用户 (Telegram/飞书/语音)
        ↓
OpenClaw Gateway
        ↓
Smart Life Agent (理解意图)
        ↓
功能模块 (食谱/故事/记录/学习)
        ↓
返回结果 → 用户
```

---

## 测试

```bash
# 测试命令行
python3 tool_smart_life.py 今天吃什么

# 测试 Skill
# 在 OpenClaw 对话中输入相应指令
```
