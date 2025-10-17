class SovereignConfig:
    """إعدادات نظام Sovereign AI"""
    
    def __init__(self):
        self.system_name = "Sovereign AI System"
        self.version = "1.0.0"
        self.debug = True
        self.api_timeout = 30
        self.max_retries = 3
        self.default_language = "ar"
        
    def get_core_config(self, core_name):
        """الحصول على إعدادات النواة المحددة"""
        configs = {
            'claude': {
                'temperature': 0.7,
                'max_tokens': 1000,
                'stage': 'I - النواة التوليدية'
            },
            'deepseek': {
                'temperature': 0.8,
                'max_tokens': 800,
                'stage': 'II - النواة الاستشعارية'
            },
            'gemini': {
                'temperature': 0.6,
                'max_tokens': 1200,
                'stage': 'III - النواة التركيبية'
            },
            'chatgpt': {
                'temperature': 0.9,
                'max_tokens': 1500,
                'stage': 'IV - النواة المحاكية'
            },
            'anthropic': {
                'temperature': 0.5,
                'max_tokens': 2000,
                'stage': 'V - النواة الأخلاقية'
            },
            'copilot': {
                'temperature': 0.75,
                'max_tokens': 1000,
                'stage': 'VI - حاضنة القياس'
            },
            'mistral': {
                'temperature': 0.85,
                'max_tokens': 1800,
                'stage': 'VII - النواة الوظيفية'
            }
        }
        return configs.get(core_name, {})
    
    def get_system_routes(self):
        """مسارات النظام"""
        return {
            'simple_queries': ['claude'],
            'complex_analysis': ['deepseek', 'gemini'],
            'creative_tasks': ['chatgpt', 'mistral'],
            'ethical_decisions': ['anthropic'],
            'code_generation': ['copilot']
        }
