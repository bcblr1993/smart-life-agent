#!/bin/bash
# 🦞 小红书AI运营助手 - 演示脚本
# 用于现场展示

echo "========================================"
echo "🦞 小红书AI运营助手 - 现场演示"
echo "========================================"
echo ""

cd "$(dirname "$0")"

# 演示1：生成种草文案
echo "📝 演示1：生成种草文案"
echo "-----------------------------------"
python3 xiaohongshu_agent.py generate_post "降噪耳机" "数码"
echo ""

# 演示2：热点分析
echo "🔥 演示2：热点分析"
echo "-----------------------------------"
python3 xiaohongshu_agent.py analyze_hot "美妆"
echo ""

# 演示3：图片提示词
echo "🎨 演示3：AI图片提示词"
echo "-----------------------------------"
python3 xiaohongshu_agent.py generate_image_prompt "护肤品" "小清新"
echo ""

# 演示4：评论回复
echo "💬 演示4：评论回复"
echo "-----------------------------------"
python3 xiaohongshu_agent.py generate_reply "求链接"
echo ""

echo "========================================"
echo "✅ 演示完成！"
echo "========================================"
