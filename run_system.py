#!/usr/bin/env python3
"""
نظام طقوس البعث الذكائي - Renaissance AI System
الإصدار 1.0 - تم التطوير باستخدام أحدث تقنيات الذكاء الاصطناعي
"""

import sys
import os

# إضافة المسارات
sys.path.append('cores')
sys.path.append('orchestrators') 
sys.path.append('routers')
sys.path.append('unifiers')

def main():
    print("🌅 بدء تشغيل نظام طقوس البعث الذكائي...")
    print("=" * 60)
    
    try:
        from main_system import RenaissanceAI
        
        # إنشاء النظام
        system = RenaissanceAI()
        
        print("\\n🟢 النظام جاهز للاستخدام!")
        print("\\n💡 يمكنك البدء بإرسال رسائل للنظام")
        print("📟 للخروج، اكتب 'exit' أو 'quit'")
        print("-" * 50)
        
        # حلقة تفاعلية
        while True:
            try:
                user_input = input("\\n👤 أنت: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'خروج']:
                    print("\\n👋 إلى اللقاء! شكراً لاستخدامك نظام طقوس البعث")
                    break
                
                if not user_input:
                    continue
                
                # معالجة الرسالة
                result = system.process_message(user_input, "interactive_user")
                
                print(f"\\n🤖 النظام: {result['unified_response']}")
                print(f"\\n🔧 [المعالجة باستخدام {result['processing_metadata']['cores_used']} نواة ذكائية]")
                
            except KeyboardInterrupt:
                print("\\n\\n👋 تم إيقاف النظام بواسطة المستخدم")
                break
            except Exception as e:
                print(f"\\n❌ خطأ في المعالجة: {e}")
                continue
                
    except Exception as e:
        print(f"❌ فشل في تشغيل النظام: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
