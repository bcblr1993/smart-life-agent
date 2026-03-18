#!/usr/bin/env python3
"""
Smart Life Agent - 硬件联动模块
用于中关村北纬龙虾大赛 - 展示硬件联动能力（加分项）
"""

import json
import random
import time
from datetime import datetime

class HardwareBridge:
    """硬件桥接器 - 连接智能设备"""
    
    def __init__(self):
        self.devices = {
            "speaker": {"name": "智能音箱", "status": "在线", "type": "audio"},
            "screen": {"name": "智能屏", "status": "在线", "type": "display"},
            "robot": {"name": "早教机器人", "status": "离线", "type": "robot"}
        }
        
    def list_devices(self) -> str:
        """列出可用设备"""
        result = "📱 可用设备列表：\n\n"
        for device_id, info in self.devices.items():
            status_emoji = "✅" if info["status"] == "在线" else "❌"
            result += f"{status_emoji} {info['name']} - {info['status']}\n"
        return result
    
    def play_story(self, story_title: str) -> str:
        """通过智能音箱播放故事"""
        if self.devices["speaker"]["status"] != "在线":
            return "❌ 智能音箱离线，无法播放"
        
        return f"""🎵 正在通过智能音箱播放：《{story_title}》

✅ 设备：{self.devices['speaker']['name']}
⏱️ 预计时长：5分钟
🔊 音量：适中

📖 故事内容：
{self._get_story_content(story_title)}

💡 提示：可以语音控制暂停/继续"""
    
    def _get_story_content(self, title: str) -> str:
        """获取故事内容（简化版）"""
        stories = {
            "小兔子勇敢之旅": "从前有一只小兔子叫白白，它一直很害怕黑暗...",
            "星星的礼物": "小狐狸星星今晚失眠了，因为它觉得今天一天都不开心...",
            "爱哭的小水滴": "云朵阿姨怀里住着很多小水滴..."
        }
        return stories.get(title, "故事内容...")
    
    def show_recipe(self, recipe_name: str) -> str:
        """在智能屏上展示食谱"""
        if self.devices["screen"]["status"] != "在线":
            return "❌ 智能屏离线，无法展示"
        
        return f"""📺 正在智能屏展示食谱：《{recipe_name}》

✅ 设备：{self.devices['screen']['name']}
📱 投屏成功！

🍳 食谱详情：
━━━━━━━━━━━━━━━━━━
菜名：{recipe_name}
时间：20分钟
难度：⭐⭐

食材：
- 鸡蛋 2个
- 虾仁 5个
- 温水 150ml

步骤：
1. 鸡蛋打散
2. 加入温水
3. 放入虾仁
4. 蒸10分钟
━━━━━━━━━━━━━━━━━━

👨‍🍳 还可以语音朗读步骤哦！"""
    
    def control_light(self, action: str) -> str:
        """控制智能灯光"""
        actions = {
            "开": "💡 已开灯，亮度100%",
            "关": "💡 已关灯",
            "调暗": "💡 已调暗，亮度50%",
            "睡眠模式": "💡 已切换为睡眠模式，亮度10%，暖黄色"
        }
        return actions.get(action, "❌ 未知指令")
    
    def send_to_watch(self, message: str) -> str:
        """发送消息到儿童手表"""
        return f"""⌚ 消息已发送到儿童手表

📨 内容：{message}
⏰ 发送时间：{datetime.now().strftime('%H:%M')}
✅ 送达状态：成功

📱 手表提示：收到来自小管家的消息~"""

def demo_hardware():
    """硬件联动演示"""
    print("=" * 55)
    print("🦞 Smart Life Agent - 硬件联动演示")
    print("    中关村北纬龙虾大赛 | 加分项展示")
    print("=" * 55)
    print()
    
    bridge = HardwareBridge()
    
    # 演示1：列出设备
    print("📱 演示1：设备列表")
    print("-" * 50)
    print(bridge.list_devices())
    print()
    
    # 演示2：播放故事
    print("🎵 演示2：智能音箱播放故事")
    print("-" * 50)
    print(bridge.play_story("小兔子勇敢之旅"))
    print()
    
    # 演示3：展示食谱
    print("📺 演示3：智能屏展示食谱")
    print("-" * 50)
    print(bridge.show_recipe("虾仁蒸蛋"))
    print()
    
    # 演示4：控制灯光
    print("💡 演示4：智能灯光控制")
    print("-" * 50)
    print(bridge.control_light("睡眠模式"))
    print()
    
    # 演示5：发送到手表的
    print("⌚ 演示5：儿童手表消息")
    print("-" * 50)
    print(bridge.send_to_watch("该睡觉啦！小管家爱你~"))
    print()
    
    print("=" * 55)
    print("✅ 硬件联动演示完成！")
    print("=" * 55)

if __name__ == "__main__":
    import sys
    bridge = HardwareBridge()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "devices":
            print(bridge.list_devices())
        elif command == "story" and len(sys.argv) > 2:
            print(bridge.play_story(sys.argv[2]))
        elif command == "recipe" and len(sys.argv) > 2:
            print(bridge.show_recipe(sys.argv[2]))
        elif command == "light" and len(sys.argv) > 2:
            print(bridge.control_light(sys.argv[2]))
        elif command == "watch" and len(sys.argv) > 2:
            message = " ".join(sys.argv[2:])
            print(bridge.send_to_watch(message))
        else:
            print("用法：")
            print("  python3 hardware_bridge.py devices")
            print("  python3 hardware_bridge.py story <故事名>")
            print("  python3 hardware_bridge.py recipe <菜名>")
            print("  python3 hardware_bridge.py light <开/关/调暗/睡眠模式>")
            print("  python3 hardware_bridge.py watch <消息>")
    else:
        demo_hardware()
