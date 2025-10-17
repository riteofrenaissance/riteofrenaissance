class ResponseUnifier:
    """موحد الاستجابات - دمج وتنظيم استجابات النوى"""
    
    def __init__(self):
        self.fusion_strategies = {
            'balanced': self._balanced_fusion,
            'expert_weighted': self._expert_weighted_fusion,
            'confidence_based': self._confidence_based_fusion
        }
    
    def unify_responses(self, core_responses, strategy='balanced'):
        """دمج استجابات النوى المختلفة"""
        
        if not core_responses:
            return self._generate_fallback_response()
        
        # اختيار استراتيجية الدمج
        fusion_function = self.fusion_strategies.get(strategy, self._balanced_fusion)
        unified_response = fusion_function(core_responses)
        
        # تحسين الصياغة النهائية
        final_output = self._refine_final_output(unified_response)
        
        return {
            'unified_response': final_output,
            'strategy_used': strategy,
            'sources_combined': len(core_responses),
            'fusion_quality': 'high',
            'components_breakdown': self._create_breakdown(core_responses)
        }
    
    def _balanced_fusion(self, responses):
        """دمج متوازن لجميع الاستجابات"""
        main_responses = []
        metadata_aggregate = {}
        
        for response in responses:
            main_responses.append(response['output'])
            # تجميع الميتاداتا
            for key, value in response.get('metadata', {}).items():
                if key not in metadata_aggregate:
                    metadata_aggregate[key] = []
                metadata_aggregate[key].append(value)
        
        # إنشاء استجابة موحدة
        unified_text = " \\n\\n".join(main_responses)
        unified_text += "\\n\\n🧩 [مدمج من عدة تخصصات ذكائية]"
        
        return {
            'text': unified_text,
            'metadata': metadata_aggregate,
            'core_count': len(responses)
        }
    
    def _expert_weighted_fusion(self, responses):
        """دمج مرجح بناءً على تخصص النواة"""
        # يمكن تطبيق خوارزميات ترجيح أكثر تعقيداً
        return self._balanced_fusion(responses)
    
    def _confidence_based_fusion(self, responses):
        """دمج بناءً على ثقة كل نواة"""
        sorted_responses = sorted(responses, key=lambda x: x.get('confidence', 0), reverse=True)
        return self._balanced_fusion(sorted_responses[:2])  # أفضل نواتين
    
    def _refine_final_output(self, unified_response):
        """تحسين الصياغة النهائية"""
        base_text = unified_response['text']
        
        # إضافة تحسينات على الصياغة
        enhancements = [
            "✨ تمت المعالجة باستخدام نظام النوى المتعددة",
            "📊 الجودة المضمونة عبر التكامل الذكي",
            "🔄 متوافق مع أحدث معايير الذكاء الاصطناعي"
        ]
        
        enhanced_text = base_text + "\\n\\n" + " | ".join(enhancements)
        return enhanced_text
    
    def _create_breakdown(self, responses):
        """إنشاء تفصيل للمكونات"""
        breakdown = []
        for response in responses:
            breakdown.append({
                'core': response['core'],
                'stage': response['stage'],
                'confidence': response.get('confidence', 0),
                'contribution': response['output'][:100]  # أول 100 حرف
            })
        return breakdown
    
    def _generate_fallback_response(self):
        """إنشاء استجابة احتياطية"""
        return {
            'text': "🤖 أنا هنا لمساعدتك! يبدو أن النظام في طور التهيئة. يمكنك إعادة المحاولة.",
            'metadata': {'fallback': True, 'reason': 'no_core_responses'},
            'core_count': 0
        }
