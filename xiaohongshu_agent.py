#!/usr/bin/env python3
"""
小红书AI运营助手 - 核心工具
用于中关村北纬龙虾大赛参赛作品
"""

import json
import random
from datetime import datetime

# ============ 热门话题库 ============
HOT_TOPICS = {
    "美妆": ["#早八人妆容", "#通勤妆", "#伪素颜", "#变美逆袭", "#化妆教程"],
    "护肤": ["#护肤分享", "#护肤好物", "#敏感肌", "#护肤routine", "#精简护肤"],
    "穿搭": ["#穿搭分享", "#ootd", "#通勤穿搭", "#平价穿搭", "#显瘦穿搭"],
    "美食": ["#美食分享", "#一人食", "#快手早餐", "#减脂餐", "#家常菜"],
    "家居": ["#家居好物", "#收纳分享", "#租房改造", "#居家美学", "#小户型"],
    "数码": ["#数码科技", "#数码测评", "#APP推荐", "#效率工具", "#数码好物"],
    "职场": ["#职场干货", "#职场技能", "#职场生存指南", "#工作日常", "#职场女性"],
    "情感": ["#情感分享", "#情感树洞", "#恋爱日常", "#单身日记", "#婚姻生活"],
    "健身": ["#健身日常", "#居家运动", "#健身打卡", "#减脂日记", "#马甲线"],
    "旅行": ["#旅行分享", "#周末去哪儿", "#小众旅行地", "#旅行攻略", "#穷游"],
}

# ============ 标题模板 ============
TITLE_TEMPLATES = [
    "绝绝子！这个{topic}也太好用了吧🔥",
    "姐妹们！{topic}终于被我搞明白了！",
    "{topic}yyds！用了再也离不开！",
    "答应我，{topic}一定要试试这个！",
    "私藏已久的{topic}分享！手慢无",
    "{topic}踩坑总结！不想踩坑的进",
    "{topic}一周体验报告！真实测评",
    "后悔没早知道的{topic}！真香",
]

# ============ 正文模板 ============
BODY_TEMPLATES = [
    """姐妹们！今天必须给你们安利{topic}👇

✨ 使用感受：
1. xxx
2. xxx
3. xxx

💰 性价比：
xxx

⭐ 总结：
xxx

#{} #{} #{}""",
    
    """{topic}也太卷了吧！但是这个方案真的绝👇

📌 核心亮点：
• xxx
• xxx
• xxx

💡 建议：
xxx

#{} #{} #{}""",
    
    """不会吧不会吧还有人不知道{topic}？

今天必须给你们科普一下👇

🔍 详细说明：
xxx

⚠️ 注意：
xxx

✅ 总结：
#{} #{} #{}""",
]

class XiaohongshuAgent:
    """小红书AI运营助手"""
    
    def __init__(self, name="小红虾"):
        self.name = name
        self.topics = HOT_TOPICS
    
    def generate_post(self, topic, category="美妆") -> dict:
        """生成小红书种草文案"""
        
        # 随机选择模板
        title_template = random.choice(TITLE_TEMPLATES)
        body_template = random.choice(BODY_TEMPLATES)
        
        # 生成标题
        title = title_template.format(topic=topic)
        
        # 生成正文
        body = body_template.format(topic=topic, 
                                    *random.sample(self.topics.get(category, ["#分享"]), 3))
        
        # 生成标签
        hashtags = random.sample(self.topics.get(category, ["#分享"]), 5)
        
        return {
            "title": title,
            "body": body,
            "hashtags": hashtags,
            "category": category,
            "timestamp": datetime.now().isoformat()
        }
    
    def analyze_hot(self, category="美妆") -> dict:
        """分析热门话题"""
        topics = self.topics.get(category, ["#分享"])
        
        return {
            "category": category,
            "hot_topics": topics,
            "trend": "上升中 📈",
            "suggestions": [
                f"可以结合{topics[0]}创作内容",
                f"近期{topics[1]}热度很高",
                f"建议尝试{topics[2]}相关内容"
            ],
            "timestamp": datetime.now().isoformat()
        }
    
    def generate_image_prompt(self, topic, style="小清新") -> dict:
        """生成AI绘画提示词"""
        
        prompts = {
            "小清新": f"{topic}, 清新风格, 浅色背景, 柔和光线, 简约布置, 高质感, 8k, 摄影作品",
            "高级感": f"{topic}, 高级感, 轻奢风格, 艺术感, 精致细节, 大片质感, 8k, 商业摄影",
            "可爱风": f"{topic}, 可爱风格, 卡通元素, 明亮色彩, 少女心, 梦幻氛围, 8k, 插画风格",
            "复古风": f"{topic}, 复古风格, 怀旧色调, 胶片质感, 复古配色, 怀旧氛围, 8k, 复古摄影",
        }
        
        return {
            "topic": topic,
            "style": style,
            "prompt": prompts.get(style, prompts["小清新"]),
            "suggestions": [
                "建议尺寸：3:4 (1456x1944)",
                "可加入文字：标题+关键词",
                "配色建议：白色/浅色背景更吸睛"
            ]
        }
    
    def generate_reply(self, comment_type="好评") -> dict:
        """生成评论回复"""
        
        replies = {
            "好评": [
                "谢谢姐妹喜欢！🥰 会继续努力分享更多好物的～",
                "太开心能得到认可！有问题随时问我哦～",
                "感谢支持！🙏 希望能帮到更多姐妹",
            ],
            "疑问": [
                "姐妹有什么问题可以问我哦～知无不言！",
                "问得好！具体是这样的xxx，有其他问题吗？",
                "欢迎提问呀～我会尽力解答的！",
            ],
            "负面": [
                "感谢反馈～会认真改进的！谢谢提醒",
                "抱歉给你带来不好的体验🥺 方便告诉我具体哪里需要改进吗？",
                "谢谢指出不足，我们会越做越好的！",
            ],
            "求链接": [
                "姐妹可以关注我，后面会出详细教程哦～",
                "正在整理中！关注我不要错过呀！",
                "链接不方便直接发，私信我告诉你呀～",
            ],
        }
        
        return {
            "type": comment_type,
            "replies": replies.get(comment_type, replies["好评"]),
            "tip": "根据评论具体内容选择合适回复，保持亲切友好的语气"
        }

# ============ CLI 接口 ============
def main():
    import sys
    
    agent = XiaohongshuAgent()
    
    if len(sys.argv) < 2:
        print("请选择功能：")
        print("1. generate_post - 生成种草文案")
        print("2. analyze_hot - 热点分析")
        print("3. generate_image_prompt - 图片提示词")
        print("4. generate_reply - 评论回复")
        return
    
    command = sys.argv[1]
    
    if command == "generate_post":
        topic = sys.argv[2] if len(sys.argv) > 2 else "好物"
        category = sys.argv[3] if len(sys.argv) > 3 else "美妆"
        result = agent.generate_post(topic, category)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif command == "analyze_hot":
        category = sys.argv[2] if len(sys.argv) > 2 else "美妆"
        result = agent.analyze_hot(category)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif command == "generate_image_prompt":
        topic = sys.argv[2] if len(sys.argv) > 2 else "美妆"
        style = sys.argv[3] if len(sys.argv) > 3 else "小清新"
        result = agent.generate_image_prompt(topic, style)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif command == "generate_reply":
        comment_type = sys.argv[2] if len(sys.argv) > 2 else "好评"
        result = agent.generate_reply(comment_type)
        print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
