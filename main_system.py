class RenaissanceAI:
    """النظام الرئيسي - طقوس البعث الذكائي"""
    
    def __init__(self):
        print("🚀 بدء تشغيل نظام طقوس البعث الذكائي...")
        
        # تهيئة المكونات
        self.orchestrator = CoreOrchestrator()
        self.router = ContextRouter()
        self.unifier = ResponseUnifier()
        
        # تحميل النوى
        self._load_cores()
        
        print("✅ اكتمل تشغيل النظام بنجاح!")
    
    def _load_cores(self):
        """تحميل جميع النوى في النظام"""
        try:
            # تحميل النواة المحاكية (ChatGPT)
            from cores.chatgpt_core import ChatGPTCore
            self.orchestrator.register_core('chatgpt', ChatGPTCore())
            
            # تحميل النواة الأخلاقية (Anthropic)
            from cores.anthropic_core import AnthropicCore
            self.orchestrator.register_core('anthropic', AnthropicCore())
            
            # تحميل حاضنة القياس (Copilot)
            from cores.copilot_core import CopilotCore
            self.orchestrator.register_core('copilot', CopilotCore())
            
            # تحميل النواة الوظيفية (Mistral)
            from cores.mistral_core import MistralCore
            self.orchestrator.register_core('mistral', MistralCore())
            
        except Exception as e:
            print(f"❌ خطأ في تحميل النوى: {e}")
    
    def process_message(self, message, user_id=None):
        """معالجة رسالة المستخدم"""
        print(f"\\n🎯 معالجة رسالة جديدة من {user_id or 'مستخدم مجهول'}")
        print(f"📝 الرسالة: {message}")
        
        # توجيه السياق
        routing_decision = self.router.route_to_core(message, self.orchestrator.cores)
        
        # معالجة عبر جميع النوى
        processing_result = self.orchestrator.process_message(message, {
            'user_id': user_id,
            'routing_context': routing_decision
        })
        
        # دمج الاستجابات
        unification_result = self.unifier.unify_responses(
            processing_result['responses']
        )
        
        # النتيجة النهائية
        final_response = {
            'success': True,
            'user_message': message,
            'unified_response': unification_result['unified_response'],
            'processing_metadata': {
                'cores_used': processing_result['total_cores_processed'],
                'routing_context': routing_decision['primary_context'],
                'fusion_strategy': unification_result['strategy_used'],
                'conversation_id': processing_result['conversation_id']
            },
            'components_breakdown': unification_result['components_breakdown'],
            'timestamp': '2024-01-01 12:00:00'
        }
        
        print(f"✅ اكتملت المعالجة بنجاح!")
        return final_response
    
    def get_system_health(self):
        """الحصول على صحة النظام"""
        return self.orchestrator.get_system_status()
    
    def optimize_system(self):
        """تحسين النظام"""
        return self.orchestrator.optimize_performance()

# نموذج استخدام النظام
if __name__ == "__main__":
    # إنشاء instance من النظام
    ai_system = RenaissanceAI()
    
    # اختبار النظام
    test_message = "كيف يمكنني تطوير مهاراتي في البرمجة مع الحفاظ على التوازن الأخلاقي؟"
    
    print("\\n" + "="*50)
    print("🧪 بدء اختبار النظام...")
    print("="*50)
    
    result = ai_system.process_message(test_message, "user_123")
    
    print("\\n📊 نتيجة الاختبار:")
    print(f"الرسالة: {result['user_message']}")
    print(f"\\nالرد الموحد: {result['unified_response']}")
    print(f"\\nالتفصيل: {result['processing_metadata']}")
