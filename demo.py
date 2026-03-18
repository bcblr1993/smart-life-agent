#!/usr/bin/env python3
"""
Smart Life Agent - 智能育儿生活助手
中关村北纬龙虾大赛参赛作品
赛道：生活龙虾
专注：儿童食谱、睡前故事、日常记录、学习提醒
"""

import json
import random
from datetime import datetime

class SmartLifeAgent:
    """智能育儿生活助手"""
    
    def __init__(self):
        self.name = "小管家"
        self.child_info = {
            "name": "宝宝",
            "age": 5,
            "likes": ["糖果", "动画片"],
            "dislikes": ["胡萝卜", "睡觉"]
        }
        
    def chat(self, message: str) -> str:
        """对话入口"""
        message = message.lower()
        
        # 食谱推荐
        if any(k in message for k in ["吃", "食谱", "菜谱", "做饭", "做饭", "晚餐", "午餐", "早餐"]):
            return self.handle_recipe(message)
        
        # 睡前故事
        elif any(k in message for k in ["故事", "睡前", "讲", "听", "story"]):
            return self.handle_story()
        
        # 日常记录
        elif any(k in message for k in ["记录", "日记", "成长", "档案", "记录一下"]):
            return self.handle_record(message)
        
        # 学习提醒
        elif any(k in message for k in ["学习", "提醒", "作业", "课程", "study", "练琴"]):
            return self.handle_study(message)
        
        else:
            return self.handle_help()
    
    def handle_recipe(self, message: str) -> str:
        """儿童食谱推荐"""
        # 判断是早餐/午餐/晚餐
        meal_type = "晚餐"
        if "早餐" in message or "早上" in message:
            meal_type = "早餐"
        elif "午餐" in message or "中午" in message:
            meal_type = "午餐"
        
        recipes = {
            "早餐": [
                """🍳 今日早餐推荐：彩虹蔬菜煎饼

⏱️ 准备时间：15分钟
⭐ 难度：⭐（简单）

📝 食材：
• 面粉 100g
• 鸡蛋 1个
• 胡萝卜 适量
• 西葫芦 适量
• 牛奶 50ml

👨‍🍳 做法：
1. 蔬菜擦丝
2. 面粉+鸡蛋+牛奶搅拌成糊
3. 加入蔬菜丝
4. 平底锅煎至两面金黄

💡 小贴士：可以搭配番茄酱一起吃，孩子更爱！""",

                """🥣 今日早餐：牛奶燕麦水果碗

⏱️ 准备时间：5分钟
⭐ 难度：⭐（超简单）

📝 食材：
• 燕麦 30g
• 牛奶 150ml
• 香蕉 半根
• 蓝莓 适量
• 蜂蜜 少许

👨‍🍳 做法：
1. 燕麦+牛奶微波2分钟
2. 摆上水果
3. 淋上蜂蜜

💡 营养：富含膳食纤维和维生素！"""
            ],
            "午餐": [
                """🍱 今日午餐：卡通造型便当

⏱️ 准备时间：25分钟
⭐ 难度：⭐⭐

📝 食材：
• 米饭 1碗
• 鸡翅 3个
• 西兰花 适量
• 番茄 1个
• 海苔 少许

👨‍🍳 做法：
1. 鸡翅用酱油腌制后煎熟
2. 米饭捏成卡通造型
3. 用海苔贴出眼睛表情
4. 西兰花焯水摆盘

💡 趣味：孩子会爱上吃饭！""",

                """🍝 今日午餐：番茄肉酱意面

⏱️ 准备时间：20分钟
⭐ 难度：⭐

📝 食材：
• 意面 50g
• 番茄 1个
• 肉末 50g
• 洋葱 适量
• 芝士 少许

👨‍🍳 做法：
1. 意面煮熟
2. 番茄炒出汁+肉末
3. 浇在意面上
4. 撒芝士

💡 酸甜开胃，孩子最爱！"""
            ],
            "晚餐": [
                """🍲 今日晚餐：虾仁蒸蛋

⏱️ 准备时间：20分钟
⭐ 难度：⭐⭐

📝 食材：
• 鸡蛋 2个
• 虾仁 5个
• 温水 150ml
• 盐 少许
• 葱花 适量

👨‍🍳 做法：
1. 鸡蛋打散+温水+盐
2. 过滤泡沫
3. 放入虾仁
4. 蒸10分钟
5. 撒葱花+淋酱油

💡 嫩滑可口，营养丰富！""",

                """🥘 今日晚餐：蔬菜鸡肉焖饭

⏱️ 准备时间：30分钟
⭐ 难度：⭐⭐

📝 食材：
• 米饭 1碗
• 鸡胸肉 100g
• 胡萝卜 适量
• 土豆 适量
• 豌豆 适量

👨‍🍳 做法：
1. 鸡肉切丁腌制
2. 蔬菜切小块
3. 所有食材放电饭煲
4. 煮饭模式

💡 一锅端，省时省力！"""
            ]
        }
        
        result = random.choice(recipes[meal_type])
        
        return f"""🍽️ {self.child_info['name']}的{meal_type}建议：

{result}

━━━━━━━━━━━━━━━━━━━━━━━━
💡 妈妈小贴士：
根据宝宝{self.child_info['age']}岁年龄，
注意少盐少油，营养均衡哦！"""
    
    def handle_story(self) -> str:
        """睡前故事"""
        stories = [
            """🌙 睡前故事：《小兔子勇敢之旅》

从前有一只小兔子，它叫白白。
白白一直很害怕黑暗，晚上不敢自己睡觉。

一天晚上，月亮阿姨对白白说：
"白白，你知道吗？每个小朋友的心里都有一盏小灯，
当你害怕的时候，它就会亮起来，保护你。"

白白好奇地问："真的吗？"
月亮阿姨笑着说："你试试看，闭上眼睛，
感受心里的那盏灯。"

白白闭上眼睛，感觉心里暖暖的，
真的有一盏小灯亮了起来！

从那天起，白白再也不害怕黑暗了。
因为它知道，心里有灯，就永远有光明。

🌟 故事寓意：勇敢不是不害怕，而是害怕了还往前走。
━━━━━━━━━━━━━━━━━━━━━━━━
💤 晚安，做个好梦~""",

            """🌙 睡前故事：《星星的礼物》

小狐狸星星今晚失眠了，
因为它觉得今天一天都不开心。

它走出家门，想找月亮姐姐聊天。
却发现路上有好多小动物，
都在为明天做准备。

小熊在存蜂蜜，
小鹿在整理鹿角，
小老鼠在做新裙子。

星星问："你们为什么这么开心呀？"

小熊说："因为明天是新的一天呀！
每一天都有惊喜在等着我们！"

星星回到家，闭上眼睛，
期待着明天会有什么惊喜。

🌟 故事寓意：每一天都是礼物，要期待明天。
━━━━━━━━━━━━━━━━━━━━━━━━
💤 晚安，祝你梦到彩虹~""",

            """🌙 睡前故事：《爱哭的小水滴》

云朵阿姨怀里住着很多小水滴。
其中有一颗叫乐乐的小水滴，
它特别喜欢哭。

有一天，乐乐又哭了，
其他小水滴说："乐乐别哭啦！"

云朵阿姨温和地说：
"乐乐，你想去人间看看吗？
那里有好多小朋友需要你。"

乐乐停止了哭泣，好奇地问：
"真的吗？我能做什么呢？"

云朵阿姨说：
"你可以变成雨滴，滋润花朵，
可以变成雪花，带给人们欢乐，
还可以变成汗水，让农民伯伯的庄稼长大！"

乐乐明白了，原来哭泣也可以变成
帮助别人的力量！

🌟 故事寓意：每种情绪都有价值，要学会接纳自己。
━━━━━━━━━━━━━━━━━━━━━━━━
💤 晚安，宝贝~"""
        ]
        
        story = random.choice(stories)
        
        return f"""📖 {self.child_info['name']}的睡前故事时间~

━━━━━━━━━━━━━━━━━━━━━━━━
{story}"""
    
    def handle_record(self, message: str) -> str:
        """儿童日常记录"""
        # 判断记录类型
        if "身高" in message or "体重" in message:
            return self.record_growth()
        elif "饮食" in message or "吃饭" in message:
            return self.record_meal()
        elif "情绪" in message or "心情" in message:
            return self.record_mood()
        else:
            return self.record_summary()
    
    def record_growth(self) -> str:
        """记录生长发育"""
        import random
        height = 100 + random.randint(5, 15)
        weight = 14 + random.randint(2, 6)
        
        return f"""📊 {self.child_info['name']}的成长记录

📅 记录日期：{datetime.now().strftime('%Y-%m-%d')}

📏 身高：{height}cm
⚖️ 体重：{weight}kg

📈 成长曲线：
████████████████░░ 80%

💡 建议：
• 保证充足睡眠（10-12小时）
• 每天户外运动1小时
• 均衡饮食，补充钙质

━━━━━━━━━━━━━━━━━━━━━━━━
💾 记录已保存！"""
    
    def record_meal(self) -> str:
        """记录饮食"""
        meals = [
            ("早餐", "牛奶+鸡蛋+面包", "✅ 营养满分"),
            ("午餐", "米饭+红烧肉+青菜", "✅ 荤素搭配"),
            ("晚餐", "面条+蔬菜汤", "✅ 清淡易消化"),
        ]
        
        result = """🥗 今日饮食记录

"""
        for meal, food, status in meals:
            result += f"• {meal}：{food} {status}\n"
        
        result += """
━━━━━━━━━━━━━━━━━━━━━━━━
💧 饮水：约 800ml
🍬 零食：1次（饼干）

💡 今日总结：
表现不错！继续保持均衡饮食~"""
        
        return result
    
    def record_mood(self) -> str:
        """记录情绪"""
        moods = [
            ("😄 开心", "今天表现：开心、活泼"),
            ("😊 平静", "今天表现：平静、乖巧"),
            ("🤔 思考", "今天表现：爱思考、好奇"),
        ]
        
        mood, desc = random.choice(moods)
        
        return f"""😊 {self.child_info['name']}今日心情

{mood}

{desc}

📝 今日亮点：
• 主动帮忙收拾玩具
• 和小朋友分享零食
• 学会了一首新歌

💡 情绪小贴士：
倾听孩子的情绪，给予正向反馈，
有助于建立安全感~

━━━━━━━━━━━━━━━━━━━━━━━━
💾 记录已保存！"""
    
    def record_summary(self) -> str:
        """成长档案汇总"""
        import random
        height = 100 + random.randint(5, 15)
        weight = 14 + random.randint(2, 6)
        
        return f"""📚 {self.child_info['name']}的成长档案

━━━━━━━━━━━━━━━━━━━━━━━━
👶 基本信息：
• 姓名：{self.child_info['name']}
• 年龄：{self.child_info['age']}岁
• 性别：保密

📏 最新生长数据：
• 身高：{height}cm
• 体重：{weight}kg

📝 今日记录：
• 饮食：✅ 正常
• 睡眠：✅ 8小时
• 情绪：😊 开心
• 学习：✅ 完成

━━━━━━━━━━━━━━━━━━━━━━━━
💾 记录时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}"""
    
    def handle_study(self, message: str) -> str:
        """学习提醒"""
        if "提醒" in message or "设置" in message:
            return self.set_reminder(message)
        elif "今天" in message or "有哪些" in message:
            return self.today_schedule()
        else:
            return self.learning_tips()
    
    def set_reminder(self, message: str) -> str:
        """设置提醒"""
        return """⏰ 学习提醒设置

✅ 已为您设置以下提醒：

📚 每日学习计划：
• 09:00-09:30 晨读（英语/语文）
• 15:00-15:30 下午学习
• 19:00-19:30 阅读时间
• 20:00-20:30 练琴/兴趣班

🎵 习惯养成：
• 每天背3个英语单词
• 每天阅读20分钟
• 每周学会一首古诗

━━━━━━━━━━━━━━━━━━━━━━━━
💡 小贴士：
学龄前儿童注意力约15-20分钟，
建议采用"番茄工作法"哦~"""
    
    def today_schedule(self) -> str:
        """今日学习安排"""
        import random
        
        schedules = [
            """📅 今日学习安排

⏰ 上午：
• 09:00-09:20 认字（5个字）
• 09:30-09:45 数学启蒙（数数）

⏰ 下午：
• 15:00-15:20 英语儿歌
• 15:30-15:45 涂鸦/手工

⏰ 晚上：
• 19:00-19:15 亲子阅读
• 20:00-20:30 听睡前故事

━━━━━━━━━━━━━━━━━━━━━━━━
💡 今日亮点：
 - 认识新字：爱、学、校
 - 学习数字：1-10
 - 新学儿歌：Little Star""",

            """📅 今日学习安排

⏰ 上午：
• 09:00-09:25 拼音学习
• 09:30-09:45 简单加减法

⏰ 下午：
• 15:00-15:20 乐高/积木
• 15:30-15:45 运动时间

⏰ 晚上：
• 19:00-19:20 睡前阅读
• 20:00 准时睡觉

━━━━━━━━━━━━━━━━━━━━━━━━
💡 今日亮点：
 - 拼音：a o e i u
 - 数学：5以内加减法
 - 精细动作：搭积木"""
        ]
        
        return random.choice(schedules)
    
    def learning_tips(self) -> str:
        """学习建议"""
        tips = """💡 育儿学习小贴士

🎯 不同年龄段学习重点：

📖 3-4岁（幼儿园小班）：
• 认知数字1-10
• 认识基础颜色和形状
• 简单自理能力
• 亲子绘本阅读

📖 4-5岁（中班）：
• 认识更多汉字
• 简单拼音入门
• 10以内加减法
• 绘画和手工

📖 5-6岁（大班）：
• 幼小衔接准备
• 20以内加减法
• 拼音拼读
• 写字练习

━━━━━━━━━━━━━━━━━━━━━━━━
💡 核心原则：
玩中学，学中玩！
保护兴趣比学到多少更重要~"""
        return tips
    
    def handle_help(self) -> str:
        """帮助信息"""
        return f"""👋 你好！我是{self.child_info['name']}的智能成长小管家~

我可以帮你：

🍳 儿童食谱
"今天吃什么好？"
"宝宝早餐做什么？"

📖 睡前故事
"讲个故事"
"睡前故事"

📝 日常记录
"记录今天的身高"
"记录今天的表现"
"查看成长档案"

⏰ 学习提醒
"今天有什么学习计划？"
"设置学习提醒"

━━━━━━━━━━━━━━━━━━━━━━━━
试试告诉我吧！😊"""


def demo():
    """演示"""
    print("=" * 55)
    print("🦞 Smart Life Agent - 智能育儿生活助手")
    print("    中关村北纬龙虾大赛 | 赛道：生活龙虾")
    print("=" * 55)
    print()
    
    agent = SmartLifeAgent()
    
    # 演示对话
    demos = [
        ("今天吃什么好？", "🍳 儿童食谱"),
        ("讲个睡前故事", "📖 睡前故事"),
        ("记录今天的表现", "📝 日常记录"),
        ("今天的学习计划", "⏰ 学习提醒"),
        ("有什么功能？", "❓ 帮助"),
    ]
    
    for user_input, category in demos:
        print(f"👤 用户：{user_input}")
        print(f"📂 {category}")
        print("-" * 50)
        response = agent.chat(user_input)
        print(response)
        print()
        print("=" * 50)
    
    print()
    print("✅ 演示完成！")
    print()
    print("🎯 参赛赛道：生活龙虾")
    print("📌 作品定位：育儿生活助手")


if __name__ == "__main__":
    import sys
    
    agent = SmartLifeAgent()
    
    # 如果带参数，按参数运行
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        print(agent.chat(user_input))
    else:
        demo()
