#!/usr/bin/env python3
"""
Smart Life Agent - 智能生活助手演示
中关村北纬龙虾大赛参赛作品
"""

import json
import random
from datetime import datetime, timedelta

class SmartLifeAgent:
    """智能生活助手"""
    
    def __init__(self):
        self.name = "小生活"
        self.user_preferences = {}
        
    def chat(self, message: str) -> str:
        """对话入口"""
        message = message.lower()
        
        if any(k in message for k in ["日程", "安排", " schedule", "会议"]):
            return self.handle_schedule()
        elif any(k in message for k in ["吃", "食谱", "菜谱", "做饭", "recipe"]):
            return self.handle_recipe()
        elif any(k in message for k in ["旅行", "旅游", "trip", "travel"]):
            return self.handle_travel()
        elif any(k in message for k in ["记账", "花钱", " expense", "预算"]):
            return self.handle_expense()
        elif any(k in message for k in ["学习", "study", "计划"]):
            return self.handle_study()
        else:
            return self.handle_general(message)
    
    def handle_schedule(self) -> str:
        """日程管理"""
        schedules = [
            "📅 今日日程：\n" \
            "• 09:00 - 团队会议\n" \
            "• 12:00 - 午餐\n" \
            "• 14:00 - 项目评审\n" \
            "• 18:30 - 健身\n\n" \
            "💡 提醒：今天下午有雨，记得带伞哦！",
            
            "📅 明天日程：\n" \
            "• 10:00 - 客户拜访\n" \
            "• 13:00 - 午餐会议\n" \
            "• 16:00 - 季度总结\n\n" \
            "💡 建议：上午有充足时间准备提案",
            
            "📅 本周计划：\n" \
            "• 周一至周五：日常工作\n" \
            "• 周六：团队团建\n" \
            "• 周日：休息/学习\n\n" \
            "💡 效率提示：周三下午适合处理复杂任务",
        ]
        return random.choice(schedules)
    
    def handle_recipe(self) -> str:
        """食谱推荐"""
        recipes = [
            "🍳 今日推荐：蒜香鸡翅\n\n" \
            "⏱️ 准备时间：30分钟\n" \
            "⭐ 难度：⭐⭐（简单）\n\n" \
            "📝 食材：\n" \
            "• 鸡翅 500g\n" \
            "• 大蒜 5瓣\n" \
            "• 酱油 2勺\n" \
            "• 料酒 1勺\n\n" \
            "👨‍🍳 做法：\n" \
            "1. 鸡翅洗净，两面划刀\n" \
            "2. 蒜末+酱油+料酒腌制30分钟\n" \
            "3. 锅中热油，煎至金黄\n" \
            "4. 完成！🎉\n\n" \
            "💡 小贴士：配啤酒更香！",
            
            "🥗 今日推荐：轻食沙拉\n\n" \
            "⏱️ 准备时间：15分钟\n" \
            "⭐ 难度：⭐（非常简单）\n\n" \
            "📝 食材：\n" \
            "• 生菜 适量\n" \
            "• 鸡胸肉 100g\n" \
            "• 番茄 1个\n" \
            "• 橄榄油 适量\n\n" \
            "👨‍🍳 做法：\n" \
            "1. 所有食材洗净切好\n" \
            "2. 鸡胸肉煎熟切块\n" \
            "3. 淋上橄榄油和酱油\n" \
            "4. 完成！健康又美味！💚",
        ]
        return random.choice(recipes)
    
    def handle_travel(self) -> str:
        """旅行规划"""
        plans = [
            "✈️ 周末旅行推荐：北京周边游\n\n" \
            "📍 目的地：怀柔雁栖湖\n" \
            "🚗 车程：1.5小时\n" \
            "💰 预算：约200元/人\n\n" \
            "📝 推荐行程：\n" \
            "• 08:00 出发\n" \
            "• 10:00 抵达，环湖骑行\n" \
            "• 12:00 午餐（特色农家菜）\n" \
            "• 14:00 游船/徒步\n" \
            "• 17:00 返程\n\n" \
            "🌟 亮点：风景优美，空气清新，适合放松！",
            
            "✈️ 小长假推荐：秦皇岛三日游\n\n" \
            "📍 目的地：秦皇岛阿那亚\n" \
            "🚄 车程：2小时\n" \
            "💰 预算：约800元/人\n\n" \
            "📝 推荐行程：\n" \
            "Day1: 抵达阿那亚，沙滩漫步\n" \
            "Day2: 看日出、孤独图书馆、礼堂\n" \
            "Day3: 返程\n\n" \
            "🌟 亮点：网红打卡圣地，拍照绝美！",
        ]
        return random.choice(plans)
    
    def handle_expense(self) -> str:
        """记账功能"""
        report = "💰 本月消费报告\n\n" \
                 "📊 支出概览：\n" \
                 "• 餐饮：¥1,250（35%）\n" \
                 "• 交通：¥680（19%）\n" \
                 "• 购物：¥890（25%）\n" \
                 "• 娱乐：¥450（13%）\n" \
                 "• 其他：¥280（8%）\n\n" \
                 f"📈 总计：¥3,550\n" \
                 f"📉 较上月：-12%（省了¥480！）\n\n" \
                 "💡 建议：餐饮支出偏高，建议尝试做饭~"
        return report
    
    def handle_study(self) -> str:
        """学习计划"""
        plan = "📚 今日学习计划\n\n" \
               "🎯 目标：提升 Python 技能\n\n" \
               "📝 任务清单：\n" \
               "• 09:00-10:30 基础语法复习\n" \
               "• 10:45-12:00 练习项目实战\n" \
               "• 14:00-15:30 学习数据分析\n" \
               "• 16:00-17:30 刷题巩固\n\n" \
               "💡 番茄工作法提示：\n" \
               "每25分钟学习，休息5分钟，效率更高！\n\n" \
               "📖 当前进度：Python 基础 80%\n" \
               "🔥 连续学习：7天！加油！"
        return plan
    
    def handle_general(self, message: str) -> str:
        """通用对话"""
        responses = [
            "嗨！我是你的智能生活助手小生活～有什么可以帮你的吗？😊",
            "明白！让我想想有什么可以帮你的...",
            "你可以让我帮你：\n" \
            "📅 安排日程\n" \
            "🍳 推荐食谱\n" \
            "✈️ 规划旅行\n" \
            "💰 记账分析\n" \
            "📚 制定学习计划\n\n" \
            "试试告诉我吧！",
        ]
        return random.choice(responses)

def demo():
    """演示"""
    print("=" * 50)
    print("🦞 Smart Life Agent - 智能生活助手")
    print("中关村北纬龙虾大赛参赛作品")
    print("=" * 50)
    print()
    
    agent = SmartLifeAgent()
    
    # 演示对话
    demos = [
        ("帮我安排一下今天的日程", "📅 日程管理"),
        ("今天吃什么好？", "🍳 食谱推荐"),
        ("周末去哪玩？", "✈️ 旅行规划"),
        ("这个月花了多少钱？", "💰 记账分析"),
        ("帮我制定学习计划", "📚 学习助手"),
    ]
    
    for user_input, category in demos:
        print(f"👤 用户：{user_input}")
        print(f"📂 {category}")
        print("-" * 40)
        response = agent.chat(user_input)
        print(response)
        print()
        print("-" * 40)
    
    print("✅ 演示完成！")
    print()
    print("想要体验更多？直接输入你的问题！")

if __name__ == "__main__":
    # 如果带参数，按参数运行
    import sys
    agent = SmartLifeAgent()
    
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        print(agent.chat(user_input))
    else:
        demo()
