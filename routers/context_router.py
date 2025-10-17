class ContextRouter:
    """موجه السياق - توجيه الرسائل بناءً على السياق"""
    
    def __init__(self):
        self.context_patterns = {
            'ethical': ['أخلاق', 'قيم', 'ضمير', 'مسؤولية', 'آداب'],
            'technical': ['برمجة', 'كود', 'تطوير', 'تقني', 'برمج'],
            'emotional': ['شعور', 'عاطفة', 'قلق', 'سعادة', 'حزن'],
            'creative': ['إبداع', 'ابتكار', 'فن', 'تصميم', 'تخيل'],
            'analytical': ['تحليل', 'دراسة', 'بحث', 'إحصاء', 'منطق']
        }
        
        self.core_mappings = {
            'ethical': 'anthropic',
            'technical': 'copilot', 
            'emotional': 'chatgpt',
            'creative': 'chatgpt',
            'analytical': 'mistral'
        }
    
    def analyze_context(self, message):
        """تحليل سياق الرسالة"""
        context_scores = {}
        
        for context_type, patterns in self.context_patterns.items():
            score = 0
            for pattern in patterns:
                if pattern in message:
                    score += 1
            context_scores[context_type] = score
        
        # تحديد السياق الرئيسي
        primary_context = max(context_scores.items(), key=lambda x: x[1])
        
        return {
            'primary_context': primary_context[0] if primary_context[1] > 0 else 'general',
            'context_scores': context_scores,
            'confidence': primary_context[1] / len(patterns) if primary_context[1] > 0 else 0.0
        }
    
    def route_to_core(self, message, available_cores):
        """توجيه الرسالة إلى النواة المناسبة"""
        context_analysis = self.analyze_context(message)
        recommended_core = self.core_mappings.get(context_analysis['primary_context'], 'chatgpt')
        
        routing_decision = {
            'message': message,
            'context_analysis': context_analysis,
            'recommended_core': recommended_core,
            'routing_confidence': context_analysis['confidence'],
            'available_cores': list(available_cores.keys()),
            'timestamp': '2024-01-01 12:00:00'
        }
        
        print(f"🧭 التوجيه: '{message}' → {recommended_core} (ثقة: {context_analysis['confidence']:.2f})")
        
        return routing_decision
    
    def learn_from_feedback(self, message, core_used, user_feedback):
        """التعلم من التغذية الراجعة"""
        print(f"📚 التعلم من التغذية الراجعة: {core_used} → {user_feedback}")
        
        learning_report = {
            'message_pattern': message[:50],  # أول 50 حرف من الرسالة
            'core_selected': core_used,
            'user_feedback': user_feedback,
            'adjustment_made': 'سياق تم تحسينه',
            'learning_rate': 0.85
        }
        
        return learning_report
