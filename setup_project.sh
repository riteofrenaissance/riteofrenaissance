#!/bin/bash

echo "🏗️  بدء تهيئة مشروع طقوس البعث الذكائي..."

# إنشاء الهيكل التنظيمي
mkdir -p cores orchestrators routers unifiers tests docs

# جعل ملفات التشغيل قابلة للتنفيذ
chmod +x run_system.py
chmod +x setup_project.sh

echo "✅ اكتملت التهيئة!"
echo "📁 الهيكل التنظيمي:"
find . -type f -name "*.py" | head -20

echo ""
echo "🚀 لتشغيل النظام:"
echo "   python run_system.py"
echo ""
echo "🧪 لاختبار النظام:"
echo "   python main_system.py"
