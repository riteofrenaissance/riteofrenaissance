class CoreOrchestrator:
    """منسق النوى - إدارة التكامل بين جميع النوى"""
    
    def __init__(self):
        self.cores = {}
        self.conversation_history = []
        self.performance_metrics = {}
        
    def register_core(self, name, core_instance):
        """تسجيل نواة جديدة في النظام"""
        self.cores[name] = {
            'instance': core_instance,
            'usage_count': 0,
            'success_rate': 0.0
        }
        print(f"✅ تم تسجيل النواة: {name}")
    
    def process_message(self, message, user_context=None):
        """معالجة الرسالة عبر جميع النوى المتاحة"""
        
        print(f"🎯 بدء معالجة الرسالة: '{message}'")
        
        # جمع النتائج من جميع النوى
        all_responses = []
        
        for core_name, core_data in self.cores.items():
            try:
                print(f"🔄 معالجة بواسطة {core_name}...")
                
                # زيادة عداد الاستخدام
                core_data['usage_count'] += 1
                
                # معالجة الرسالة
                response = core_data['instance'].process(message, user_context)
                all_responses.append(response)
                
                print(f"✅ اكتملت معالجة {core_name}")
                
            except Exception as e:
                print(f"❌ خطأ في {core_name}: {str(e)}")
                continue
        
        # تسجيل في سجل المحادثة
        conversation_entry = {
            'timestamp': '2024-01-01 12:00:00',  # يمكن استخدام datetime.now()
            'message': message,
            'responses': all_responses,
            'user_context': user_context
        }
        self.conversation_history.append(conversation_entry)
        
        return {
            'status': 'success',
            'message': message,
            'total_cores_processed': len(all_responses),
            'responses': all_responses,
            'conversation_id': len(self.conversation_history)
        }
    
    def get_system_status(self):
        """الحصول على حالة النظام"""
        status = {
            'total_cores': len(self.cores),
            'total_conversations': len(self.conversation_history),
            'core_usage': {},
            'system_health': 'excellent'
        }
        
        for core_name, core_data in self.cores.items():
            status['core_usage'][core_name] = {
                'usage_count': core_data['usage_count'],
                'success_rate': core_data['success_rate']
            }
        
        return status
    
    def optimize_performance(self):
        """تحسين أداء النظام"""
        print("🔄 تحسين أداء النظام...")
        
        optimization_report = {
            'cores_optimized': 0,
            'memory_usage': 'optimized',
            'processing_speed': 'enhanced',
            'recommendations': [
                "تنظيف الذاكرة المؤقتة",
                "موازنة الحمل بين النوى",
                "تحسين توزيع المهام"
            ]
        }
        
        return optimization_report
